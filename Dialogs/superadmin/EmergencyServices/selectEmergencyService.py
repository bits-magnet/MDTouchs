from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.EmergencyServices.removeEmergencyService import *

class selectEmergencyService(object):
    def setup(self, selectEmergencyService):
        selectEmergencyService.setObjectName("selectEmergencyService")
        selectEmergencyService.resize(415, 313)
        selectEmergencyService.setMinimumSize(QtCore.QSize(415, 313))
        selectEmergencyService.setMaximumSize(QtCore.QSize(415, 313))
        self.title = QtWidgets.QLabel(selectEmergencyService)
        self.title.setGeometry(QtCore.QRect(10, 0, 391, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectEmergencyService)
        self.frame.setGeometry(QtCore.QRect(10, 60, 391, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(200, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.emergencyServiceComboBox = QtWidgets.QComboBox(self.frame)
        self.emergencyServiceComboBox.setGeometry(QtCore.QRect(200, 160, 161, 27))
        self.emergencyServiceComboBox.setObjectName("emergencyServiceComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(200, 80, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(20, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.emergencyServiceLabel = QtWidgets.QLabel(self.frame)
        self.emergencyServiceLabel.setGeometry(QtCore.QRect(20, 160, 161, 31))
        self.emergencyServiceLabel.setObjectName("emergencyServiceLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(140, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(20, 10, 341, 27))
        self.searchByID.setObjectName("searchByID")
        self.removeButton = QtWidgets.QPushButton(selectEmergencyService)
        self.removeButton.setGeometry(QtCore.QRect(170, 280, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectEmergencyService)
        QtCore.QMetaObject.connectSlotsByName(selectEmergencyService)

    def retranslateUi(self, selectEmergencyService):
        _translate = QtCore.QCoreApplication.translate
        selectEmergencyService.setWindowTitle(_translate("selectEmergencyService", " "))
        self.title.setText(_translate("selectEmergencyService", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Select Emergency Service</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.emergencyServiceLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">E. Service :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.ORLabel.setText(_translate("selectEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectEmergencyService", "Search by Emergency Service ID"))
        self.removeButton.setText(_translate("selectEmergencyService", "SELECT"))

        self.stateAddFunction(selectEmergencyService)
        self.clickEvents(selectEmergencyService)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButton(parent))

    def clickOnRemoveButton(self, parent):
        self.window = QDialog()
        self.dialog = removeEmergencyService()
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
            self.cityComboBox.addItem(i)
