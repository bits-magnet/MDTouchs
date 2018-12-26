from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Pages.superadmin.Hospital import *
from Pages.superadmin.BloodBank import *
from Pages.superadmin.Doctor import *
from Pages.superadmin.Events import *
from Pages.superadmin.Dispensary import *
from Pages.superadmin.EmergencyService import *
from Pages.superadmin.TestCenter import *


class superadminHome(object):
    def setup(self, Home):
        Home.setObjectName("Home")
        Home.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home.sizePolicy().hasHeightForWidth())
        Home.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.eventLabel = QtWidgets.QLabel(self.centralwidget)
        self.eventLabel.setGeometry(QtCore.QRect(380, 260, 141, 51))
        self.eventLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.eventLabel.setObjectName("eventLabel")
        self.emergencyLabel = QtWidgets.QLabel(self.centralwidget)
        self.emergencyLabel.setGeometry(QtCore.QRect(1080, 260, 171, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emergencyLabel.sizePolicy().hasHeightForWidth())
        self.emergencyLabel.setSizePolicy(sizePolicy)
        self.emergencyLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.emergencyLabel.setObjectName("emergencyLabel")
        self.bloodLabel = QtWidgets.QLabel(self.centralwidget)
        self.bloodLabel.setGeometry(QtCore.QRect(600, 260, 190, 51))
        self.bloodLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bloodLabel.setObjectName("bloodLabel")
        self.doctorLabel = QtWidgets.QLabel(self.centralwidget)
        self.doctorLabel.setGeometry(QtCore.QRect(140, 580, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doctorLabel.sizePolicy().hasHeightForWidth())
        self.doctorLabel.setSizePolicy(sizePolicy)
        self.doctorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.doctorLabel.setObjectName("doctorLabel")
        self.testLabel = QtWidgets.QLabel(self.centralwidget)
        self.testLabel.setGeometry(QtCore.QRect(830, 260, 195, 51))
        self.testLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.testLabel.setObjectName("testLabel")
        self.dispensaryLabel = QtWidgets.QLabel(self.centralwidget)
        self.dispensaryLabel.setGeometry(QtCore.QRect(350, 580, 200, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dispensaryLabel.sizePolicy().hasHeightForWidth())
        self.dispensaryLabel.setSizePolicy(sizePolicy)
        self.dispensaryLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.dispensaryLabel.setObjectName("dispensaryLabel")
        self.settingsLabel = QtWidgets.QLabel(self.centralwidget)
        self.settingsLabel.setGeometry(QtCore.QRect(1090, 580, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsLabel.sizePolicy().hasHeightForWidth())
        self.settingsLabel.setSizePolicy(sizePolicy)
        self.settingsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.settingsLabel.setObjectName("settingsLabel")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1240, 10, 101, 91))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MDTouch/Images/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QtCore.QSize(80, 80))
        self.logout.setObjectName("logout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 130, 1301, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hospital = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hospital.sizePolicy().hasHeightForWidth())
        self.hospital.setSizePolicy(sizePolicy)
        self.hospital.setMaximumSize(QtCore.QSize(120, 120))
        self.hospital.setAutoFillBackground(False)
        self.hospital.setStyleSheet("border:none;")
        self.hospital.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MDTouch/Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hospital.setIcon(icon1)
        self.hospital.setIconSize(QtCore.QSize(100, 100))
        self.hospital.setObjectName("hospital")
        self.horizontalLayout.addWidget(self.hospital)
        self.events = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.events.sizePolicy().hasHeightForWidth())
        self.events.setSizePolicy(sizePolicy)
        self.events.setMinimumSize(QtCore.QSize(0, 0))
        self.events.setMaximumSize(QtCore.QSize(120, 120))
        self.events.setStyleSheet("border:none;")
        self.events.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../MDTouch/Images/event.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.events.setIcon(icon2)
        self.events.setIconSize(QtCore.QSize(100, 100))
        self.events.setObjectName("events")
        self.horizontalLayout.addWidget(self.events)
        self.bloodBank = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bloodBank.sizePolicy().hasHeightForWidth())
        self.bloodBank.setSizePolicy(sizePolicy)
        self.bloodBank.setMaximumSize(QtCore.QSize(120, 120))
        self.bloodBank.setStyleSheet("border:none;")
        self.bloodBank.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../MDTouch/Images/bloodbank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodBank.setIcon(icon3)
        self.bloodBank.setIconSize(QtCore.QSize(100, 100))
        self.bloodBank.setObjectName("bloodBank")
        self.horizontalLayout.addWidget(self.bloodBank)
        self.testCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testCenters.sizePolicy().hasHeightForWidth())
        self.testCenters.setSizePolicy(sizePolicy)
        self.testCenters.setMaximumSize(QtCore.QSize(120, 120))
        self.testCenters.setStyleSheet("border:none;")
        self.testCenters.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../MDTouch/Images/test_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testCenters.setIcon(icon4)
        self.testCenters.setIconSize(QtCore.QSize(100, 100))
        self.testCenters.setObjectName("testCenters")
        self.horizontalLayout.addWidget(self.testCenters)
        self.emergency = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emergency.sizePolicy().hasHeightForWidth())
        self.emergency.setSizePolicy(sizePolicy)
        self.emergency.setMaximumSize(QtCore.QSize(120, 120))
        self.emergency.setStyleSheet("border:none;")
        self.emergency.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../MDTouch/Images/emergency.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emergency.setIcon(icon5)
        self.emergency.setIconSize(QtCore.QSize(100, 100))
        self.emergency.setObjectName("emergency")
        self.horizontalLayout.addWidget(self.emergency)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 450, 1301, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.doctor = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doctor.sizePolicy().hasHeightForWidth())
        self.doctor.setSizePolicy(sizePolicy)
        self.doctor.setMaximumSize(QtCore.QSize(120, 120))
        self.doctor.setStyleSheet("border:none;")
        self.doctor.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../MDTouch/Images/doctor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctor.setIcon(icon6)
        self.doctor.setIconSize(QtCore.QSize(100, 100))
        self.doctor.setObjectName("doctor")
        self.horizontalLayout_2.addWidget(self.doctor)
        self.dispensary = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dispensary.sizePolicy().hasHeightForWidth())
        self.dispensary.setSizePolicy(sizePolicy)
        self.dispensary.setMaximumSize(QtCore.QSize(120, 120))
        self.dispensary.setStyleSheet("image: url(:/dispensary.png);\n"
"border:none;")
        self.dispensary.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../MDTouch/Images/dispensary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dispensary.setIcon(icon7)
        self.dispensary.setIconSize(QtCore.QSize(100, 100))
        self.dispensary.setObjectName("dispensary")
        self.horizontalLayout_2.addWidget(self.dispensary)
        self.users = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.users.sizePolicy().hasHeightForWidth())
        self.users.setSizePolicy(sizePolicy)
        self.users.setMaximumSize(QtCore.QSize(120, 120))
        self.users.setStyleSheet("border:none;")
        self.users.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../MDTouch/Images/users.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.users.setIcon(icon8)
        self.users.setIconSize(QtCore.QSize(100, 100))
        self.users.setObjectName("users")
        self.horizontalLayout_2.addWidget(self.users)
        self.analytics = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analytics.sizePolicy().hasHeightForWidth())
        self.analytics.setSizePolicy(sizePolicy)
        self.analytics.setMaximumSize(QtCore.QSize(120, 120))
        self.analytics.setStyleSheet("border:none;")
        self.analytics.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../MDTouch/Images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analytics.setIcon(icon9)
        self.analytics.setIconSize(QtCore.QSize(100, 100))
        self.analytics.setObjectName("analytics")
        self.horizontalLayout_2.addWidget(self.analytics)
        self.settings = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMaximumSize(QtCore.QSize(120, 120))
        self.settings.setStyleSheet("border:none;")
        self.settings.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../MDTouch/Images/settings.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon10)
        self.settings.setIconSize(QtCore.QSize(100, 100))
        self.settings.setObjectName("settings")
        self.horizontalLayout_2.addWidget(self.settings)
        self.analyticsLabel = QtWidgets.QLabel(self.centralwidget)
        self.analyticsLabel.setGeometry(QtCore.QRect(840, 580, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyticsLabel.sizePolicy().hasHeightForWidth())
        self.analyticsLabel.setSizePolicy(sizePolicy)
        self.analyticsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.analyticsLabel.setObjectName("analyticsLabel")
        self.usersLabel = QtWidgets.QLabel(self.centralwidget)
        self.usersLabel.setGeometry(QtCore.QRect(600, 580, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usersLabel.sizePolicy().hasHeightForWidth())
        self.usersLabel.setSizePolicy(sizePolicy)
        self.usersLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.usersLabel.setObjectName("usersLabel")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(550, 20, 255, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 50))
        self.title.setMaximumSize(QtCore.QSize(400, 70))
        self.title.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.title.setObjectName("title")
        self.hospitalLabel = QtWidgets.QLabel(self.centralwidget)
        self.hospitalLabel.setGeometry(QtCore.QRect(140, 260, 141, 51))
        self.hospitalLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.inbox = QtWidgets.QPushButton(self.centralwidget)
        self.inbox.setGeometry(QtCore.QRect(1130, 0, 80, 80))
        self.inbox.setMaximumSize(QtCore.QSize(100, 100))
        self.inbox.setStyleSheet("border:none;")
        self.inbox.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../MDTouch/Images/inbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inbox.setIcon(icon15)
        self.inbox.setIconSize(QtCore.QSize(80, 80))
        self.inbox.setObjectName("inbox")
        Home.setCentralWidget(self.centralwidget)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "MainWindow"))
        self.eventLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Events</span></p></body></html>"))
        self.emergencyLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Emergency</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Services</span></p></body></html>"))
        self.bloodLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Blood Banks</span></p></body></html>"))
        self.doctorLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Doctors</span></p></body></html>"))
        self.testLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Test Centers</span></p></body></html>"))
        self.dispensaryLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Dispensaries</span></p></body></html>"))
        self.settingsLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Settings</span></p></body></html>"))
        self.analyticsLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Statistics</span></p></body></html>"))
        self.usersLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Users</span></p></body></html>"))
        self.title.setText(_translate("Home", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.hospitalLabel.setText(_translate("Home", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Hospitals</span></p></body></html>"))

        self.clickEvents(Home)

    def clickEvents(self, parent):
        self.hospital.clicked.connect(lambda : self.clickOnHospital(parent))
        self.events.clicked.connect(lambda : self.clickOnEvents(parent))
        self.bloodBank.clicked.connect(lambda : self.clickOnBloodBank(parent))
        self.testCenters.clicked.connect(lambda: self.clickOnTestCenters(parent))
        self.emergency.clicked.connect(lambda : self.clickOnEmergency(parent))
        self.dispensary.clicked.connect(lambda : self.clickOnDispensary(parent))
        self.doctor.clicked.connect(lambda: self.clickOnDoctors(parent))
        self.users.clicked.connect(lambda: self.clickOnUsers(parent))
        self.analytics.clicked.connect(lambda : self.clickOnAnalytics(parent))
        self.settings.clicked.connect(lambda : self.clickOnSettings(parent))
        self.inbox.clicked.connect(lambda: self.clickOnInbox(parent))
        self.logout.clicked.connect(lambda : self.clickOnLogOut(parent))

        self.doctor_home = Doctor()
        self.hospital_home = Hospital()
        self.bloodbank_home = BloodBank()
        self.events_home = Events()
        self.dispensary_home = Dispensary()
        self.testcenter_home = TestCenter()
        self.emergency_home = Emergency()


    def clickOnHospital(self, parent):
        self.hospital_home.setup(parent,self)
    def clickOnEvents(self, parent):
        self.events_home.setup(parent,self)
    def clickOnBloodBank(self, parent):
        self.bloodbank_home.setup(parent,self)
    def clickOnTestCenters(self, parent):
        self.testcenter_home.setup(parent, self)
    def clickOnEmergency(self, parent):
        self.emergency_home.setup(parent, self)
    def clickOnDispensary(self, parent):
        self.dispensary_home.setup(parent, self)
    def clickOnDoctors(self, parent):
        self.doctor_home.setup(parent,self)
    def clickOnUsers(self, parent):
        pass
    def clickOnAnalytics(self, parent):
        pass
    def clickOnSettings(self, parent):
        pass
    def clickOnInbox(self, parent):
        pass
    def clickOnLogOut(self, parent):
        parent.loginpage.setup(parent)