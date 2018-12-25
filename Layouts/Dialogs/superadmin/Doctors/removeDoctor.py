# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'removeDoctor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_removeDoctor(object):
    def setupUi(self, removeDoctor):
        removeDoctor.setObjectName("removeDoctor")
        removeDoctor.resize(400, 350)
        self.frame = QtWidgets.QFrame(removeDoctor)
        self.frame.setGeometry(QtCore.QRect(10, 60, 381, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(120, 70, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.hospitalComboBox = QtWidgets.QComboBox(self.frame)
        self.hospitalComboBox.setGeometry(QtCore.QRect(120, 120, 161, 27))
        self.hospitalComboBox.setObjectName("hospitalComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(120, 20, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(30, 70, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(30, 120, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(30, 20, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.doctorLabel = QtWidgets.QLabel(self.frame)
        self.doctorLabel.setGeometry(QtCore.QRect(30, 170, 111, 31))
        self.doctorLabel.setObjectName("doctorLabel")
        self.doctorComboBox = QtWidgets.QComboBox(self.frame)
        self.doctorComboBox.setGeometry(QtCore.QRect(120, 170, 161, 27))
        self.doctorComboBox.setObjectName("doctorComboBox")
        self.removeButton = QtWidgets.QPushButton(removeDoctor)
        self.removeButton.setGeometry(QtCore.QRect(160, 310, 80, 28))
        self.removeButton.setObjectName("removeButton")
        self.title = QtWidgets.QLabel(removeDoctor)
        self.title.setGeometry(QtCore.QRect(80, 0, 261, 51))
        self.title.setObjectName("title")

        self.retranslateUi(removeDoctor)
        QtCore.QMetaObject.connectSlotsByName(removeDoctor)

    def retranslateUi(self, removeDoctor):
        _translate = QtCore.QCoreApplication.translate
        removeDoctor.setWindowTitle(_translate("removeDoctor", " "))
        self.cityLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.stateLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.doctorLabel.setText(_translate("removeDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Doctor :</span></p></body></html>"))
        self.removeButton.setText(_translate("removeDoctor", "REMOVE"))
        self.title.setText(_translate("removeDoctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Remove Doctor</span></p></body></html>"))

