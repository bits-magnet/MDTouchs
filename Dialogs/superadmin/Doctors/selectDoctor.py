from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.superadmin.Doctors.removeDoctor import *
from Dialogs.messageBox import *

class selectDoctor(object):
    def __init__(self):
        self.last_city = ''
        self.hospital_list = []
        self.doctor_list = []
        self.last_hospital = ''
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
    '''

        self.clickEvents(selectDoctor)

    def clickEvents(self, parent):
        self.stateAddFunction(selectDoctor)
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButton(parent))

    # Do Not Delete This Code Mrudul Add The Hospital ComboBox Here

    def clickOnRemoveButton(self, parent):
        id = self.searchByID.text()
        if id != "":
            if id.isdigit():
                import requests
                URL = "https://mdtouch.herokuapp.com/api/doctor/" + str(id)
                r = requests.get(url= URL)
                data = r.json()
                if data == {"detail": "Not found."}:
                    self.window = messageBox()
                    self.window.infoBox("Id Does Not Exists")
                    self.searchByID.setText("")
                    return
                else:
                    URL = "https://mdtouch.herokuapp.com/api/hospital/" + str(data["workplace"])
                    r = requests.get(url=URL)
                    hdata = r.json()
                    parent.close()
                    self.window = QDialog()
                    self.dialog =
                    self.dialog.setup(self.window,data,hdata)
                    self.window.setModal(True)
                    self.window.show()
                    return

            else:
                self.window = messageBox()
                self.window.infoBox("Id is a Integer")
                self.searchByID.setText("")
            return

        if self.doctorComboBox.count() == 0:
            self.window = messageBox()
            self.window.infoBox("Select the hospital first")
            return
        doctor_name = self.doctorComboBox.currentText()
        doctorData = {}
        hdata = {}
        for i in self.doctor_list:
            if doctor_name == i["firstName"] + " " + i["lastName"]:
                doctorData = i
                break
        for i in self.hospital_list:
            if i["name"] == self.hospitalComboBox.currentText():
                hdata = i
                break
        parent.close()
        self.window = QDialog()
        self.dialog = removeDoctor()
        self.dialog.setup(self.window,doctorData,hdata)
        self.window.setModal(True)
        self.window.show()


    def stateAddFunction(self,parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))
        self.stateComboBox.currentIndexChanged.connect(lambda :self.hospitalComboBoxAdd(parent))
        #self.stateComboBox.currentIndexChanged.connect(lambda : self.doctorComboBoxAdd(parent))

    def cityAddFunction(self,parent):
        state = self.stateComboBox.currentText()
        i = self.cityComboBox.count()
        flag = True
        while i > 0:
            flag = False
            self.cityComboBox.removeItem(0)
            i-=1
        flag = True
        for i in cities[state]:
            flag = False
            self.cityComboBox.addItem(i)
        flag = True
        self.cityComboBox.currentIndexChanged.connect(lambda :self.hospitalComboBoxAdd(parent))

    def hospitalComboBoxAdd(self,parent):
        if self.last_city == self.cityComboBox.currentText() or self.cityComboBox.count() != len(cities[self.stateComboBox.currentText()]) or self.cityComboBox.itemText(self.cityComboBox.count()-1) != cities[self.stateComboBox.currentText()][-1]:
            return
        self.last_city = self.cityComboBox.currentText()
        # First Erase all Hospitals
        i = self.hospitalComboBox.count()
        while i > 0:
            i -= 1
            self.hospitalComboBox.removeItem(0)

        import requests
        print(self.cityComboBox.currentText())
        URL = "https://mdtouch.herokuapp.com/api/hospital/"
        param ={
            "city": self.cityComboBox.currentText()
        }
        r = requests.get(url=URL,params=param)
        l = r.json()
        print(l)
        self.hospital_list = l
        for i in l:
            self.hospitalComboBox.addItem(str(i["name"]))
        self.hospitalComboBox.currentIndexChanged.connect(lambda : self.doctorComboBoxAdd(parent))

    def doctorComboBoxAdd(self,parent):
        i = self.doctorComboBox.count()
        while i > 0:
            i -= 1
            self.doctorComboBox.removeItem(0)
        workplace_id = 0
        print(self.hospital_list)
        for i in self.hospital_list:
            if i["name"] == self.hospitalComboBox.currentText():
                workplace_id = i["id"]
                break
        if workplace_id == 0:
            return

        print(workplace_id)
        import requests
        URL = "https://mdtouch.herokuapp.com/api/doctor/"
        param = {
            "workplace" : int(workplace_id)
        }
        r = requests.get(url=URL,params=param)
        self.doctor_list = r.json()
        print(self.doctor_list)
        for i in self.doctor_list:
            self.doctorComboBox.addItem(str(i["firstName"]) + " " + i["lastName"])
    '''


