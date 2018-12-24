from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *

class addTestCenter(object):
    def setup(self, addTestCenter):
        addTestCenter.setObjectName("addTestCenter")
        addTestCenter.resize(750, 500)
        self.title = QtWidgets.QLabel(addTestCenter)
        self.title.setGeometry(QtCore.QRect(260, 0, 261, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(addTestCenter)
        self.frame.setGeometry(QtCore.QRect(10, 60, 731, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(25, 20, 81, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(150, 20, 561, 41))
        self.name.setObjectName("name")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(25, 70, 91, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(25, 280, 131, 41))
        self.contactLabel.setObjectName("contactLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(25, 190, 61, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(25, 150, 91, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(25, 240, 61, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.address = QtWidgets.QTextEdit(self.frame)
        self.address.setGeometry(QtCore.QRect(150, 70, 561, 75))
        self.address.setObjectName("address")
        self.pinCode = QtWidgets.QLineEdit(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(150, 160, 181, 27))
        self.pinCode.setObjectName("pinCode")
        self.contact = QtWidgets.QLineEdit(self.frame)
        self.contact.setGeometry(QtCore.QRect(150, 290, 181, 27))
        self.contact.setInputMethodHints(QtCore.Qt.ImhNone)
        self.contact.setObjectName("contact")
        self.state = QtWidgets.QComboBox(self.frame)
        self.state.setGeometry(QtCore.QRect(150, 200, 181, 27))
        self.state.setObjectName("state")
        self.city = QtWidgets.QComboBox(self.frame)
        self.city.setGeometry(QtCore.QRect(150, 250, 181, 27))
        self.city.setObjectName("city")
        self.addButton = QtWidgets.QPushButton(addTestCenter)
        self.addButton.setGeometry(QtCore.QRect(330, 420, 131, 41))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(addTestCenter)
        QtCore.QMetaObject.connectSlotsByName(addTestCenter)

    def retranslateUi(self, addTestCenter):
        _translate = QtCore.QCoreApplication.translate
        addTestCenter.setWindowTitle(_translate("addTestCenter", "Dialog"))
        self.title.setText(_translate("addTestCenter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Add Test Center</span></p></body></html>"))
        self.nameLabel.setText(_translate("addTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("addTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("addTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("addTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("addTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("addTestCenter", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.addButton.setText(_translate("addTestCenter", "ADD"))

        self.clickEvents(addTestCenter)

    def clickEvents(self, parent):
        self.stateAddFunction(parent)

    def stateAddFunction(self,parent):
        for i in states.values():
            self.state.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.city.addItem(i)
        self.state.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))

    def cityAddFunction(self,parent):
        state = self.state.currentText()

        while self.city.count() > 0:
            self.city.removeItem(0)

        for i in cities[state]:
            self.city.addItem(i)
