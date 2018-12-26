# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountCreated.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_accountInfo(object):
    def setupUi(self, accountInfo):
        accountInfo.setObjectName("accountInfo")
        accountInfo.resize(452, 272)
        accountInfo.setMinimumSize(QtCore.QSize(452, 272))
        accountInfo.setMaximumSize(QtCore.QSize(452, 272))
        self.label = QtWidgets.QLabel(accountInfo)
        self.label.setGeometry(QtCore.QRect(20, 140, 141, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(accountInfo)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(accountInfo)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(accountInfo)
        self.label_4.setGeometry(QtCore.QRect(170, 90, 121, 41))
        self.label_4.setStyleSheet("font-size:12pt;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(accountInfo)
        self.label_5.setGeometry(QtCore.QRect(170, 140, 141, 41))
        self.label_5.setStyleSheet("font-size:12pt;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(accountInfo)
        self.label_6.setGeometry(QtCore.QRect(170, 190, 141, 31))
        self.label_6.setStyleSheet("font-size:12pt;")
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(accountInfo)
        self.frame.setGeometry(QtCore.QRect(10, 10, 431, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 391, 61))
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(accountInfo)
        self.label_8.setGeometry(QtCore.QRect(20, 230, 261, 41))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(accountInfo)
        self.pushButton.setGeometry(QtCore.QRect(340, 230, 80, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(accountInfo)
        QtCore.QMetaObject.connectSlotsByName(accountInfo)

    def retranslateUi(self, accountInfo):
        _translate = QtCore.QCoreApplication.translate
        accountInfo.setWindowTitle(_translate("accountInfo", "Account Created"))
        self.label.setText(_translate("accountInfo", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">username :</span></p></body></html>"))
        self.label_2.setText(_translate("accountInfo", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">password : </span></p></body></html>"))
        self.label_3.setText(_translate("accountInfo", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">ID : </span></p></body></html>"))
        self.label_4.setText(_translate("accountInfo", "id"))
        self.label_5.setText(_translate("accountInfo", "username"))
        self.label_6.setText(_translate("accountInfo", "password"))
        self.label_7.setText(_translate("accountInfo", "<html><head/><body><p><span style=\" font-size:12pt; color:#00ff00;\">Account Created !!!</span><span style=\" font-size:12pt;\"><br/>Please send these details to the account holder</span></p></body></html>"))
        self.label_8.setText(_translate("accountInfo", "<html><head/><body><p>Click OK to view Account Profile</p></body></html>"))
        self.pushButton.setText(_translate("accountInfo", "OK"))

