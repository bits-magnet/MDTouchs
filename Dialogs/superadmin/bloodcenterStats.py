from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.Graphs.bloodReportGraph import *

class bloodcenterstats(object):
    def setup(self, bloodcenterstats):
        bloodcenterstats.setObjectName("bloodcenterstats")
        bloodcenterstats.resize(393, 409)
        self.titleLabel = QtWidgets.QLabel(bloodcenterstats)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 361, 41))
        self.titleLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")
        self.close = QtWidgets.QPushButton(bloodcenterstats)
        self.close.setGeometry(QtCore.QRect(140, 360, 89, 25))
        self.close.setObjectName("close")
        self.searchtcButton = QtWidgets.QPushButton(bloodcenterstats)
        self.searchtcButton.setGeometry(QtCore.QRect(20, 190, 161, 25))
        self.searchtcButton.setObjectName("searchtcButton")
        self.allBillsButton = QtWidgets.QPushButton(bloodcenterstats)
        self.allBillsButton.setGeometry(QtCore.QRect(190, 190, 161, 25))
        self.allBillsButton.setObjectName("allBillsButton")
        self.titleLabel_2 = QtWidgets.QLabel(bloodcenterstats)
        self.titleLabel_2.setGeometry(QtCore.QRect(10, 80, 241, 41))
        self.titleLabel_2.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.titleLabel_2.setObjectName("titleLabel_2")
        self.titleLabel_3 = QtWidgets.QLabel(bloodcenterstats)
        self.titleLabel_3.setGeometry(QtCore.QRect(-30, 130, 241, 41))
        self.titleLabel_3.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.titleLabel_3.setObjectName("titleLabel_3")
        self.frame_2 = QtWidgets.QFrame(bloodcenterstats)
        self.frame_2.setGeometry(QtCore.QRect(20, 240, 341, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tcid = QtWidgets.QLineEdit(self.frame_2)
        self.tcid.setGeometry(QtCore.QRect(80, 10, 181, 25))
        self.tcid.setObjectName("tcid")
        self.goToProfile = QtWidgets.QPushButton(self.frame_2)
        self.goToProfile.setGeometry(QtCore.QRect(170, 60, 151, 25))
        self.goToProfile.setObjectName("goToProfile")
        self.bloodstatsgraph = QtWidgets.QPushButton(self.frame_2)
        self.bloodstatsgraph.setGeometry(QtCore.QRect(10, 60, 161, 25))
        self.bloodstatsgraph.setObjectName("bloodstatsgraph")
        self.bbcRegistered = QtWidgets.QLabel(bloodcenterstats)
        self.bbcRegistered.setGeometry(QtCore.QRect(270, 90, 67, 17))
        self.bbcRegistered.setObjectName("bbcRegistered")
        self.totalbills = QtWidgets.QLabel(bloodcenterstats)
        self.totalbills.setGeometry(QtCore.QRect(270, 140, 67, 17))
        self.totalbills.setObjectName("totalbills")

        self.retranslateUi(bloodcenterstats)
        QtCore.QMetaObject.connectSlotsByName(bloodcenterstats)

    def retranslateUi(self, bloodcenterstats):
        _translate = QtCore.QCoreApplication.translate
        bloodcenterstats.setWindowTitle(_translate("bloodcenterstats", "Stats"))
        self.titleLabel.setText(_translate("bloodcenterstats", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; text-decoration: underline;\">Blood Center Stats</span></p><p align=\"center\"><br/></p></body></html>"))
        self.close.setText(_translate("bloodcenterstats", "close"))
        self.searchtcButton.setText(_translate("bloodcenterstats", "Search Blood Centers"))
        self.allBillsButton.setText(_translate("bloodcenterstats", "All Blood Bills"))
        self.titleLabel_2.setText(_translate("bloodcenterstats", "<html><head/><body><p align=\"center\">Blood Center Registered :</p></body></html>"))
        self.titleLabel_3.setText(_translate("bloodcenterstats", "<html><head/><body><p align=\"center\">Total Blood Bills:</p></body></html>"))
        self.tcid.setPlaceholderText(_translate("bloodcenterstats", "Enter Blood Center ID"))
        self.goToProfile.setText(_translate("bloodcenterstats", "Go To Profile"))
        self.bloodstatsgraph.setText(_translate("bloodcenterstats", "See Blood Stats"))
        self.bbcRegistered.setText(_translate("bloodcenterstats", "12"))
        self.totalbills.setText(_translate("bloodcenterstats", "24"))
        self.events(bloodcenterstats)

    def events(self,parent):
        self.bloodstatsgraph.clicked.connect(lambda : self.clickOnBloodGraph())


    def clickOnBloodGraph(self):

        self.window = QDialog()
        self.dialog = bloodbankGraph()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()
