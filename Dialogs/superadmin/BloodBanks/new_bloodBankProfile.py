
from PyQt5 import QtCore, QtGui, QtWidgets
from Dialogs.bloodBank.bloodRecordsDialog import *
from Dialogs.superadmin.Events.myEventList import *
from Dialogs.bloodBank.bloodquantityList import *
class new_bloodBankProfile(object):
    def setup(self, bloodBankProfile,userdata):
        self.userdata = userdata
        bloodBankProfile.setObjectName("bloodBankProfile")
        bloodBankProfile.resize(553, 490)
        self.frame = QtWidgets.QFrame(bloodBankProfile)
        self.frame.setGeometry(QtCore.QRect(10, 10, 531, 431))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(25, 30, 101, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(25, 80, 101, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(25, 240, 131, 41))
        self.contactLabel.setObjectName("contactLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(295, 200, 101, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(25, 160, 101, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(25, 200, 101, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.address = QtWidgets.QTextBrowser(self.frame)
        self.address.setGeometry(QtCore.QRect(150, 80, 371, 61))
        self.address.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.address.setObjectName("address")
        self.pinCode = QtWidgets.QLabel(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(150, 170, 181, 21))
        self.pinCode.setStyleSheet("font-size:12pt;")
        self.pinCode.setObjectName("pinCode")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(350, 210, 181, 21))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(100, 210, 181, 21))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.contact = QtWidgets.QLabel(self.frame)
        self.contact.setGeometry(QtCore.QRect(150, 250, 181, 21))
        self.contact.setStyleSheet("font-size:12pt;")
        self.contact.setObjectName("contact")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(150, 30, 371, 41))
        self.name.setStyleSheet("font-size:16pt;")
        self.name.setObjectName("name")
        self.IDLabel = QtWidgets.QLabel(self.frame)
        self.IDLabel.setGeometry(QtCore.QRect(25, 0, 131, 41))
        self.IDLabel.setObjectName("IDLabel")
        self.bloodBankID = QtWidgets.QLabel(self.frame)
        self.bloodBankID.setGeometry(QtCore.QRect(150, 0, 371, 41))
        self.bloodBankID.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.bloodBankID.setObjectName("bloodBankID")
        self.bloodQuantitiesLabel = QtWidgets.QLabel(self.frame)
        self.bloodQuantitiesLabel.setGeometry(QtCore.QRect(30, 285, 191, 41))
        self.bloodQuantitiesLabel.setObjectName("bloodQuantitiesLabel")
        self.billingRecordsLabel = QtWidgets.QLabel(self.frame)
        self.billingRecordsLabel.setGeometry(QtCore.QRect(30, 330, 191, 31))
        self.billingRecordsLabel.setObjectName("billingRecordsLabel")
        self.eventsOrganizedLabel = QtWidgets.QLabel(self.frame)
        self.eventsOrganizedLabel.setGeometry(QtCore.QRect(30, 370, 191, 31))
        self.eventsOrganizedLabel.setObjectName("eventsOrganizedLabel")
        self.bloodQuantities = QtWidgets.QPushButton(self.frame)
        self.bloodQuantities.setGeometry(QtCore.QRect(230, 290, 111, 28))
        self.bloodQuantities.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.bloodQuantities.setObjectName("bloodQuantities")
        self.billingRecords = QtWidgets.QPushButton(self.frame)
        self.billingRecords.setGeometry(QtCore.QRect(230, 330, 111, 28))
        self.billingRecords.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.billingRecords.setObjectName("billingRecords")
        self.eventsOrganized = QtWidgets.QPushButton(self.frame)
        self.eventsOrganized.setGeometry(QtCore.QRect(230, 370, 111, 28))
        self.eventsOrganized.setStyleSheet("text-decoration:underline;\n"
"color:blue;\n"
"border:none;")
        self.eventsOrganized.setObjectName("eventsOrganized")
        self.pushButton = QtWidgets.QPushButton(bloodBankProfile)
        self.pushButton.setGeometry(QtCore.QRect(450, 450, 80, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(bloodBankProfile)
        QtCore.QMetaObject.connectSlotsByName(bloodBankProfile)

    def retranslateUi(self, bloodBankProfile):
        _translate = QtCore.QCoreApplication.translate
        bloodBankProfile.setWindowTitle(_translate("bloodBankProfile", "Blood Bank Profile"))
        self.nameLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.address.setPlaceholderText(_translate("bloodBankProfile", "Street, Landmark, Area"))
        self.pinCode.setText(_translate("bloodBankProfile", "PinCode"))
        self.state.setText(_translate("bloodBankProfile", "State"))
        self.city.setText(_translate("bloodBankProfile", "City"))
        self.contact.setText(_translate("bloodBankProfile", "1234567890"))
        self.name.setText(_translate("bloodBankProfile", "Name"))
        self.IDLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.bloodBankID.setText(_translate("bloodBankProfile", "BloodBankID"))
        self.bloodQuantitiesLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Blood Quantities:</span></p></body></html>"))
        self.billingRecordsLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Billing Records :</span></p></body></html>"))
        self.eventsOrganizedLabel.setText(_translate("bloodBankProfile", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Events Orgranized :</span></p></body></html>"))
        self.bloodQuantities.setText(_translate("bloodBankProfile", "Check Here"))
        self.billingRecords.setText(_translate("bloodBankProfile", "Check Here"))
        self.eventsOrganized.setText(_translate("bloodBankProfile", "Check Here"))
        self.pushButton.setText(_translate("bloodBankProfile", "OK"))

        self.events(bloodBankProfile,self.userdata)

    def events(self,parent,data):

        print(data)
        self.pinCode.setText(str(data["pin"]))
        self.bloodBankID.setText(str(data["id"]))
        self.name.setText(data['name'])
        self.address.setText(data["address"])
        self.contact.setText(str(data["contact"]))
        self.state.setText(data["state"])
        self.city.setText(data["city"])
        self.billingRecords.clicked.connect(lambda : self)
        self.pushButton.clicked.connect(lambda: parent.close())
        self.billingRecords.clicked.connect(lambda : self.clickOnBillingRecords(parent,data))
        self.eventsOrganized.clicked.connect(lambda : self.clickOneventOrganized(parent,data))
        self.bloodQuantities.clicked.connect(lambda : self.clickOnBloodQuantities(parent,data))

    def clickOnBillingRecords(self,parent,userdata):
        self.window = QDialog()
        self.dialog = bloodDialog()
        self.dialog.setup(self.window,userdata)
        self.window.setModal(True)
        self.window.show()


    def clickOneventOrganized(self,parent,userdata):
        self.window = QDialog()
        self.dialog = myEventList()
        self.dialog.setup(self.window,'BB',userdata)
        self.window.setModal(True)
        self.window.show()

    def clickOnBloodQuantities(self,parent,userdata):
        self.window = QDialog()
        self.dialog = bloodquanityList()
        self.dialog.setup(self.window,userdata)
        self.window.setModal(True)
        self.window.show()
