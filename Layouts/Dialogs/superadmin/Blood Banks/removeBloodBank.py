# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeBloodBank.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_removeBloodBank(object):
    def setupUi(self, removeBloodBank):
        removeBloodBank.setObjectName("removeBloodBank")
        removeBloodBank.resize(400, 320)
        self.frame = QtWidgets.QFrame(removeBloodBank)
        self.frame.setGeometry(QtCore.QRect(10, 60, 381, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 80, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.bloodBankComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodBankComboBox.setGeometry(QtCore.QRect(160, 130, 161, 27))
        self.bloodBankComboBox.setObjectName("bloodBankComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 30, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 80, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.bloodBankLabel = QtWidgets.QLabel(self.frame)
        self.bloodBankLabel.setGeometry(QtCore.QRect(40, 130, 111, 31))
        self.bloodBankLabel.setObjectName("bloodBankLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 30, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.removeButton = QtWidgets.QPushButton(removeBloodBank)
        self.removeButton.setGeometry(QtCore.QRect(160, 270, 80, 28))
        self.removeButton.setObjectName("removeButton")
        self.title = QtWidgets.QLabel(removeBloodBank)
        self.title.setGeometry(QtCore.QRect(50, 0, 311, 51))
        self.title.setObjectName("title")

        self.retranslateUi(removeBloodBank)
        QtCore.QMetaObject.connectSlotsByName(removeBloodBank)

    def retranslateUi(self, removeBloodBank):
        _translate = QtCore.QCoreApplication.translate
        removeBloodBank.setWindowTitle(_translate("removeBloodBank", " "))
        self.cityLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.bloodBankLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Blood Bank :</span></p></body></html>"))
        self.stateLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.removeButton.setText(_translate("removeBloodBank", "REMOVE"))
        self.title.setText(_translate("removeBloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">REMOVE BLOOD BANK</span></p></body></html>"))

