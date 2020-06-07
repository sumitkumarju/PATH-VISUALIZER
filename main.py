import sys
import time
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import QRectF
from PyQt5.Qt import Qt
from PyQt5 import QtCore
from view import Ui_Dialog

X_=[-1,0,0,1]
Y_=[0,-1,1,0]
sys.setrecursionlimit(10**6)

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.createGraphicView()
        self.matrix= [ [0 for i in range(56)] for j in range(34)]
        self.visited= [ [False for i in range(56)] for j in range(34)]
        #print((self.matrix))
        self.srt=False
        self.end=False
        self.startnode={}
        self.endnode={}
        self.clear.pressed.connect(self.createGraphicView)
        self.startnodeinput.toggled.connect(self.startselected)
        self.endnodeinput.toggled.connect(self.endselected)
        self.dfsinput.toggled.connect(self.dfs)

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
            self.scene.addLine(x,0,x,825, QPen(Qt.white))


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

    def dfs_util(self,x,y,x_,y_):
        if x==x_ and y==y_:
            print("found")
            return

        brush = QBrush()
        brush.setColor(Qt.white)
        brush.setStyle(Qt.SolidPattern)
        borderColor = Qt.black
        fillColor = Qt.red
        self.scene.addRect(QRectF(x*25,y*25, 25, 25),borderColor,brush)
        self.update()
        self.visited[x][y]=True

        for i in range(4):
            X=x+X_[i]
            Y=y+Y_[i]

            if X>=0 and X<=33 and y>=0 and y<=55 and self.visited[X][Y]==False and self.matrix[X][Y]!=1:
                print(X,Y)
                time.sleep(0.1)
                self.dfs_util(X,Y,x_,y_)

    def dfs(self):
        x=int(self.startnode['x']/25)
        y=int(self.startnode['y']/25)
        x_=int(self.endnode['x']/25)
        y_=int(self.endnode['y']/25)
        print("Initial ", x,y)
        print("Required ", x_,y_)
        self.dfs_util(x,y,x_,y_)




    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.MouseMove and source is self.graphicsView.viewport()):
            pos = event.pos()
            brush = QBrush()
            brush.setColor(Qt.yellow)
            brush.setStyle(Qt.SolidPattern)
            borderColor = Qt.black
            fillColor = Qt.red
            x=(pos.x()-pos.x()%25)
            y=(pos.y()-pos.y()%25)  #25 50
            self.matrix[int(y/25)][int(x/25)]=1
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
                self.startnode={'x':y,'y':x}
                self.matrix[int(y/25)][int(x/25)]=2
                brush.setColor(Qt.red)
                self.srt=False

            elif self.end:
                self.endnode={'x':y,'y':x}
                print(y/25,x/25)
                self.matrix[int(y/25)][int(x/25)]=3
                brush.setColor(Qt.green)
                self.end=False
            else:
                brush.setColor(Qt.yellow)
                self.matrix[int(y/25)][int(x/25)]=1



            #matrix[x][y]=1;

            self.scene.addRect(QRectF(x,y, 25, 25),borderColor,brush)
            #print((self.matrix))
            #print('mouse press: (%d, %d)' % (pos.x(), pos.y()))
        return QtWidgets.QWidget.eventFilter(self, source, event)




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

