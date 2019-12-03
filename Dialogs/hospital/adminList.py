
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Dialogs.messageBox import *

class Widget1(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self,parent=None)
        layout = QFrame(self)
        layout.setGeometry(0,0,600,50)
        self.noticeIdLabel = QLabel(layout)
        self.noticeIdLabel.setGeometry(QRect(10,10,150,30))
        self.noticeIdLabel.setText("Id : 123")
        self.noticeNameLabel = QLabel(layout)
        self.noticeNameLabel.setGeometry(QRect(180,10,500,30))

class adminList(object):
    def setup(self, adminList,hdata):
        self.hospitaldata = hdata
        adminList.setObjectName("adminList")
        adminList.resize(640, 480)
        self.frame = QtWidgets.QFrame(adminList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.adminListLabel = QtWidgets.QLabel(self.frame)
        self.adminListLabel.setGeometry(QtCore.QRect(250, 0, 131, 41))
        self.adminListLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.adminListLabel.setObjectName("adminListLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okbutton = QtWidgets.QPushButton(adminList)
        self.okbutton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okbutton.setObjectName("okbutton")
        self.okbutton.clicked.connect(lambda : adminList.close())

        self.retranslateUi(adminList)
        QtCore.QMetaObject.connectSlotsByName(adminList)

    def retranslateUi(self, adminList):
        _translate = QtCore.QCoreApplication.translate
        adminList.setWindowTitle(_translate("adminList", "Admins"))
        self.adminListLabel.setText(_translate("adminList", "<html><head/><body><p><span style=\" text-decoration: underline;\">Admin List</span></p></body></html>"))
        self.okbutton.setText(_translate("adminList", "close"))
        self.events(adminList)

    def events(self,parent):
        import requests
        URL = "https://mdtouchs.herokuapp.com/MDTouch/api/administrator/"
        params = {
            "workplace" : int(self.hospitaldata["id"])
        }
        r = requests.get(url=URL,params=params)
        l = r.json()
        if len(l) == 0:
            self.window = messageBox()
            self.window.infoBox("No Admin Found")
            parent.close()
            return
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAutoScrollMargin(100)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowHeight(0,120)
        self.tableWidget.setStyleSheet("background : rgb(255,255,255);")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tablewidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(l))
        ctr = 0
        for i in l:
            if ctr == 10:
                break

            self.item  = Widget1()
            self.item.noticeIdLabel.setText("ID : " + str(i["id"]))
            self.item.noticeNameLabel.setText(str(i["firstName"] + " " + i["lastName"]))
            self.tableWidget.setCellWidget(ctr,0,self.item)
            self.tableWidget.setRowHeight(ctr,50)
            ctr += 1




