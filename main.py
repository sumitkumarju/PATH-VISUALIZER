import sys
import time
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import QRectF
from PyQt5.Qt import Qt, QTimer
from PyQt5 import QtCore
from view import Ui_Dialog


sys.setrecursionlimit(10**6)

from collections import deque
ROW = 33
COL = 55

class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

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
        self.visited= [ [False for i in range(55)] for j in range(33)]
        #print((self.matrix))
        self.srt=False
        self.end=False
        self.startnode={}
        self.endnode={}
        self.clear.pressed.connect(self.createGraphicView)
        self.startnodeinput.toggled.connect(self.startselected)
        self.endnodeinput.toggled.connect(self.endselected)
        self.bfsinput.toggled.connect(self.bfs)
        self.dfsinput.toggled.connect(self.print)


    def print(self):
        print(self.startnode)
        print(self.endnode)
        print(self.matrix)
        brush = QBrush()
        brush.setColor(Qt.white)
        brush.setStyle(Qt.SolidPattern)
        borderColor = Qt.black
        fillColor = Qt.red
        for x in range(800,1300,25):
            for y in range(300,700,25):
                self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
                time.sleep(0.1)

        #self.update()

    def createGraphicView(self):
        self.scene  =QGraphicsScene()
        #self.greenBrush = QBrush(Qt.green)
        #self.grayBrush = QBrush(Qt.gray)

        self.pen = QPen(Qt.red)

        #self.shapes()
                  # Grid pattern.
        # self.scene.setBackgroundBrush(brush)


        # rect = QRectF(0.0, 0.0, 638, 378)         # Screen res or whatever.

        # self.scene.addRect(rect,borderColor,fillColor)  # Rectangle for color.Qt.green
        # self.scene.addRect(rect,borderColor,brush)

        self.graphicsView.setHorizontalScrollBarPolicy ( Qt.ScrollBarAlwaysOff )
        self.graphicsView.setVerticalScrollBarPolicy ( Qt.ScrollBarAlwaysOff )

        self.scene.setBackgroundBrush(Qt.black)

        for x in range(0,1376,25):
            self.scene.addLine(x,0,x,825, QPen(Qt.red))


        for y in range(0,826,25):
            self.scene.addLine(0,y,1375,y, QPen(Qt.white))



        self.graphicsView.setScene(self.scene)

        #self.graphicsView.setMouseTracking(True)
        self.graphicsView.viewport().installEventFilter(self)



    def startselected(self, selected):
        if selected:
            self.srt=True

    def endselected(self, selected):
        if selected:
            self.end=True

    # def dfs_util(self,x,y,x_,y_):
    #     if x==x_ and y==y_:
    #         print("found")
    #         return

        # brush = QBrush()
        # brush.setColor(Qt.white)
        # brush.setStyle(Qt.SolidPattern)
        # borderColor = Qt.black
        # fillColor = Qt.red
        # self.scene.addRect(QRectF(y*25,x*25, 25, 25),borderColor,brush)
        # self.update()
    #     time.sleep(0.1)
    #     self.visited[x][y]=True

    #     for i in range(4):
    #         X=x+X_[i]
    #         Y=y+Y_[i]

    #         if X>=0 and X<33 and y>=0 and y<55 and self.visited[X][Y]==False and self.matrix[X][Y]!=1:
    #             print(X,Y)
    #             self.dfs_util(X,Y,x_,y_)

    # def dfs(self):
        # x=int(self.startnode['y']/25)
        # y=int(self.startnode['x']/25)
        # x_=int(self.endnode['y']/25)
        # y_=int(self.endnode['x']/25)
    #     print("Initial ", x,y)
    #     print("Required ", x_,y_)
    #     self.dfs_util(x,y,x_,y_)


    def bfs_util(self, src: Point, dest: Point):


        if self.matrix[src.x][src.y]!=1 or self.matrix[dest.x][dest.y]!=1:
            return -1

        visited = [[False for i in range(COL)] for j in range(ROW)]


        visited[src.x][src.y] = True


        q = deque()


        s = queueNode(src,0)
        q.append(s)

        while q:

            curr = q.popleft()
            pt = curr.pt
            if pt.x == dest.x and pt.y == dest.y:
                return curr.dist

            self.paint(pt.y*25,pt.x*25)

            #print({pt.y*25},{pt.x*25})
            #self.x = f"QRectF({pt.y*25},{pt.x*25}, 25, 25)"
            #self.update()
            #QTimer.singleShot(2000, self.update)
            for i in range(4):
                row = pt.x + rowNum[i]
                col = pt.y + colNum[i]
                if (isValid(row,col) and self.matrix[row][col] == 1 and not visited[row][col]):
                    visited[row][col] = True
                    Adjcell = queueNode(Point(row,col),curr.dist+1)
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
        else:
            print("Shortest Path doesn't exist")


    def paint(self,x,y):
        print(x,y)
        brush = QBrush()
        brush.setColor(Qt.white)
        brush.setStyle(Qt.SolidPattern)
        borderColor = Qt.black
        fillColor = Qt.red
        self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
        self.update()
        time.sleep(0.001)


    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseMove and source is self.graphicsView.viewport()):
            pos = event.pos()
            brush = QBrush()
            brush.setColor(Qt.yellow)
            brush.setStyle(Qt.SolidPattern)
            borderColor = Qt.black
            fillColor = Qt.red
            x=(pos.x()-pos.x()%25)
            y=(pos.y()-pos.y()%25)
            if x<=1350 and y<=800: #25 50
                self.matrix[int(y/25)][int(x/25)]=0
                self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
            #print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
            #print("X=",self.startnode)
            #print("Y=",self.endnode)
        if (event.type() == QtCore.QEvent.MouseButtonPress and source is self.graphicsView.viewport() and event.button() == Qt.RightButton):
            pos = event.pos()
            brush = QBrush()
            brush.setStyle(Qt.SolidPattern)
            borderColor = Qt.black
            fillColor = Qt.red
            x=(pos.x()-pos.x()%25)
            y=(pos.y()-pos.y()%25)
            if self.srt:
                self.startnode={'x':x,'y':y}
                self.matrix[int(y/25)][int(x/25)]=1
                brush.setColor(Qt.red)
                self.srt=False

            elif self.end:
                self.endnode={'x':x,'y':y}
                print(y/25,x/25)
                self.matrix[int(y/25)][int(x/25)]=1
                brush.setColor(Qt.green)
                self.end=False
            else:
                brush.setColor(Qt.yellow)
                self.matrix[int(y/25)][int(x/25)]=0



            #matrix[x][y]=1;

            self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
            #print((self.matrix))
            #print('mouse press: (%d, %d)' % (pos.x(), pos.y()))
        return QtWidgets.QWidget.eventFilter(self, source, event)


    # def paintEvent(self, event):
    #     #lastPoint = event.pos()
    #     print(self.x)
        # brush = QBrush()
        # brush.setColor(Qt.white)
        #     brush.setStyle(Qt.SolidPattern)
        #     borderColor = Qt.black
        #     fillColor = Qt.red
        #     x=(self.lastPoint.x()-self.lastPoint.x()%25)
        #     y=(self.lastPoint.y()-self.lastPoint.y()%25)
        #     self.scene.addRect(QRectF(x-25,y-50, 25, 25),borderColor,brush)

    def shapes(self):
        ellipse = self.scene.addEllipse(20,20, 200,200, self.pen, self.greenBrush)
        rect = self.scene.addRect(-100,-100, 200,200, self.pen, self.grayBrush)

        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)
        ellipse.setFlag(QGraphicsItem.ItemIsSelectable)





app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

