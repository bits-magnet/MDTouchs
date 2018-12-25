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
        self.widget.setGeometry(QtCore.QRect(10, 70, 271, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/sample_event.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(7, 7, 7);")
        self.widget.setObjectName("widget")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(30, 10, 91, 31))
        self.nameLabel.setObjectName("nameLabel")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(120, 10, 561, 31))
        self.name.setStyleSheet("font-size:16pt;")
        self.name.setObjectName("name")
        self.creatorLabel = QtWidgets.QLabel(self.frame)
        self.creatorLabel.setGeometry(QtCore.QRect(10, 290, 101, 31))
        self.creatorLabel.setObjectName("creatorLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.frame)
        self.descriptionLabel.setGeometry(QtCore.QRect(310, 190, 131, 41))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.dateLabel = QtWidgets.QLabel(self.frame)
        self.dateLabel.setGeometry(QtCore.QRect(310, 70, 71, 31))
        self.dateLabel.setObjectName("dateLabel")
        self.venueLabel = QtWidgets.QLabel(self.frame)
        self.venueLabel.setGeometry(QtCore.QRect(310, 130, 81, 31))
        self.venueLabel.setObjectName("venueLabel")
        self.creator = QtWidgets.QLabel(self.frame)
        self.creator.setGeometry(QtCore.QRect(120, 290, 181, 31))
        self.creator.setStyleSheet("font-size:12pt;")
        self.creator.setObjectName("creator")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(400, 70, 221, 31))
        self.date.setStyleSheet("font-size:12pt;")
        self.date.setObjectName("date")
        self.venue = QtWidgets.QLabel(self.frame)
        self.venue.setGeometry(QtCore.QRect(400, 130, 221, 31))
        self.venue.setStyleSheet("font-size:12pt;")
        self.venue.setObjectName("venue")
        self.description = QtWidgets.QLabel(self.frame)
        self.description.setGeometry(QtCore.QRect(310, 230, 401, 91))
        self.description.setStyleSheet("font-size:12pt;")
        self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description.setObjectName("description")
        self.deleteButton = QtWidgets.QPushButton(deleteEvent)
        self.deleteButton.setGeometry(QtCore.QRect(330, 420, 131, 41))
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(deleteEvent)
        QtCore.QMetaObject.connectSlotsByName(deleteEvent)

    def retranslateUi(self, deleteEvent):
        _translate = QtCore.QCoreApplication.translate
        deleteEvent.setWindowTitle(_translate("deleteEvent", "Dialog"))
        self.title.setText(_translate("deleteEvent", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Delete Event</span></p></body></html>"))
        self.nameLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.name.setText(_translate("deleteEvent", "event_name"))
        self.creatorLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Creator : </span></p></body></html>"))
        self.descriptionLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Description :</span></p></body></html>"))
        self.dateLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Date : </span></p></body></html>"))
        self.venueLabel.setText(_translate("deleteEvent", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Venue : </span></p></body></html>"))
        self.creator.setText(_translate("deleteEvent", "creator"))
        self.date.setText(_translate("deleteEvent", "date"))
        self.venue.setText(_translate("deleteEvent", "venue"))
        self.description.setText(_translate("deleteEvent", "description"))
        self.deleteButton.setText(_translate("deleteEvent", "Delete"))

import img_rc
