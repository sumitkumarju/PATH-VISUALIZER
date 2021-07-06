import sys
import time
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt, QTimer
from PyQt5 import QtCore
from collections import deque
import numpy as np
import pickle
from view import Ui_Dialog
from queue import PriorityQueue

sys.setrecursionlimit(10**6)


ROW = 33
COL = 55

class Point:
    def __init__(self,x,y,pt=None):
        self.x = x
        self.y = y
        self.parent=pt

class queueNode:
    def __init__(self,pt: Point, dist: int):
        self.pt = pt
        self.dist = dist

def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)



rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]




class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.createGraphicView()

        self.matrix= [ [1 for i in range(55)] for j in range(33)]
        self.points= [ [Point(j,i) for i in range(55)] for j in range(33)]

        self.startnode={}
        self.endnode={}
        self.sfirst=True
        self.efirst=True
        self.wtlst=[]
        self.blklst=[]

        self.clearb.pressed.connect(self.clearmaze)
        self.clearp.pressed.connect(self.clearpath)
        self.clearw.pressed.connect(self.clearweight)
        self.visualize.pressed.connect(self.algorithm)

        self.speedInput.setMinimum(1)
        self.speedInput.setMaximum(1000)
        self.speedInput.setValue(500)
        self.delay = 0.002
        self.speedInput.setTickPosition(QSlider.TicksBelow)
        self.speedInput.setTickInterval(200)
        self.speedInput.valueChanged.connect(self.valuechange)




    def valuechange(self):
      self.delay = 1/self.speedInput.value()

    def clearmaze(self):
        self.scene.clear()
        self.wtlst=[]
        self.blklst=[]
        self.sfirst=True
        self.efirst=True
        self.matrix= [ [1 for i in range(55)] for j in range(33)]
        self.points= [ [Point(j,i) for i in range(55)] for j in range(33)]
        for x in range(0,1376,25):
            self.scene.addLine(x,0,x,825, QPen(Qt.black))
        for y in range(0,826,25):
            self.scene.addLine(0,y,1375,y, QPen(Qt.black))

    def clearweight(self):
        self.scene.clear()
        self.wtlst=[]
        self.blklst=[]
        self.matrix= [ [1 for i in range(55)] for j in range(33)]
        self.points= [ [Point(j,i) for i in range(55)] for j in range(33)]
        for x in range(0,1376,25):
            self.scene.addLine(x,0,x,825, QPen(Qt.black))
        for y in range(0,826,25):
            self.scene.addLine(0,y,1375,y, QPen(Qt.black))

        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        borderColor = Qt.black

        brush.setColor(Qt.red)
        self.scene.addRect(QRectF(self.startnode['x'],self.startnode['y'], 25, 25),borderColor,brush)

        brush.setColor(Qt.green)
        self.scene.addRect(QRectF(self.endnode['x'],self.endnode['y'], 25, 25),borderColor,brush)


    def clearpath(self):
        self.scene.clear()
        for x in range(0,1376,25):
            self.scene.addLine(x,0,x,825, QPen(Qt.black))
        for y in range(0,826,25):
            self.scene.addLine(0,y,1375,y, QPen(Qt.black))

        brush = QBrush()
        brush.setStyle(Qt.SolidPattern)
        borderColor = Qt.black

        brush.setColor(Qt.red)
        self.scene.addRect(QRectF(self.startnode['x'],self.startnode['y'], 25, 25),borderColor,brush)

        brush.setColor(Qt.green)
        self.scene.addRect(QRectF(self.endnode['x'],self.endnode['y'], 25, 25),borderColor,brush)

        brush.setColor(Qt.black)

        for x,y in self.wtlst:
            self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)

        brush.setColor(Qt.gray)

        for x,y in self.blklst:
            self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)


    def createGraphicView(self):
        self.scene  =QGraphicsScene()


        self.pen = QPen(Qt.red)

        self.graphicsView.setHorizontalScrollBarPolicy ( Qt.ScrollBarAlwaysOff )
        self.graphicsView.setVerticalScrollBarPolicy ( Qt.ScrollBarAlwaysOff )

        self.scene.setBackgroundBrush(Qt.white)

