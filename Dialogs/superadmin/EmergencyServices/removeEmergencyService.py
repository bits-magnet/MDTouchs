from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *

class removeEmergencyService(object):
    def setup(self, removeEmergencyService):
        removeEmergencyService.setObjectName("removeEmergencyService")
        removeEmergencyService.resize(470, 340)
        removeEmergencyService.setWindowTitle("")
        self.title = QtWidgets.QLabel(removeEmergencyService)
        self.title.setGeometry(QtCore.QRect(0, 10, 471, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(removeEmergencyService)
        self.frame.setGeometry(QtCore.QRect(10, 70, 451, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(200, 80, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.bloodBankComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodBankComboBox.setGeometry(QtCore.QRect(200, 140, 161, 27))
        self.bloodBankComboBox.setObjectName("bloodBankComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(200, 20, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.bloodBankLabel = QtWidgets.QLabel(self.frame)
        self.bloodBankLabel.setGeometry(QtCore.QRect(20, 140, 161, 31))
        self.bloodBankLabel.setObjectName("bloodBankLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.removeButton = QtWidgets.QPushButton(removeEmergencyService)
        self.removeButton.setGeometry(QtCore.QRect(190, 290, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(removeEmergencyService)
        QtCore.QMetaObject.connectSlotsByName(removeEmergencyService)

    def retranslateUi(self, removeEmergencyService):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("removeEmergencyService",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">REMOVE EMERGENCY SERVICE</span></p></body></html>"))
        self.cityLabel.setText(_translate("removeEmergencyService",
                                          "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.bloodBankLabel.setText(_translate("removeEmergencyService",
                                               "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Emergency Service :</span></p></body></html>"))
        self.stateLabel.setText(_translate("removeEmergencyService",
                                           "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.removeButton.setText(_translate("removeEmergencyService", "REMOVE"))

        self.clickEvents(removeEmergencyService)

    def clickEvents(self, parent):
        self.stateAddFunction(parent)

    def stateAddFunction(self,parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))

    def cityAddFunction(self,parent):
        state = self.stateComboBox.currentText()

        while self.cityComboBox.count() > 0:
            self.cityComboBox.removeItem(0)

        for i in cities[state]:
            self.cityComboBox.addItem(i)