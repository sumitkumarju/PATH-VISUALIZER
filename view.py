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
        self.graphicsView.setGeometry(QtCore.QRect(20, 30, 1375, 825))
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(1430, 60, 131, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startnodeinput = QtWidgets.QRadioButton(self.layoutWidget)
        self.startnodeinput.setObjectName("startnodeinput")
        self.verticalLayout.addWidget(self.startnodeinput)
        self.endnodeinput = QtWidgets.QRadioButton(self.layoutWidget)
        self.endnodeinput.setObjectName("endnodeinput")
        self.verticalLayout.addWidget(self.endnodeinput)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(1430, 280, 141, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.algorithms = QtWidgets.QLabel(self.layoutWidget1)
        self.algorithms.setAlignment(QtCore.Qt.AlignCenter)
        self.algorithms.setObjectName("algorithms")
        self.verticalLayout_2.addWidget(self.algorithms)
        self.bfsinput = QtWidgets.QRadioButton(self.layoutWidget1)
        self.bfsinput.setObjectName("bfsinput")
        self.verticalLayout_2.addWidget(self.bfsinput)
        self.dfsinput = QtWidgets.QRadioButton(self.layoutWidget1)
        self.dfsinput.setObjectName("dfsinput")
        self.verticalLayout_2.addWidget(self.dfsinput)
        self.dijkstrasinput = QtWidgets.QRadioButton(self.layoutWidget1)
        self.dijkstrasinput.setObjectName("dijkstrasinput")
        self.verticalLayout_2.addWidget(self.dijkstrasinput)
        self.bellinput = QtWidgets.QRadioButton(self.layoutWidget1)
        self.bellinput.setObjectName("bellinput")
        self.verticalLayout_2.addWidget(self.bellinput)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(1430, 530, 141, 101))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.visualize = QtWidgets.QPushButton(self.layoutWidget2)
        self.visualize.setObjectName("visualize")
        self.verticalLayout_3.addWidget(self.visualize)
        self.clear = QtWidgets.QPushButton(self.layoutWidget2)
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

