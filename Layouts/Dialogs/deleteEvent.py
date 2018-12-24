# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteEvent.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteEvent(object):
    def setupUi(self, deleteEvent):
        deleteEvent.setObjectName("deleteEvent")
        deleteEvent.resize(750, 500)
        self.title = QtWidgets.QLabel(deleteEvent)
        self.title.setGeometry(QtCore.QRect(240, 0, 261, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(deleteEvent)
        self.frame.setGeometry(QtCore.QRect(10, 60, 731, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 10, 271, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/sample_event.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(7, 7, 7);")
        self.widget.setObjectName("widget")
        self.eventNameLabel = QtWidgets.QLabel(self.frame)
        self.eventNameLabel.setGeometry(QtCore.QRect(310, 10, 91, 31))
        self.eventNameLabel.setObjectName("eventNameLabel")
        self.eventNameLabel_2 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_2.setGeometry(QtCore.QRect(400, 10, 221, 31))
        self.eventNameLabel_2.setStyleSheet("font-size:12pt;\n"
"background-color: rgb(255, 255, 255);")
        self.eventNameLabel_2.setObjectName("eventNameLabel_2")
        self.eventNameLabel_3 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_3.setGeometry(QtCore.QRect(10, 250, 91, 31))
        self.eventNameLabel_3.setObjectName("eventNameLabel_3")
        self.eventNameLabel_4 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_4.setGeometry(QtCore.QRect(310, 190, 131, 41))
        self.eventNameLabel_4.setObjectName("eventNameLabel_4")
        self.eventNameLabel_5 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_5.setGeometry(QtCore.QRect(310, 70, 71, 31))
        self.eventNameLabel_5.setObjectName("eventNameLabel_5")
        self.eventNameLabel_6 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_6.setGeometry(QtCore.QRect(310, 130, 81, 31))
        self.eventNameLabel_6.setObjectName("eventNameLabel_6")
        self.eventNameLabel_7 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_7.setGeometry(QtCore.QRect(100, 250, 181, 31))
        self.eventNameLabel_7.setStyleSheet("font-size:12pt;\n"
"background-color: rgb(255, 255, 255);")
        self.eventNameLabel_7.setObjectName("eventNameLabel_7")
        self.eventNameLabel_8 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_8.setGeometry(QtCore.QRect(400, 70, 221, 31))
        self.eventNameLabel_8.setStyleSheet("font-size:12pt;\n"
"background-color: rgb(255, 255, 255);")
        self.eventNameLabel_8.setObjectName("eventNameLabel_8")
        self.eventNameLabel_9 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_9.setGeometry(QtCore.QRect(400, 130, 221, 31))
        self.eventNameLabel_9.setStyleSheet("font-size:12pt;\n"
"background-color: rgb(255, 255, 255);")
        self.eventNameLabel_9.setObjectName("eventNameLabel_9")
        self.eventNameLabel_10 = QtWidgets.QLabel(self.frame)
        self.eventNameLabel_10.setGeometry(QtCore.QRect(310, 230, 401, 91))
        self.eventNameLabel_10.setStyleSheet("font-size:12pt;\n"
"background-color: rgb(255, 255, 255);")
        self.eventNameLabel_10.setObjectName("eventNameLabel_10")
        self.addButton = QtWidgets.QPushButton(deleteEvent)
        self.addButton.setGeometry(QtCore.QRect(330, 420, 131, 41))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(deleteEvent)
        QtCore.QMetaObject.connectSlotsByName(deleteEvent)

    def retranslateUi(self, deleteEvent):
        _translate = QtCore.QCoreApplication.translate
        deleteEvent.setWindowTitle(_translate("deleteEvent", "Dialog"))
        self.title.setText(_translate("deleteEvent", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Delete Event</span></p></body></html>"))
        self.eventNameLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.eventNameLabel_2.setText(_translate("deleteEvent", "event_name"))
        self.eventNameLabel_3.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Creator : </span></p></body></html>"))
        self.eventNameLabel_4.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Description :</span></p></body></html>"))
        self.eventNameLabel_5.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Date : </span></p></body></html>"))
        self.eventNameLabel_6.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Venue : </span></p></body></html>"))
        self.eventNameLabel_7.setText(_translate("deleteEvent", "creator"))
        self.eventNameLabel_8.setText(_translate("deleteEvent", "date"))
        self.eventNameLabel_9.setText(_translate("deleteEvent", "sdfsff"))
        self.eventNameLabel_10.setText(_translate("deleteEvent", "description"))
        self.addButton.setText(_translate("deleteEvent", "Delete"))

import img_rc
