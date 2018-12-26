from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.Doctors.removeDoctor import *

class selectDoctor(object):
    def setup(self, selectDoctor):
        selectDoctor.setObjectName("selectDoctor")
        selectDoctor.resize(380, 350)
        self.title = QtWidgets.QLabel(selectDoctor)
        self.title.setGeometry(QtCore.QRect(30, 0, 331, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectDoctor)
        self.frame.setGeometry(QtCore.QRect(10, 60, 351, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 130, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.doctorComboBox = QtWidgets.QComboBox(self.frame)
        self.doctorComboBox.setGeometry(QtCore.QRect(160, 180, 161, 27))
        self.doctorComboBox.setObjectName("doctorComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 80, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 130, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.doctorLabel = QtWidgets.QLabel(self.frame)
        self.doctorLabel.setGeometry(QtCore.QRect(40, 180, 111, 31))
        self.doctorLabel.setObjectName("doctorLabel")
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
        self.removeButton = QtWidgets.QPushButton(selectDoctor)
        self.removeButton.setGeometry(QtCore.QRect(130, 310, 131, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectDoctor)
        QtCore.QMetaObject.connectSlotsByName(selectDoctor)

    def retranslateUi(self, selectDoctor):
        _translate = QtCore.QCoreApplication.translate
        selectDoctor.setWindowTitle(_translate("selectDoctor", " "))
        self.title.setText(_translate("selectDoctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Select Doctor</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.doctorLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Doctor :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.ORLabel.setText(_translate("selectDoctor", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectDoctor", "Search by Doctor ID"))
        self.removeButton.setText(_translate("selectDoctor", "SELECT"))

        self.stateAddFunction(selectDoctor)
        self.clickEvents(selectDoctor)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButton(parent))

    def clickOnRemoveButton(self, parent):
        self.window = QDialog()
        self.dialog = removeDoctor()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()
            

    def stateAddFunction(self, parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda: self.cityAddFunction(parent))

    def cityAddFunction(self, parent):
        state = self.stateComboBox.currentText()

        while self.cityComboBox.count() > 0:
            self.cityComboBox.removeItem(0)

        for i in cities[state]:
            self.city.addItem(i)
