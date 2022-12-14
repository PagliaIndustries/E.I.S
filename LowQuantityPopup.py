from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LowQuantityAlertPopup(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_LowQuantityAlertPopup, self).__init__(parent)
        self.setObjectName("Low Quantity Alert!")
        self.resize(444, 195)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LowQuantityAlertHeader = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.LowQuantityAlertHeader.setFont(font)
        self.LowQuantityAlertHeader.setStyleSheet("color: rgb(170, 0, 0);")
        self.LowQuantityAlertHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.LowQuantityAlertHeader.setObjectName("LowQuantityAlertHeader")
        self.verticalLayout.addWidget(self.LowQuantityAlertHeader)
        self.ItemsWithLowQuantityAmountLable = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ItemsWithLowQuantityAmountLable.setFont(font)
        self.ItemsWithLowQuantityAmountLable.setAlignment(QtCore.Qt.AlignCenter)
        self.ItemsWithLowQuantityAmountLable.setObjectName("ItemsWithLowQuantityAmountLable")
        self.verticalLayout.addWidget(self.ItemsWithLowQuantityAmountLable)
        self.TextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.TextBrowser.setObjectName("TextBrowser")
        self.verticalLayout.addWidget(self.TextBrowser)
        self.AcknowledgeButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AcknowledgeButton.setFont(font)
        self.AcknowledgeButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.AcknowledgeButton.setObjectName("AcknowledgeButton")
        self.verticalLayout.addWidget(self.AcknowledgeButton)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Low Quantity Alert!"))
        self.LowQuantityAlertHeader.setText(_translate("MainWindow", "Low Quantity Alert!"))
        self.ItemsWithLowQuantityAmountLable.setText(_translate("MainWindow", "()Items Have Low Quantity!"))
        self.TextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.AcknowledgeButton.setText(_translate("MainWindow", "Acknowledge"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_LowQuantityAlertPopup()
    win.show()
    sys.exit(app.exec_())
