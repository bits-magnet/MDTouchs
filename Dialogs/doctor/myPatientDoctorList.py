from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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

class myPatientDoctorList(object):
    def setup(self, myPatientDoctorList,doctordata):
        self.doctordata = doctordata
        self.appointments = []
        myPatientDoctorList.setObjectName("myPatientDoctorList")
        myPatientDoctorList.resize(636, 480)
        self.frame = QtWidgets.QFrame(myPatientDoctorList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.patientLabel = QtWidgets.QLabel(self.frame)
        self.patientLabel.setGeometry(QtCore.QRect(230, 0, 191, 41))
        self.patientLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.patientLabel.setObjectName("patientLabel")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 41, 601, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.okButton = QtWidgets.QPushButton(myPatientDoctorList)
        self.okButton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(myPatientDoctorList)
        QtCore.QMetaObject.connectSlotsByName(myPatientDoctorList)

    def retranslateUi(self, myPatientDoctorList):
        _translate = QtCore.QCoreApplication.translate
        myPatientDoctorList.setWindowTitle(_translate("myPatientDoctorList", "My Patient List"))
        self.patientLabel.setText(_translate("myPatientDoctorList", "My Patients"))
        self.okButton.setText(_translate("myPatientDoctorList", "close"))
        self.events(myPatientDoctorList)

    def events(self,parent):
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
        import requests
        URL = "https://mdtouch.herokuapp.com/MDTouch/api/appointment/"
        params = {
            "doctor" : self.doctordata["id"],
            "status" : 1
        }
        r = requests.get(url=URL)
        self.appointments = r.json()
        ctr = 0
        for i in self.appointments:


            self.item  = Widget1()
            self.item.noticeIdLabel.setText("ID : " + str(i["id"]))
            self.item.noticeNameLabel.setText(str(i["title"]))
            self.tableWidget.setCellWidget(ctr,0,self.item)
            self.tableWidget.setRowHeight(ctr,50)
            ctr += 1
        self.tableWidget.cellClicked.connect(self.cellClick)

    def cellClick(self,row,col):
        pass


