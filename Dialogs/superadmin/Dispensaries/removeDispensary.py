from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class removeDispensary(object):
    def setup(self, removeDispensary):
        removeDispensary.setObjectName("removeDispensary")
        removeDispensary.resize(400, 321)
        removeDispensary.setWindowTitle("")
        self.title = QtWidgets.QLabel(removeDispensary)
        self.title.setGeometry(QtCore.QRect(10, 0, 381, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(removeDispensary)
        self.frame.setGeometry(QtCore.QRect(10, 70, 381, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 80, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.dispensaryComboBox = QtWidgets.QComboBox(self.frame)
        self.dispensaryComboBox.setGeometry(QtCore.QRect(160, 130, 161, 27))
        self.dispensaryComboBox.setObjectName("dispensaryComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 30, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 80, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.dispensaryLabel = QtWidgets.QLabel(self.frame)
        self.dispensaryLabel.setGeometry(QtCore.QRect(40, 130, 111, 31))
        self.dispensaryLabel.setObjectName("dispensaryLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 30, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.removeButton = QtWidgets.QPushButton(removeDispensary)
        self.removeButton.setGeometry(QtCore.QRect(160, 280, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(removeDispensary)
        QtCore.QMetaObject.connectSlotsByName(removeDispensary)

    def retranslateUi(self, removeDispensary):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("removeDispensary",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">REMOVE DISPENSARY</span></p></body></html>"))
        self.cityLabel.setText(_translate("removeDispensary",
                                          "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.dispensaryLabel.setText(_translate("removeDispensary",
                                                "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dispensary :</span></p></body></html>"))
        self.stateLabel.setText(_translate("removeDispensary",
                                           "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.removeButton.setText(_translate("removeDispensary", "REMOVE"))

        self.clickEvents(removeDispensary)

    def clickEvents(self, parent):
        pass