#       Drawing maze
        for x in range(0,1376,25):
            self.scene.addLine(x,0,x,825, QPen(Qt.black))


        for y in range(0,826,25):
            self.scene.addLine(0,y,1375,y, QPen(Qt.black))



        self.graphicsView.setScene(self.scene)

        self.graphicsView.viewport().installEventFilter(self)


    def algorithm(self):
        algo = self.algoInput.itemText(self.algoInput.currentIndex())
        if algo == "Breadth First Search":
            self.bfs()
        elif algo == "Depth First Search":
            self.dfs()
        elif algo == "A* Algorithm":
            self.a_star()
        elif algo == "Dijkstra\'s Algorithm":
            self.dijkstras()
        elif algo == "Greedy Best First Search":
            self.gbfs()

    def dijkstras(self):

        R=[[0 for i in range(55*33)] for j in range(33*55)]

        x_=int(self.endnode['y']/25)
        y_=int(self.endnode['x']/25)
        dest = x_*55+y_

        x=int(self.startnode['y']/25)
        y=int(self.startnode['x']/25)
        src = x*55+y

        for i in range(55*33):
            if(self.matrix[int(i/55)][i%55]):
                if i-1>=(int)(i/55)*55 and (self.matrix[int((i-1)/55)][(i-1)%55]):
                    R[i][i-1]=self.matrix[int((i-1)/55)][(i-1)%55]

                if (i+1)<((int)(i/55)+1)*55 and (self.matrix[int((i+1)/55)][(i+1)%55]):
                    R[i][i+1]=self.matrix[int((i+1)/55)][(i+1)%55]

                if (i-55)>=0 and (self.matrix[int((i-55)/55)][(i-55)%55]):
                    R[i][i-55]=self.matrix[int((i-55)/55)][(i-55)%55]

                if (i+55)<33*55 and (self.matrix[int((i+55)/55)][(i+55)%55]):
                    R[i][i+55]=self.matrix[int((i+55)/55)][(i+55)%55]

        open_set = []
        open_set.append((0,src))
        came_from = {}
        dist = {i: float("inf") for i in range(55*33)}
        dist[src] = 0
        open_set_hash = {src}
        while len(open_set):
            open_set.sort(key = lambda x: x[0])
            last = open_set.pop(0)
            # print(last[0])
            current = last[1]
            if current!=dest and current!=src:
                self.paint((current%55)*25,(int)(current/55)*25,Qt.cyan,0.01)

            # print(dist[current])
            open_set_hash.remove(current)

            if current == dest:
                print(f"Dijkstras path length={last[0]}")
                brush = QBrush()
                brush.setStyle(Qt.SolidPattern)
                borderColor = Qt.black
                brush.setColor(Qt.black)

                for x,y in self.wtlst:
                    self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)

                while current in came_from:
                    current = came_from[current]
                    if current!=src:
                        self.paint((current%55)*25,(int)(current/55)*25,Qt.darkCyan)
                return True

            for neighbor in range(55*33):
                if R[current][neighbor]>0:
                    temp_dist = dist[current] + R[current][neighbor]
                    if temp_dist < dist[neighbor]:
                        if neighbor  in open_set_hash:
                            open_set.remove((dist[neighbor],neighbor))
                            open_set_hash.remove(neighbor)
                        dist[neighbor] = temp_dist
                        came_from[neighbor] = current
                        open_set.append((dist[neighbor],neighbor))
                        open_set_hash.add(neighbor)


        print("Path does not exists")
        return False

    def dfs(self):

        R=[[0 for i in range(55*33)] for j in range(33*55)]

        x_=int(self.endnode['y']/25)
        y_=int(self.endnode['x']/25)
        dest = x_*55+y_

        x=int(self.startnode['y']/25)
        y=int(self.startnode['x']/25)
        src = x*55+y

        for i in range(55*33):
            if(self.matrix[int(i/55)][i%55]):
                if i-1>=(int)(i/55)*55 and (self.matrix[int((i-1)/55)][(i-1)%55]):
                    R[i][i-1]=1

                if (i+1)<((int)(i/55)+1)*55 and (self.matrix[int((i+1)/55)][(i+1)%55]):
                    R[i][i+1]=1

                if (i-55)>=0 and (self.matrix[int((i-55)/55)][(i-55)%55]):
                    R[i][i-55]=1

                if (i+55)<33*55 and (self.matrix[int((i+55)/55)][(i+55)%55]):
                    R[i][i+55]=1

        stack = []
        came_from = {}
        visited = {src}

        stack.append((src,0))

        while (len(stack)):

            t = stack[-1]
            current =t[0]
            d = t[1]
            stack.pop()



            if current!=src and current!=dest:
                self.paint((current%55)*25,(int)(current/55)*25,Qt.blue)
                self.paint((current%55)*25,(int)(current/55)*25,Qt.cyan)


            if current == dest:
                print(f"Deepest path length={d}")
                while current in came_from:
                    current = came_from[current]
                    if current!=src:
                        self.paint((current%55)*25,(int)(current/55)*25,Qt.darkCyan)
                return True
            visited.add(current)
            for neighbor in range(55*33):
                if R[current][neighbor]:
                    if neighbor not in visited:
                        came_from[neighbor]=current
                        stack.append((neighbor,d+1))

        print(f"Deepest path does not exist")
        return False



    def bfs(self):

        R=[[0 for i in range(55*33)] for j in range(33*55)]

        x_=int(self.endnode['y']/25)
        y_=int(self.endnode['x']/25)
        dest = x_*55+y_

        x=int(self.startnode['y']/25)
        y=int(self.startnode['x']/25)
        src = x*55+y

        for i in range(55*33):
            if(self.matrix[int(i/55)][i%55]):
                if i-1>=(int)(i/55)*55 and (self.matrix[int((i-1)/55)][(i-1)%55]):
                    R[i][i-1]=1

                if (i+1)<((int)(i/55)+1)*55 and (self.matrix[int((i+1)/55)][(i+1)%55]):
                    R[i][i+1]=1

                if (i-55)>=0 and (self.matrix[int((i-55)/55)][(i-55)%55]):
                    R[i][i-55]=1

                if (i+55)<33*55 and (self.matrix[int((i+55)/55)][(i+55)%55]):
                    R[i][i+55]=1


        q = deque()
        q.append((src,0))
        came_from = {}
        visited = {src}



        while q:

            t = q.popleft()
            current =t[0]
            d = t[1]


            if current!=src and current!=dest:
                self.paint((current%55)*25,(int)(current/55)*25,Qt.cyan)

            if current == dest:
                print(f"Shortest path length={d}")
                while current in came_from:
                    current = came_from[current]
                    if current!=src:
                        self.paint((current%55)*25,(int)(current/55)*25,Qt.darkCyan)
                return True


            for neighbor in range(55*33):
                if R[current][neighbor]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        came_from[neighbor]=current
                        if neighbor!=dest:
                            self.paint((neighbor%55)*25,(int)(neighbor/55)*25,Qt.blue)


                        q.append((neighbor,d+1))



        print("Shortest Path doesn't exist")
        return False



    def q_point(self):

        R=[[-1 for i in range(55*33)] for j in range(33*55)]

        x_=int(self.endnode['y']/25)
        y_=int(self.endnode['x']/25)
        dest = x_*55+y_

        x=int(self.startnode['y']/25)
        y=int(self.startnode['x']/25)
        src = x*55+y

        for i in range(55*33):
            if(self.matrix[int(i/55)][i%55]):
                if i-1>=(int)(i/55)*55 and (self.matrix[int((i-1)/55)][(i-1)%55]):
                    R[i][i-1]=0

                if (i+1)<((int)(i/55)+1)*55 and (self.matrix[int((i+1)/55)][(i+1)%55]):
                    R[i][i+1]=0

                if (i-55)>=0 and (self.matrix[int((i-55)/55)][(i-55)%55]):
                    R[i][i-55]=0

                if (i+55)<33*55 and (self.matrix[int((i+55)/55)][(i+55)%55]):
                    R[i][i+55]=0
                if i !=dest and i!=src:
                    self.paint((i%55)*25,(int)(i/55)*25,Qt.blue)



        print(dest)
        #Assigning rewards
        R[dest][dest]=100

        i=dest
        if i-1>=(int)(i/55)*55 and (self.matrix[int((i-1)/55)][(i-1)%55]):
            R[i][i-1]=100
            self.paint(((i-1)%55)*25,(int)((i-1)/55)*25,Qt.black)
        if (i+1)<((int)(i/55)+1)*55 and (self.matrix[int((i+1)/55)][(i+1)%55]):
            R[i][i+1]=100
            self.paint(((i+1)%55)*25,(int)((i+1)/55)*25,Qt.black)
        if (i-55)>=0 and (self.matrix[int((i-55)/55)][(i-55)%55]):
            R[i][i-55]=100
            self.paint(((i-55)%55)*25,(int)((i-55)/55)*25,Qt.black)

        if (i+55)<33*55 and (self.matrix[int((i+55)/55)][(i+55)%55]):
            R[i][i+55]=100
            self.paint(((i+55)%55)*25,(int)((i+55)/55)*25,Qt.black)

        R= np.mat(R)
        print(type(R))



        # Gamma (learning parameter).
        gamma = 0.8

        def available_actions(state):
            current_state_row = R[state,]
            av_act = np.where(current_state_row >= 0)[1]
            return av_act
        def sample_next_action(available_act):
            next_action = int(np.random.choice(available_act,1))
            return next_action

        def update(current_state, action, gamma):
            # if abs(current_state-action)!= 1 and abs(current_state-action)!= 55:
            #   print("update-",current_state,action)
            max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

            if max_index.shape[0] > 1:
                max_index = int(np.random.choice(max_index, size = 1))
            else:
                max_index = int(max_index)
            max_value = Q[action, max_index]

            # Q learning formula
            Q[current_state, action] = R[current_state, action] + gamma * max_value

        load = True

        if load:
            pickle_in = open(f'{dest}.pkl','rb')
            Q=pickle.load(pickle_in)

        else:
            Q = np.matrix(np.zeros([55*33,55*33]))


        # Train over  150000 iterations. (Re-iterate the process above).
        for i in range(50000):
            self.currentnodeInput.setText(f"{i}")
            current_state = np.random.randint(0, int(Q.shape[0]))

            available_act = available_actions(current_state)
            if len(available_act)==0:
                continue
            if current_state !=dest and current_state !=src:
                self.paint((current_state%55)*25,(int)(current_state/55)*25,Qt.white)
            action = sample_next_action(available_act)
            update(current_state,action,gamma)

        # Normalize the "trained" Q matrix
        print("Trained Q matrix:")

        print(src)
        count=0
        for i in range(33*55):
            #print(i,np.max(Q[i,]))
            if np.max(Q[i,])!=0.0:
                count+=1
        print(count)

        current_state = src
        steps = [current_state]

        while current_state != dest:

            next_step_index = np.where(Q[current_state,] == np.max(Q[current_state,]))[1]

            if next_step_index.shape[0] > 1:
                next_step_index = int(np.random.choice(next_step_index, size = 1))
            else:
                next_step_index = int(next_step_index)
            #if np.max(Q[current_state,]) == 0:
            #    print("No path")
            #    break
            #print((int)(next_step_index/55),next_step_index%55,Q[current_state, next_step_index])
            if next_step_index !=dest and next_step_index !=src:
                self.paint((next_step_index%55)*25,(int)(next_step_index/55)*25,Qt.darkCyan,0.01)
            steps.append(next_step_index)
            current_state = next_step_index

        # Print selected sequence of steps
        print("Selected path:")
        print(steps)


        f = open(f'{dest}.pkl','wb')
        pickle.dump(Q,f)
        f.close()

    def gbfs(self):
        def h(p1, p2):
            x1, y1 = p1/55,p1%55
            x2, y2 = p2/55,p2%55
            return abs(x1 - x2) + abs(y1 - y2)


        R=[[0 for i in range(55*33)] for j in range(33*55)]

        x_=int(self.endnode['y']/25)
        y_=int(self.endnode['x']/25)
        dest = x_*55+y_

        x=int(self.startnode['y']/25)
        y=int(self.startnode['x']/25)
        src = x*55+y

        for i in range(55*33):
            if(self.matrix[int(i/55)][i%55]):
                if i-1>=(int)(i/55)*55 and (self.matrix[int((i-1)/55)][(i-1)%55]):
                    R[i][i-1]=1

                if (i+1)<((int)(i/55)+1)*55 and (self.matrix[int((i+1)/55)][(i+1)%55]):
                    R[i][i+1]=1

                if (i-55)>=0 and (self.matrix[int((i-55)/55)][(i-55)%55]):
                    R[i][i-55]=1

                if (i+55)<33*55 and (self.matrix[int((i+55)/55)][(i+55)%55]):
                    R[i][i+55]=1

        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, src))
        came_from = {}
        f_score = {i: float("inf") for i in range(55*33)}
        f_score[src] = h(src,dest)

        open_set_hash = {src}

        while not open_set.empty():

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == dest:

                while current in came_from:
                    current = came_from[current]
                    if current!=src:
                        self.paint((current%55)*25,(int)(current/55)*25,Qt.darkCyan)
                return

            for neighbor in range(55*33):
                if R[current][neighbor]:
                    if h(neighbor, dest) < f_score[neighbor]:
                        h_score =  h(neighbor, dest)
                        came_from[neighbor] = current
                        f_score[neighbor] = h_score
                        if neighbor not in open_set_hash:
                            count += 1
                            open_set.put((f_score[neighbor], count, neighbor))
                            open_set_hash.add(neighbor)
                            if neighbor!=dest :
                                self.paint((neighbor%55)*25,(int)(neighbor/55)*25,Qt.cyan)



        print("Path does not exists")
        return False

    def a_star(self):

        def h(p1, p2):
            x1, y1 = p1/55,p1%55
            x2, y2 = p2/55,p2%55
            return abs(x1 - x2) + abs(y1 - y2)


        R=[[0 for i in range(55*33)] for j in range(33*55)]

        x_=int(self.endnode['y']/25)
        y_=int(self.endnode['x']/25)
        dest = x_*55+y_

        x=int(self.startnode['y']/25)
        y=int(self.startnode['x']/25)
        src = x*55+y

        for i in range(55*33):
            if(self.matrix[int(i/55)][i%55]):
                if i-1>=(int)(i/55)*55 and (self.matrix[int((i-1)/55)][(i-1)%55]):
                    R[i][i-1]=1

                if (i+1)<((int)(i/55)+1)*55 and (self.matrix[int((i+1)/55)][(i+1)%55]):
                    R[i][i+1]=1

                if (i-55)>=0 and (self.matrix[int((i-55)/55)][(i-55)%55]):
                    R[i][i-55]=1

                if (i+55)<33*55 and (self.matrix[int((i+55)/55)][(i+55)%55]):
                    R[i][i+55]=1

        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, src))
        came_from = {}
        g_score = {i: float("inf") for i in range(55*33)}
        g_score[src] = 0
        f_score = {i: float("inf") for i in range(55*33)}
        f_score[src] = h(src,dest)

        open_set_hash = {src}

        while not open_set.empty():

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == dest:

                while current in came_from:
                    current = came_from[current]
                    if current!=src:
                        self.paint((current%55)*25,(int)(current/55)*25,Qt.darkCyan)
                return

            for neighbor in range(55*33):
                if R[current][neighbor]:
                    temp_g_score = g_score[current] + 1

                    if temp_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = temp_g_score
                        f_score[neighbor] = temp_g_score + h(neighbor, dest)
                        if neighbor not in open_set_hash:
                            count += 1
                            open_set.put((f_score[neighbor], count, neighbor))
                            open_set_hash.add(neighbor)
                            if neighbor!=dest :
                                self.paint((neighbor%55)*25,(int)(neighbor/55)*25,Qt.cyan)



        print("Path does not exists")
        return False




    def paint(self,x,y,color,tym = 0):
        self.currentnodeInput.setText(f"({x},{y})")
        brush = QBrush()
        brush.setColor(color)
        brush.setStyle(Qt.SolidPattern)
        borderColor = Qt.black
        fillColor = Qt.red
        self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
        QApplication.processEvents()
        if tym == 0:
            tym=self.delay
        time.sleep(tym)


    def eventFilter(self, source, event):
        node = self.nodeInput.itemText(self.nodeInput.currentIndex())
        color = ""
        if node == "Start Node":
            color= Qt.red
        elif node == "Target Node":
            color= Qt.green
        elif node == "Bomb Node(Diffuse me first)":
            color= Qt.magenta
        elif node == "Weighted Node":
            color= Qt.black
        elif node == "Unweighted Node":
            color= Qt.gray
        if (event.type() == QtCore.QEvent.MouseMove and source is self.graphicsView.viewport()):
            pos = event.pos()
            brush = QBrush()
            brush.setColor(color)
            brush.setStyle(Qt.SolidPattern)
            borderColor = Qt.black
            fillColor = Qt.red
            x=(pos.x()-pos.x()%25)
            y=(pos.y()-pos.y()%25)
            if x<=1350 and y<=800: #25 50
                if color == Qt.gray:
                 self.matrix[int(y/25)][int(x/25)]=0
                 self.blklst.append((x,y))
                 self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
                elif color == Qt.black:
                 self.matrix[int(y/25)][int(x/25)]=10
                 self.wtlst.append((x,y))
                 self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)

        if (event.type() == QtCore.QEvent.MouseButtonPress and source is self.graphicsView.viewport()):

            pos = event.pos()
            brush = QBrush(color)
            brush.setStyle(Qt.SolidPattern)
            borderColor = Qt.black
            fillColor = Qt.red
            x=(pos.x()-pos.x()%25)
            y=(pos.y()-pos.y()%25)
            if x<=1350 and y<=800:
                if color == Qt.red and self.sfirst == True:
                    self.startnode={'x':x,'y':y}
                    self.sfirst = False
                    self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
                    self.matrix[int(y/25)][int(x/25)]=1
                    # matrix not used
                elif color == Qt.green and self.efirst == True:
                    self.endnode={'x':x,'y':y}
                    self.efirst = False
                    self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
                    #print(y/25,x/25)
                    self.matrix[int(y/25)][int(x/25)]=1
                elif color == Qt.gray:
                    self.matrix[int(y/25)][int(x/25)]=0
                    self.blklst.append((x,y))
                    self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
                elif color == Qt.black:
                    self.matrix[int(y/25)][int(x/25)]=10
                    self.wtlst.append((x,y))
                    self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)

        return QtWidgets.QWidget.eventFilter(self, source, event)





app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

