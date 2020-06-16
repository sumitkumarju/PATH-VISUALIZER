# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1598, 910)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(20, 30, 1381, 851))
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(1430, 530, 141, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.visualize = QtWidgets.QPushButton(self.layoutWidget)
        self.visualize.setObjectName("visualize")
        self.verticalLayout_3.addWidget(self.visualize)
        self.clear = QtWidgets.QPushButton(self.layoutWidget)
        self.clear.setObjectName("clear")
        self.verticalLayout_3.addWidget(self.clear)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(1430, 60, 141, 151))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startnodeinput = QtWidgets.QPushButton(self.widget)
        self.startnodeinput.setObjectName("startnode")
        self.verticalLayout.addWidget(self.startnodeinput)
        self.endnodeinput = QtWidgets.QPushButton(self.widget)
        self.endnodeinput.setObjectName("endnode")
        self.verticalLayout.addWidget(self.endnodeinput)
        self.bars = QtWidgets.QPushButton(self.widget)
        self.bars.setObjectName("bars")
        self.verticalLayout.addWidget(self.bars)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(1430, 280, 141, 201))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.algo = QtWidgets.QLabel(self.widget1)
        self.algo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.algo.setObjectName("algo")
        self.verticalLayout_2.addWidget(self.algo)
        self.bfsinput = QtWidgets.QPushButton(self.widget1)
        self.bfsinput.setObjectName("bfs")
        self.verticalLayout_2.addWidget(self.bfsinput)
        self.dfsinput = QtWidgets.QPushButton(self.widget1)
        self.dfsinput.setObjectName("dfs")
        self.verticalLayout_2.addWidget(self.dfsinput)
        self.dijkstra = QtWidgets.QPushButton(self.widget1)
        self.dijkstra.setObjectName("dijkstra")
        self.verticalLayout_2.addWidget(self.dijkstra)
        self.floyd = QtWidgets.QPushButton(self.widget1)
        self.floyd.setObjectName("floyd")
        self.verticalLayout_2.addWidget(self.floyd)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PATH VISUALIZER"))
        self.visualize.setText(_translate("Dialog", "VISUALIZE"))
        self.clear.setText(_translate("Dialog", "CLEAR"))
        self.startnodeinput.setText(_translate("Dialog", "Start Node"))
        self.endnodeinput.setText(_translate("Dialog", "End Node"))
        self.bars.setText(_translate("Dialog", "Bars"))
        self.algo.setText(_translate("Dialog", "       ALGORITHMS"))
        self.bfsinput.setText(_translate("Dialog", "BFS"))
        self.dfsinput.setText(_translate("Dialog", "DFS"))
        self.dijkstra.setText(_translate("Dialog", "Dijkstra"))
        self.floyd.setText(_translate("Dialog", "Floyd Warshall"))

