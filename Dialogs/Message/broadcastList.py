from PyQt5 import QtCore, QtGui, QtWidgets

class broadcastList(object):
    def setup(self, broadcastList):
        broadcastList.setObjectName("broadcastList")
        broadcastList.resize(636, 480)
        self.frame = QtWidgets.QFrame(broadcastList)
        self.frame.setGeometry(QtCore.QRect(10, 10, 621, 421))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.broadcastLabel = QtWidgets.QLabel(self.frame)
        self.broadcastLabel.setGeometry(QtCore.QRect(260, 0, 191, 41))
        self.broadcastLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.broadcastLabel.setObjectName("broadcastLabel")
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
        self.okButton = QtWidgets.QPushButton(broadcastList)
        self.okButton.setGeometry(QtCore.QRect(530, 440, 89, 25))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(broadcastList)
        QtCore.QMetaObject.connectSlotsByName(broadcastList)

    def retranslateUi(self, broadcastList):
        _translate = QtCore.QCoreApplication.translate
        broadcastList.setWindowTitle(_translate("broadcastList", "Broadcast List"))
        self.broadcastLabel.setText(_translate("broadcastList", "Broadcast"))
        self.okButton.setText(_translate("broadcastList", "close"))

