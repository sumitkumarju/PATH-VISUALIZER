import sys
import time
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import QRectF
from PyQt5.Qt import Qt, QTimer
from PyQt5 import QtCore
from collections import deque

from view import Ui_Dialog

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
        self.clearb.pressed.connect(self.clearmaze)
        self.visualize.pressed.connect(self.algorithm)
        # node = self.nodeInput.itemText(self.nodeInput.currentIndex())
        # print(node)
        # if node == "Start Node":
        #     self.color= Qt.red
        # elif node == "Target Node":
        #     self.color= Qt.green
        # elif node == "Bomb Node":
        #     self.color= Qt.magenta
        # elif node == "Weighted Node":
        #     self.color= Qt.black
        # elif node == "Unweighted Node":
        #     self.color= Qt.gray


        # self.startnodeinput.pressed.connect(self.startselected)
        # self.endnodeinput.pressed.connect(self.endselected)
        # self.bfsinput.pressed.connect(self.bfs)
        # self.dfsinput.pressed.connect(self.dfs)





    def algorithm(self):
        algo = self.algoInput.itemText(self.algoInput.currentIndex())
        if algo == "Breadth First Search":
            self.bfs()
        elif algo == "Depth First Search":
            self.dfs()
    def clearmaze(self):
        self.scene.clear()
        self.matrix= [ [1 for i in range(55)] for j in range(33)]
        self.points= [ [Point(j,i) for i in range(55)] for j in range(33)]
        for x in range(0,1376,25):
            self.scene.addLine(x,0,x,825, QPen(Qt.black))
        for y in range(0,826,25):
            self.scene.addLine(0,y,1375,y, QPen(Qt.black))

    def createGraphicView(self):
        self.scene  =QGraphicsScene()


        self.pen = QPen(Qt.red)

        self.graphicsView.setHorizontalScrollBarPolicy ( Qt.ScrollBarAlwaysOff )
        self.graphicsView.setVerticalScrollBarPolicy ( Qt.ScrollBarAlwaysOff )

        self.scene.setBackgroundBrush(Qt.white)

        for x in range(0,1376,25):
            self.scene.addLine(x,0,x,825, QPen(Qt.black))


        for y in range(0,826,25):
            self.scene.addLine(0,y,1375,y, QPen(Qt.black))



        self.graphicsView.setScene(self.scene)

        self.graphicsView.viewport().installEventFilter(self)



    def dfs_util(self, src: Point, dest: Point,visited):

        visited = [[False for i in range(COL)] for j in range(ROW)]


        stack = []


        stack.append(src)
        first = True
        while (len(stack)):

            pt = stack[-1]
            stack.pop()

            if (not visited[pt.x][pt.y]):

                visited[pt.x][pt.y] = True

            if pt.x == dest.x and pt.y == dest.y:
                return 1

            if first == False:
             self.paint(pt.y*25,pt.x*25,Qt.blue,0.001)
             self.paint(pt.y*25,pt.x*25,Qt.cyan)

            first=False

            for i in range(4):
                row = pt.x + rowNum[i]
                col = pt.y + colNum[i]
                if (isValid(row,col) and self.matrix[row][col] == 1 and not visited[row][col]):
                    self.points[row][col].parent = pt
                    stack.append(Point(row,col))
        return -1

    def dfs(self):
        x=int(self.startnode['y']/25)
        y=int(self.startnode['x']/25)
        x_=int(self.endnode['y']/25)
        y_=int(self.endnode['x']/25)
        source = Point(x,y)
        dest = Point(x_,y_)
        visited = [[False for i in range(COL)] for j in range(ROW)]
        dist = self.dfs_util(source,dest,visited)

        if dist!=-1:
            print("Path exists")
            t= self.points[x_][y_].parent
            while t!=source:
                self.paint(t.y*25,t.x*25,Qt.darkCyan)
                t=self.points[t.x][t.y].parent
        else:
            print("Path doesn't exist")


    def bfs_util(self, src: Point, dest: Point):


        if self.matrix[src.x][src.y]!=1 or self.matrix[dest.x][dest.y]!=1:
            return -1

        visited = [[False for i in range(COL)] for j in range(ROW)]


        visited[src.x][src.y] = True


        q = deque()


        s = queueNode(src,0)
        q.append(s)
        first = True
        while q:

            curr = q.popleft()
            pt = curr.pt
            if pt.x == dest.x and pt.y == dest.y:
                return curr.dist

            if first == False:
             self.paint(pt.y*25,pt.x*25,Qt.cyan)

            first=False

            for i in range(4):
                row = pt.x + rowNum[i]
                col = pt.y + colNum[i]
                if (isValid(row,col) and self.matrix[row][col] == 1 and not visited[row][col]):
                    visited[row][col] = True
                    print(row*55+col)
                    self.points[row][col].parent = pt
                    Adjcell = queueNode(Point(row,col,pt),curr.dist+1)
                    if row == dest.x and col == dest.y:
                       return curr.dist+1

                    self.paint(col*25,row*25,Qt.blue)

                    q.append(Adjcell)


        return -1

    def bfs(self):
        x=int(self.startnode['y']/25)
        y=int(self.startnode['x']/25)
        x_=int(self.endnode['y']/25)
        y_=int(self.endnode['x']/25)
        source = Point(x,y)
        dest = Point(x_,y_)

        dist = self.bfs_util(source,dest)


        if dist!=-1:
            print("Shortest Path is",dist)
            t= self.points[x_][y_].parent
            while t!=source:
                self.paint(t.y*25,t.x*25,Qt.darkCyan,0.1)
                t=self.points[t.x][t.y].parent
        else:
            print("Shortest Path doesn't exist")



    def paint(self,x,y,color,tym=0.01):
        self.currentnodeInput.setText(f"({x},{y})")
        brush = QBrush()
        brush.setColor(color)
        brush.setStyle(Qt.SolidPattern)
        borderColor = Qt.black
        fillColor = Qt.red
        self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
        QApplication.processEvents()
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
                 self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
                elif color == Qt.black:
                 self.matrix[int(y/25)][int(x/25)]=2
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
                if color == Qt.red:
                    self.startnode={'x':x,'y':y}
                elif color == Qt.green:
                    self.endnode={'x':x,'y':y}
                    #print(y/25,x/25)
                    self.matrix[int(y/25)][int(x/25)]=1
                elif color == Qt.gray:
                    self.matrix[int(y/25)][int(x/25)]=0
                elif color == Qt.black:
                    self.matrix[int(y/25)][int(x/25)]=2
                self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)

        return QtWidgets.QWidget.eventFilter(self, source, event)





app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

