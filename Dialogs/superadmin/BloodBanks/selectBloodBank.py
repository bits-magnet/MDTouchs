from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.superadmin.BloodBanks.removeBloodBank import *
from Data.States import *

class selectBloodBank(object):
    def setup(self, selectBloodBank):
        selectBloodBank.setObjectName("selectBloodBank")
        selectBloodBank.resize(380, 350)
        self.frame = QtWidgets.QFrame(selectBloodBank)
        self.frame.setGeometry(QtCore.QRect(10, 60, 351, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 130, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.bloodBankComboBox = QtWidgets.QComboBox(self.frame)
        self.bloodBankComboBox.setGeometry(QtCore.QRect(160, 180, 161, 27))
        self.bloodBankComboBox.setObjectName("bloodBankComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 80, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 130, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.bloodBankLabel = QtWidgets.QLabel(self.frame)
        self.bloodBankLabel.setGeometry(QtCore.QRect(40, 180, 111, 31))
        self.bloodBankLabel.setObjectName("bloodBankLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 80, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(130, 50, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(40, 20, 281, 27))
        self.searchByID.setObjectName("searchByID")
        self.removeButton = QtWidgets.QPushButton(selectBloodBank)
        self.removeButton.setGeometry(QtCore.QRect(130, 310, 131, 28))
        self.removeButton.setObjectName("removeButton")
        self.title = QtWidgets.QLabel(selectBloodBank)
        self.title.setGeometry(QtCore.QRect(20, 0, 331, 51))
        self.title.setObjectName("title")

        self.retranslateUi(selectBloodBank)
        QtCore.QMetaObject.connectSlotsByName(selectBloodBank)

    def retranslateUi(self, selectBloodBank):
        _translate = QtCore.QCoreApplication.translate
        selectBloodBank.setWindowTitle(_translate("selectBloodBank", " "))
        self.cityLabel.setText(_translate("selectBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.bloodBankLabel.setText(_translate("selectBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Blood Bank :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.ORLabel.setText(_translate("selectBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectBloodBank", "Search by Blood Bank Id"))
        self.removeButton.setText(_translate("selectBloodBank", "SELECT"))
        self.title.setText(_translate("selectBloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Select Blood Bank</span></p></body></html>"))

        self.stateAddFunction(selectBloodBank)
        self.clickEvents(selectBloodBank)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveBloodBank(parent))

    def clickOnRemoveBloodBank(self, parent):
        self.window = QDialog()
        self.dialog = removeBloodBank()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

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