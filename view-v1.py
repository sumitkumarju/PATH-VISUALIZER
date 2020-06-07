# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import QRectF
from PyQt5.Qt import Qt

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1908, 1457)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 40, 654, 354))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setMouseTracking=True
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(710, 50, 114, 83))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startnodeinput = QtWidgets.QRadioButton(self.widget)
        self.startnodeinput.setObjectName("startnodeinput")
        self.verticalLayout.addWidget(self.startnodeinput)
        self.endnodeinput = QtWidgets.QRadioButton(self.widget)
        self.endnodeinput.setObjectName("endnodeinput")
        self.verticalLayout.addWidget(self.endnodeinput)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(710, 170, 138, 135))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.algorithms = QtWidgets.QLabel(self.widget1)
        self.algorithms.setAlignment(QtCore.Qt.AlignCenter)
        self.algorithms.setObjectName("algorithms")
        self.verticalLayout_2.addWidget(self.algorithms)
        self.bfsinput = QtWidgets.QRadioButton(self.widget1)
        self.bfsinput.setObjectName("bfsinput")
        self.verticalLayout_2.addWidget(self.bfsinput)
        self.dfsinput = QtWidgets.QRadioButton(self.widget1)
        self.dfsinput.setObjectName("dfsinput")
        self.verticalLayout_2.addWidget(self.dfsinput)
        self.dijkstrasinput = QtWidgets.QRadioButton(self.widget1)
        self.dijkstrasinput.setObjectName("dijkstrasinput")
        self.verticalLayout_2.addWidget(self.dijkstrasinput)
        self.bellinput = QtWidgets.QRadioButton(self.widget1)
        self.bellinput.setObjectName("bellinput")
        self.verticalLayout_2.addWidget(self.bellinput)
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(710, 340, 141, 58))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.visualize = QtWidgets.QPushButton(self.widget2)
        self.visualize.setObjectName("visualize")
        self.verticalLayout_3.addWidget(self.visualize)
        self.clear = QtWidgets.QPushButton(self.widget2)
        self.clear.setObjectName("clear")
        self.verticalLayout_3.addWidget(self.clear)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PATH VISUALIZER"))
        self.startnodeinput.setText(_translate("Dialog", "Start Node"))
        self.endnodeinput.setText(_translate("Dialog", "End Node"))
        self.radioButton_3.setText(_translate("Dialog", "Bar Node"))
        self.algorithms.setText(_translate("Dialog", "ALGORITHMS"))
        self.bfsinput.setText(_translate("Dialog", "BFS"))
        self.dfsinput.setText(_translate("Dialog", "DFS"))
        self.dijkstrasinput.setText(_translate("Dialog", "DIJKSTRAS"))
        self.bellinput.setText(_translate("Dialog", "BELLMAN FORD"))
        self.visualize.setText(_translate("Dialog", "VISUALIZE"))
        self.clear.setText(_translate("Dialog", "CLEAR"))


    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.drawing = True
    #         self.lastPoint = event.pos()
    #         brush = QBrush()
    #         brush.setColor(Qt.red)
    #         brush.setStyle(Qt.SolidPattern)
    #         borderColor = Qt.black
    #         fillColor = Qt.red
    #         x=(self.lastPoint.x()-self.lastPoint.x()%25)
    #         y=(self.lastPoint.y()-self.lastPoint.y()%25)
    #         self.scene.addRect(QRectF(x-25,y-50, 25, 25),borderColor,brush)
    #         print(self.lastPoint)
    #         print((self.lastPoint.x()-self.lastPoint.x()%25),(self.lastPoint.y()-self.lastPoint.y()%25))

    # def mouseMoveEvent(self, event):
    #      print(event.pos())
    #      if(event.buttons() & Qt.RightButton):
    #         self.lastPoint = event.pos()
    #         brush = QBrush()
    #         brush.setColor(Qt.white)
    #         brush.setStyle(Qt.SolidPattern)
    #         borderColor = Qt.black
    #         fillColor = Qt.red
    #         x=(self.lastPoint.x()-self.lastPoint.x()%25)
    #         y=(self.lastPoint.y()-self.lastPoint.y()%25)
    #         self.scene.addRect(QRectF(x-25,y-50, 25, 25),borderColor,brush)
    #         print("fuck")
    #         print(self.lastPoint)
    #         print((self.lastPoint.x()-self.lastPoint.x()%25),(self.lastPoint.y()-self.lastPoint.y()%25))
    #         self.update()

    # def mousePressEvent(self, event):
    #     self.__mousePressPos = None
    #     self.__mouseMovePos = None
    #     if event.button() == QtCore.Qt.LeftButton:
    #         self.__mousePressPos = event.globalPos()
    #         self.__mouseMovePos = event.globalPos()
    #         print(self.__mousePressPos)
    #         print(self.__mouseMovePos)
    #     super(self.graphicsView, self).mousePressEvent(event)

    # def mouseMoveEvent(self, event):
    #     if event.buttons() == QtCore.Qt.LeftButton:
    #         # adjust offset from clicked point to origin of widget
    #         currPos = self.mapToGlobal(self.pos())
    #         globalPos = event.globalPos()
    #         diff = globalPos - self.__mouseMovePos
    #         newPos = self.mapFromGlobal(currPos + diff)
    #         self.move(newPos)
    #         print(newPos)

    #         self.__mouseMovePos = globalPos

    #     super(self.graphicsView, self).mouseMoveEvent(event)

    # def mouseReleaseEvent(self, event):
    #     if self.__mousePressPos is not None:
    #         moved = event.globalPos() - self.__mousePressPos
    #         if moved.manhattanLength() > 3:
    #             event.ignore()
    #             return

    #     super(self.graphicsView, self).mouseReleaseEvent(event)

    # def mouseReleaseEvent(self, event):

    #     if event.button() == Qt.LeftButton:
    #         self.drawing = False
