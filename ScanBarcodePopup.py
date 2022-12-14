import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMainWindow, 
                                QLabel, QLineEdit, QTableWidget, QTableWidgetItem, 
                                QGridLayout, QVBoxLayout, QSizePolicy, QSpacerItem, 
                                QMessageBox,QSpinBox, QComboBox, QTableView,QStyledItemDelegate)
from PyQt5.QtCore import Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont

import sqlite3

from Constants import MainDatabase, MaxValue


class Ui_ScanBarcodePopup(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_ScanBarcodePopup, self).__init__(parent)
        self.setFixedSize(428, 188)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ScanBarcodeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ScanBarcodeLabel.setFont(font)
        self.ScanBarcodeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ScanBarcodeLabel.setObjectName("ScanBarcodeLabel")
        self.verticalLayout.addWidget(self.ScanBarcodeLabel)
        self.BarcodeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.BarcodeInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BarcodeInput.setObjectName("BarcodeInput")
        self.verticalLayout.addWidget(self.BarcodeInput)
        self.ButtonFrame = QtWidgets.QFrame(self.centralwidget)
        self.ButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonFrame.setObjectName("ButtonFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CheckoutButton = QtWidgets.QPushButton(self.ButtonFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CheckoutButton.setFont(font)
        self.CheckoutButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.CheckoutButton.setObjectName("CheckoutButton")
        self.horizontalLayout.addWidget(self.CheckoutButton)
        self.ReturnButton = QtWidgets.QPushButton(self.ButtonFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ReturnButton.setFont(font)
        self.ReturnButton.setStyleSheet("background-color: rgb(255, 170, 32);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.ReturnButton.setObjectName("ReturnButton")
        self.horizontalLayout.addWidget(self.ReturnButton)
        self.verticalLayout.addWidget(self.ButtonFrame)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

#----------------------------------------------------------------------------------------------------
#                                      Button Actions
#----------------------------------------------------------------------------------------------------
        #------------------------------------------
                     #Checkout Item Button
        #------------------------------------------
        #When the Checkout button is clicked -> Checkout Function
        CheckoutButton = self.CheckoutButton
        CheckoutButton.clicked.connect(self.CheckoutClicked)
        #------------------------------------------
        #------------------------------------------
                     #Return Item Button
        #------------------------------------------
        #When the Return button is clicked -> Return Function
        ReturnButton = self.ReturnButton
        ReturnButton.clicked.connect(self.ReturnClicked)
        #------------------------------------------

#----------------------------------
#       Checkout Function
#----------------------------------
    def CheckoutClicked(self):
        #Print in terminal for testing:
        print("The Checkout Button was clicked")

        #------------------------------------------
        #  Barcode Input Text & Selected Item Name
        #------------------------------------------
        global BarcodeInput
        BarcodeInput = self.BarcodeInput.text()

        #Connect to the inventory database (inventory.db)
        connection = sqlite3.connect(MainDatabase)
        cursor = connection.cursor()
        #Select Main_Category
        cursor.execute("SELECT Name FROM items WHERE Barcode = ?",(BarcodeInput,))
        connection.commit()
        Result = cursor.fetchone()
        #Close the connection
        connection.close()

        ItemName = ''.join(Result)
        print('Selected Item Name: ',ItemName)
        global SelectedItemName
        SelectedItemName = ItemName
        #------------------------------------------

        if self.BarcodeInput.text() is None:
            msgBox = QMessageBox.warning(None, "Error", 
                            "Nothing was entered!\nPlease ensure scanner is connected", 
                            QMessageBox.Close)
        else:
            #Connect to the inventory database (inventory.db)
            connection = sqlite3.connect(MainDatabase)
            cursor = connection.cursor()
            #Select Main_Category
            cursor.execute("SELECT Main_Category FROM items WHERE Barcode = ?",(BarcodeInput,))
            connection.commit()
            Result = cursor.fetchone()
            #Close the connection
            connection.close()

            if Result == ('Wire',):
                print('The item is wire')
                #Go to Wire Checkout Popup
                self.ex = Ui_WireCheckoutPopup(parent=self)
                self.ex.show()
                self.close()

            else:
                self.ex = Ui_CheckoutPopup(parent=self)
                self.ex.show()
                self.close()

#----------------------------------

#----------------------------------
#       Return Function
#----------------------------------
    def ReturnClicked(self):
        #Print in terminal for testing:
        print("The Return Button was clicked")

        #------------------------------------------
        #  Barcode Input Text & Selected Item Name
        #------------------------------------------
        global BarcodeInput
        BarcodeInput = self.BarcodeInput.text()

        #Connect to the inventory database (inventory.db)
        connection = sqlite3.connect(MainDatabase)
        cursor = connection.cursor()
        #Select Main_Category
        cursor.execute("SELECT Name FROM items WHERE Barcode = ?",(BarcodeInput,))
        connection.commit()
        Result = cursor.fetchone()
        #Close the connection
        connection.close()

        ItemName = ''.join(Result)
        print('Selected Item Name: ', ItemName)
        global SelectedItemName
        SelectedItemName = ItemName
        #------------------------------------------

        if self.BarcodeInput.text() is None:
            msgBox = QMessageBox.warning(None, "Error", 
                            "Nothing was entered!\nPlease ensure scanner is connected", 
                            QMessageBox.Close)
        else:
            #Connect to the inventory database (inventory.db)
            connection = sqlite3.connect(MainDatabase)
            cursor = connection.cursor()
            #Select Main_Category
            cursor.execute("SELECT Main_Category FROM items WHERE Barcode = ?",(BarcodeInput,))
            connection.commit()
            Result = cursor.fetchone()
            #Close the connection
            connection.close()

            if Result == ('Wire',):
                print('The item is wire')
                #Go to Wire Checkout Popup
                self.ex = Ui_WireReturnPopup(parent=self)
                self.ex.show()
                self.close()

            else:
                self.ex = Ui_ReturnPopup(parent=self)
                self.ex.show()
                self.close()
#----------------------------------
#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------
#                                      Retranslate Ui
#----------------------------------------------------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Scan Barcode"))
        self.ScanBarcodeLabel.setText(_translate("MainWindow", "Scan/Enter Barcode Here:"))
        self.CheckoutButton.setText(_translate("MainWindow", "Checkout"))
        self.ReturnButton.setText(_translate("MainWindow", "Return"))
#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------
#                                      Checkout Popup
#----------------------------------------------------------------------------------------------------
class Ui_CheckoutPopup(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_CheckoutPopup, self).__init__(parent)

        self.setObjectName("Checkout Item")
        self.setFixedSize(600, 188)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.messageText.setFont(font)
        self.messageText.setAlignment(QtCore.Qt.AlignCenter)
        self.messageText.setObjectName("messageText")
        self.verticalLayout.addWidget(self.messageText)
        self.CheckoutSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CheckoutSpinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CheckoutSpinBox.setObjectName("CheckoutSpinBox")
        self.verticalLayout.addWidget(self.CheckoutSpinBox)
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.verticalLayout.addWidget(self.ConfirmButton)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

#--------------------------------------------------
        self.CheckoutSpinBox.valueChanged.connect(self.currentValue)

        #------------------------------------------
                    #Confim Button
        #------------------------------------------
        #When the Confirm button is clicked -> Confirm Function
        ConfirmButton = self.ConfirmButton
        ConfirmButton.clicked.connect(self.ConfirmClicked)
        #------------------------------------------
        #------------------------------------------

    def currentValue(self):
      #Get the selected item's name from the global variable SelectedItemName in getCellText()
      #Show the current value of the SpinBox in real time
      if self.CheckoutSpinBox.value() <= 1:
          self.messageText.setText("You are taking: "+ "(" + str(self.CheckoutSpinBox.value()) + ")" + " " + SelectedItemName)
      else:
          self.messageText.setText("You are taking: "+ "(" + str(self.CheckoutSpinBox.value()) + ")" + " " + SelectedItemName + "s")



    def ConfirmClicked(self):
      CheckoutQuantity = self.CheckoutSpinBox.value()
      print("Quantity you are taking: ", CheckoutQuantity)
      
      #Connect to the inventory database (inventory.db)
      connection = sqlite3.connect(MainDatabase)
      cursor = connection.cursor()
      #Update the quantity
      cursor.execute("UPDATE items SET Quantity = Quantity - ? WHERE Barcode = ?",(CheckoutQuantity, BarcodeInput,))
      connection.commit()
      #Close the connection
      connection.close()

      #Close the window
      self.parent()
      self.close()
#--------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Checkout Item"))
        self.messageText.setText(_translate("MainWindow", "How much quantity are you taking:"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm"))

#----------------------------------------------------------------------------------------------------
#                           Max Value for Price, Quantity & Length SpinBox
#----------------------------------------------------------------------------------------------------
        self.CheckoutSpinBox.setMaximum(MaxValue)
#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------
#                                      Return Popup
#----------------------------------------------------------------------------------------------------
class Ui_ReturnPopup(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_ReturnPopup, self).__init__(parent)

        self.setObjectName("Return Item")
        self.setFixedSize(600, 188)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.messageText.setFont(font)
        self.messageText.setAlignment(QtCore.Qt.AlignCenter)
        self.messageText.setObjectName("messageText")
        self.verticalLayout.addWidget(self.messageText)
        self.ReturnSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ReturnSpinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ReturnSpinBox.setObjectName("CheckoutSpinBox")
        self.verticalLayout.addWidget(self.ReturnSpinBox)
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.verticalLayout.addWidget(self.ConfirmButton)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

#--------------------------------------------------
        self.ReturnSpinBox.valueChanged.connect(self.currentValue)

        #------------------------------------------
                    #Confim Button
        #------------------------------------------
        #When the Confirm button is clicked -> Confirm Function
        ConfirmButton = self.ConfirmButton
        ConfirmButton.clicked.connect(self.ConfirmClicked)
        #------------------------------------------
        #------------------------------------------

    def currentValue(self):
      #Get the selected item's name from the global variable SelectedItemName in getCellText()
      #Show the current value of the SpinBox in real time
      if self.ReturnSpinBox.value() <= 1:
          self.messageText.setText("You are returning: "+ "(" + str(self.ReturnSpinBox.value()) + ")" + " " + SelectedItemName)
      else:
          self.messageText.setText("You are returning: "+ "(" + str(self.ReturnSpinBox.value()) + ")" + " " + SelectedItemName + "s")


    def ConfirmClicked(self):
      CheckoutQuantity = self.ReturnSpinBox.value()
      print("Quantity you are returning: ", CheckoutQuantity)
      
      #Connect to the inventory database (inventory.db)
      connection = sqlite3.connect(MainDatabase)
      cursor = connection.cursor()
      #Update the quantity
      cursor.execute("UPDATE items SET Quantity = Quantity + ? WHERE Barcode = ?",(CheckoutQuantity, BarcodeInput,))
      connection.commit()
      #Close the connection
      connection.close()

      #Close the window
      self.parent()
      self.close()
#--------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Return Item"))
        self.messageText.setText(_translate("MainWindow", "How much quantity are you returning:"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm"))

#----------------------------------------------------------------------------------------------------
#                           Max Value for Price, Quantity & Length SpinBox
#----------------------------------------------------------------------------------------------------
        self.ReturnSpinBox.setMaximum(MaxValue)
#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------
#                                    Wire Checkout Popup
#----------------------------------------------------------------------------------------------------
class Ui_WireCheckoutPopup(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_WireCheckoutPopup, self).__init__(parent)

        self.setObjectName("Checkout Wire")
        self.setFixedSize(600, 188)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.messageText.setFont(font)
        self.messageText.setAlignment(QtCore.Qt.AlignCenter)
        self.messageText.setObjectName("messageText")
        self.verticalLayout.addWidget(self.messageText)
        self.CheckoutSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CheckoutSpinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CheckoutSpinBox.setObjectName("CheckoutSpinBox")
        self.verticalLayout.addWidget(self.CheckoutSpinBox)
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.verticalLayout.addWidget(self.ConfirmButton)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

#--------------------------------------------------
        self.CheckoutSpinBox.valueChanged.connect(self.currentValue)

        #------------------------------------------
                    #Confim Button
        #------------------------------------------
        #When the Confirm button is clicked -> Confirm Function
        ConfirmButton = self.ConfirmButton
        ConfirmButton.clicked.connect(self.ConfirmClicked)
        #------------------------------------------
        #------------------------------------------

    def currentValue(self):
      #Get the selected item's name from the global variable SelectedItemName in getCellText()
      #Show the current value of the SpinBox in real time
      if self.CheckoutSpinBox.value() > 0:
          self.messageText.setText("You are taking: "+ "(" + str(self.CheckoutSpinBox.value()) + ")Ft" + " of " + SelectedItemName)


    def ConfirmClicked(self):
      CheckoutQuantity = self.CheckoutSpinBox.value()
      print("Length(Ft) you are taking: ", CheckoutQuantity)
      
      #Connect to the inventory database (inventory.db)
      connection = sqlite3.connect(MainDatabase)
      cursor = connection.cursor()
      #Update the Total_Length_Ft for the wire in Inventory
      cursor.execute("UPDATE items SET Total_Length_Ft = Total_Length_Ft - ? WHERE Barcode = ?",(CheckoutQuantity, BarcodeInput,))
      connection.commit()
      #Close the connection
      connection.close()

      #Close the window
      self.parent()
      self.close()
#--------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Checkout Item"))
        self.messageText.setText(_translate("MainWindow", "How many Ft are you taking:"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm"))

#----------------------------------------------------------------------------------------------------
#                           Max Value for Price, Quantity & Length SpinBox
#----------------------------------------------------------------------------------------------------
        self.CheckoutSpinBox.setMaximum(MaxValue)
#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------
#                                    Wire Return Popup
#----------------------------------------------------------------------------------------------------
class Ui_WireReturnPopup(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_WireReturnPopup, self).__init__(parent)

        self.setObjectName("Return Wire")
        self.setFixedSize(600, 188)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageText = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.messageText.setFont(font)
        self.messageText.setAlignment(QtCore.Qt.AlignCenter)
        self.messageText.setObjectName("messageText")
        self.verticalLayout.addWidget(self.messageText)
        self.CheckoutSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.CheckoutSpinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CheckoutSpinBox.setObjectName("CheckoutSpinBox")
        self.verticalLayout.addWidget(self.CheckoutSpinBox)
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.verticalLayout.addWidget(self.ConfirmButton)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

#--------------------------------------------------
        self.CheckoutSpinBox.valueChanged.connect(self.currentValue)

        #------------------------------------------
                    #Confim Button
        #------------------------------------------
        #When the Confirm button is clicked -> Confirm Function
        ConfirmButton = self.ConfirmButton
        ConfirmButton.clicked.connect(self.ConfirmClicked)
        #------------------------------------------
        #------------------------------------------

    def currentValue(self):
      #Get the selected item's name from the global variable SelectedItemName in getCellText()
      #Show the current value of the SpinBox in real time
      if self.CheckoutSpinBox.value() > 0:
          self.messageText.setText("You are returning: "+ "(" + str(self.CheckoutSpinBox.value()) + ")Ft" + " of " + SelectedItemName)


    def ConfirmClicked(self):
      CheckoutQuantity = self.CheckoutSpinBox.value()
      print("Length(Ft) you are returning: ", CheckoutQuantity)
      
      #Connect to the inventory database (inventory.db)
      connection = sqlite3.connect(MainDatabase)
      cursor = connection.cursor()
      #Update the Total_Length_Ft for the wire in Inventory
      cursor.execute("UPDATE items SET Total_Length_Ft = Total_Length_Ft + ? WHERE Barcode = ?",(CheckoutQuantity, BarcodeInput,))
      connection.commit()
      #Close the connection
      connection.close()

      #Close the window
      self.parent()
      self.close()
#--------------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Checkout Item"))
        self.messageText.setText(_translate("MainWindow", "How many Ft are you returning:"))
        self.ConfirmButton.setText(_translate("MainWindow", "Confirm"))

#----------------------------------------------------------------------------------------------------
#                           Max Value for Price, Quantity & Length SpinBox
#----------------------------------------------------------------------------------------------------
        self.CheckoutSpinBox.setMaximum(MaxValue)
#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------
#                                       Run this Program
#----------------------------------------------------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    win = Ui_ScanBarcodePopup()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
#----------------------------------------------------------------------------------------------------

