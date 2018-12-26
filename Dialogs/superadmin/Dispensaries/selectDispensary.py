from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.Dispensaries.removeDispensary import *

class selectDispensary(object):
    def setup(self, selectDispensary):
        selectDispensary.setObjectName("selectDispensary")
        selectDispensary.resize(362, 330)
        self.title = QtWidgets.QLabel(selectDispensary)
        self.title.setGeometry(QtCore.QRect(30, 0, 321, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(selectDispensary)
        self.frame.setGeometry(QtCore.QRect(10, 60, 341, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(160, 120, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.dispensaryComboBox = QtWidgets.QComboBox(self.frame)
        self.dispensaryComboBox.setGeometry(QtCore.QRect(160, 170, 161, 27))
        self.dispensaryComboBox.setObjectName("dispensaryComboBox")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(160, 70, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(40, 120, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.dispensaryLabel = QtWidgets.QLabel(self.frame)
        self.dispensaryLabel.setGeometry(QtCore.QRect(40, 170, 111, 31))
        self.dispensaryLabel.setObjectName("dispensaryLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(40, 70, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.searchByID = QtWidgets.QLineEdit(self.frame)
        self.searchByID.setGeometry(QtCore.QRect(40, 10, 281, 27))
        self.searchByID.setObjectName("searchByID")
        self.ORLabel = QtWidgets.QLabel(self.frame)
        self.ORLabel.setGeometry(QtCore.QRect(120, 40, 111, 31))
        self.ORLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ORLabel.setObjectName("ORLabel")
        self.removeButton = QtWidgets.QPushButton(selectDispensary)
        self.removeButton.setGeometry(QtCore.QRect(140, 290, 80, 28))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(selectDispensary)
        QtCore.QMetaObject.connectSlotsByName(selectDispensary)

    def retranslateUi(self, selectDispensary):
        _translate = QtCore.QCoreApplication.translate
        selectDispensary.setWindowTitle(_translate("selectDispensary", " "))
        self.title.setText(_translate("selectDispensary", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Select Dispensary</span></p></body></html>"))
        self.cityLabel.setText(_translate("selectDispensary", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.dispensaryLabel.setText(_translate("selectDispensary", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Dispensary :</span></p></body></html>"))
        self.stateLabel.setText(_translate("selectDispensary", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.searchByID.setPlaceholderText(_translate("selectDispensary", "Search by Dispensary ID"))
        self.ORLabel.setText(_translate("selectDispensary", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">OR</span></p></body></html>"))
        self.removeButton.setText(_translate("selectDispensary", "SELECT"))

        self.stateAddFunction(selectDispensary)
        self.clickEvents(selectDispensary)

    def clickEvents(self, parent):
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveDispensary(parent))

    def clickOnRemoveDispensary(self, parent):
        self.window = QDialog()
        self.dialog = removeDispensary()
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