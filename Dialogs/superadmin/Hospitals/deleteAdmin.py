# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteAdmin(object):
    def setupUi(self, deleteAdmin):
        deleteAdmin.setObjectName("deleteAdmin")
        deleteAdmin.resize(400, 350)
        self.title = QtWidgets.QLabel(deleteAdmin)
        self.title.setGeometry(QtCore.QRect(80, 0, 261, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(deleteAdmin)
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
        self.adminLabel = QtWidgets.QLabel(self.frame)
        self.adminLabel.setGeometry(QtCore.QRect(30, 170, 111, 31))
        self.adminLabel.setObjectName("adminLabel")
        self.adminComboBox = QtWidgets.QComboBox(self.frame)
        self.adminComboBox.setGeometry(QtCore.QRect(120, 170, 161, 27))
        self.adminComboBox.setObjectName("adminComboBox")
        self.deleteButton = QtWidgets.QPushButton(deleteAdmin)
        self.deleteButton.setGeometry(QtCore.QRect(160, 310, 80, 28))
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(deleteAdmin)
        QtCore.QMetaObject.connectSlotsByName(deleteAdmin)

    def retranslateUi(self, deleteAdmin):
        _translate = QtCore.QCoreApplication.translate
        deleteAdmin.setWindowTitle(_translate("deleteAdmin", " "))
        self.title.setText(_translate("deleteAdmin", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Delete Admin</span></p></body></html>"))
        self.cityLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.stateLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.adminLabel.setText(_translate("deleteAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Admin :</span></p></body></html>"))
        self.deleteButton.setText(_translate("deleteAdmin", "DELETE"))

