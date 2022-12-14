#!/usr/bin/env python3

#----------------------------------------------------------------------------------------------
#                                  Table Of Contents/Overview
#----------------------------------------------------------------------------------------------
# Inventory Display
# Make All Columns Read-Only
# Search Filter
# Update Inventory
# Button Actions
# Button Functions
# Checkout Popup
# Return Popup
#----------------------------------------------------------------------------------------------

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

from ScanBarcodePopup import Ui_ScanBarcodePopup

from Constants import MainDatabase, MaxValue

class Ui_MainMenu(QMainWindow):
    def __init__(self, parent = None):
        super(Ui_MainMenu, self).__init__(parent)
        self.setObjectName("MainDisplay")
        self.setGeometry(0, 0, 1123, 903)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CheckoutButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CheckoutButton.setFont(font)
        self.CheckoutButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.CheckoutButton.setObjectName("CheckoutButton")
        self.verticalLayout.addWidget(self.CheckoutButton)
        self.ReturnButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ReturnButton.setFont(font)
        self.ReturnButton.setStyleSheet("background-color: rgb(255, 170, 32);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.ReturnButton.setObjectName("ReturnButton")
        self.verticalLayout.addWidget(self.ReturnButton)
        self.ScanBarcodeButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ScanBarcodeButton.setFont(font)
        self.ScanBarcodeButton.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.ScanBarcodeButton.setObjectName("ScanBarcodeButton")
        self.verticalLayout.addWidget(self.ScanBarcodeButton)
        self.RefreshButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RefreshButton.setFont(font)
        self.RefreshButton.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"\n"
"")
        self.RefreshButton.setObjectName("RefreshButton")
        self.verticalLayout.addWidget(self.RefreshButton)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.LogoutButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LogoutButton.setFont(font)
        self.LogoutButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.LogoutButton.setObjectName("LogoutButton")
        self.verticalLayout.addWidget(self.LogoutButton)
        self.gridLayout.addLayout(self.verticalLayout, 4, 3, 1, 1)
        self.Header = QLabel(self.centralwidget)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Header.setFont(font)
        self.Header.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.Header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Header.setObjectName("Header")
        self.gridLayout.addWidget(self.Header, 0, 1, 1, 3)
        self.SearchFilter = QComboBox(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SearchFilter.setFont(font)
        self.SearchFilter.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.SearchFilter.setObjectName("SearchFilter")
        self.gridLayout.addWidget(self.SearchFilter, 2, 1, 1, 1)
        self.SearchBar = QLineEdit(self.centralwidget)
        self.SearchBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SearchBar.setObjectName("SearchBar")
        self.gridLayout.addWidget(self.SearchBar, 2, 2, 1, 1)

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

#----------------------------------------------------------------------------------------------------
#                                       Inventory Display
#----------------------------------------------------------------------------------------------------

        #Connect to Database
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(MainDatabase)
        self.model = QSqlTableModel()
        self.delrow = -1
        self.initializeModel()

        self.sbar = self.statusBar()

        self.InventoryDisplay = QTableView()
        self.InventoryDisplay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InventoryDisplay.setModel(self.model)
        self.InventoryDisplay.clicked.connect(self.findrow)
        self.InventoryDisplay.selectionModel().selectionChanged.connect(self.getCellText)

        self.gridLayout.addWidget(self.InventoryDisplay, 4, 1, 1, 2)
        self.setCentralWidget(self.centralwidget)

        #Only selects rows (Can still edit cells by double-clicking)
        self.InventoryDisplay.setSelectionBehavior(1)
        # 0 Selecting single items.
        # 1 Selecting only rows.
        # 2 Selecting only columns.

        #----------------------------------
        #Make All Columns Un-Editable/ReadOnly
        #----------------------------------
        class ReadOnlyDelegate(QStyledItemDelegate):
                def createEditor(self, parent, option, index):
                        print('This column is Read-Only')
                        return 

        delegate = ReadOnlyDelegate(self)
        for i in range(self.model.columnCount()):
           self.InventoryDisplay.setItemDelegateForColumn(i, delegate)
        #----------------------------------

    def initializeModel(self):
       self.model.setTable('items')
       self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
       self.model.select()

        #------------------------------------------
                        #Search/Filter
        #------------------------------------------
        #Allows the user to search for items
       self.SearchFilter.clear()
       for i in range(self.model.columnCount()):
            self.SearchFilter.addItem(self.model.headerData(i, QtCore.Qt.Horizontal))
       self.SearchFilter.setCurrentIndex(1)
 
       self.SearchBar.textChanged.connect(self.filter_table)
 
    def filter_table(self, text):
        userQuery = " {} LIKE '%{}%'".format(self.SearchFilter.currentText(), text.lower()) if text else text
        self.model.setFilter(userQuery)
        self.model.select()
        #------------------------------------------
        
#----------------------------------
#       Update Inventory
#---------------------------------- 
    def findrow(self, i):
        self.delrow = i.row()

    def getCellText(self):
        if self.InventoryDisplay.selectedIndexes():
            model = self.InventoryDisplay.model()
            row = self.selectedRow()
            column = 1 #Get item name (column 1)
            name = model.data(model.index(row, column))
            #Shows the item name on the bottom left corner of the screen
            self.sbar.showMessage(str(name))
            print(name)
                        
            #Get the item Name from the currently selected row
            global SelectedItemName
            SelectedItemName = model.data(model.index(row, column))
 
    def selectedRow(self):
        if self.InventoryDisplay.selectionModel().hasSelection():
            row =  self.InventoryDisplay.selectionModel().selectedIndexes()[0].row()
            return int(row)
 
    def selectedColumn(self):
        column =  self.InventoryDisplay.selectionModel().selectedIndexes()[0].column()
        return int(column)
#----------------------------------------------------------------------------------------------------
  
    def retranslateUi(self, MainDisplay):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainDisplay", "MainMenu"))
        self.CheckoutButton.setText(_translate("MainDisplay", "Check Out"))
        self.ReturnButton.setText(_translate("MainDisplay", "Return"))
        self.ScanBarcodeButton.setText(_translate("MainDisplay", "Scan Barcode"))
        self.RefreshButton.setText(_translate("MainDisplay", "Refresh"))
        self.LogoutButton.setText(_translate("MainDisplay", "Log Out"))
        self.Header.setText(_translate("MainDisplay", "Main Menu"))

#----------------------------------------------------------------------------------------------------
#                                      Button Actions
#----------------------------------------------------------------------------------------------------
        #------------------------------------------
                        #Logout Button
        #------------------------------------------
        #When the Logout button is clicked -> LogoutClicked Function
        LogoutButton = self.LogoutButton
        LogoutButton.clicked.connect(self.LogoutClicked)
        #------------------------------------------
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
        #------------------------------------------
                     #Scan Barcode Button
        #------------------------------------------
        #When the Scan Barcode button is clicked -> ScanBarcode Function
        ScanBarcodeButton = self.ScanBarcodeButton
        ScanBarcodeButton.clicked.connect(self.ScanBarcodeClicked)
        #------------------------------------------
        #------------------------------------------
                     #Refresh Button
        #------------------------------------------
        #When the More Info button is clicked -> MoreInfo Function
        RefreshButton = self.RefreshButton
        RefreshButton.clicked.connect(self.RefreshClicked)
        #------------------------------------------

#----------------------------------
    #Logout Function
    def LogoutClicked(self):
        #Print in terminal for testing:
        print("The Logout Button was clicked")
        #Switch from this screen to the LoginScreen
        #(Import LoginScreen here to prevent circular import error)
        from LoginScreen import Ui_Loginscreen
        self.win = Ui_Loginscreen() #Define LoginScreen
        self.win.show() #Show Login Screen
        self.close() #Close this screen (AdminMenu)
#----------------------------------
#----------------------------------
    #Checkout Function
    def CheckoutClicked(self):
        #Print in terminal for testing:
        print("The Checkout Button was clicked")

        if self.InventoryDisplay.selectedIndexes():
            self.ex = Ui_CheckoutPopup(parent=self)
            self.ex.show()
        else:
            msgBox = QMessageBox.warning(None, "Error", 
                                     "No row is selected!\nPlease select a row", 
                                     QMessageBox.Close)
#----------------------------------
#----------------------------------
    #Return Function
    def ReturnClicked(self):
        #Print in terminal for testing:
        print("The Return Button was clicked")

        if self.InventoryDisplay.selectedIndexes():
            self.ex = Ui_ReturnPopup(parent=self)
            self.ex.show()  
        else:
            msgBox = QMessageBox.warning(None, "Error", 
                                     "No row is selected!\nPlease select a row", 
                                     QMessageBox.Close)
#----------------------------------
#----------------------------------
    #ScanBarcode Function
    def ScanBarcodeClicked(self):
        #Print in terminal for testing:
        print("The Scan Barcode Button was clicked")
        #Switch from this screen to the Scan Barcode Options Popup Screen (Scene Swap):
        self.win = Ui_ScanBarcodePopup()
        self.win.show()
        #self.close()
#----------------------------------
#----------------------------------
    #Refresh Function
    def RefreshClicked(self):
        #Print in terminal for testing:
        print("The Refresh Button was clicked")
        #Close and reopen the app (Refresh)
        self.win = Ui_MainMenu()
        self.win.show()
        self.close()
#----------------------------------
#----------------------------------------------------------------------------------------------------

# #Runs the Admin Menu 
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = Ui_MainMenu()
#     win.show()

#     sys.exit(app.exec_())
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
          self.messageText.setText("You are taking: "+ str(self.CheckoutSpinBox.value()) + " " + SelectedItemName)
      else:
          self.messageText.setText("You are taking: "+ str(self.CheckoutSpinBox.value()) + " " + SelectedItemName + "s")



    def ConfirmClicked(self):
      CheckoutQuantity = self.CheckoutSpinBox.value()
      print("Quantity you are taking: ", CheckoutQuantity)
      
      #Connect to the inventory database (inventory.db)
      connection = sqlite3.connect(MainDatabase)
      cursor = connection.cursor()
      #Update the quantity
      cursor.execute("UPDATE items SET Quantity = Quantity - ? WHERE Name = ?",(CheckoutQuantity, SelectedItemName,))
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


#--------------------------------------------------------------------------------------------------------------


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
          self.messageText.setText("You are returning: "+ str(self.ReturnSpinBox.value()) + " " + SelectedItemName)
      else:
          self.messageText.setText("You are returning: "+ str(self.ReturnSpinBox.value()) + " " + SelectedItemName + "s")


    def ConfirmClicked(self):
      CheckoutQuantity = self.ReturnSpinBox.value()
      print("Quantity you are returning: ", CheckoutQuantity)
      
      #Connect to the inventory database (inventory.db)
      connection = sqlite3.connect(MainDatabase)
      cursor = connection.cursor()
      #Update the quantity
      cursor.execute("UPDATE items SET Quantity = Quantity + ? WHERE Name = ?",(CheckoutQuantity, SelectedItemName,))
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
#                                       Run this Program
#----------------------------------------------------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    win = Ui_MainMenu()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
#----------------------------------------------------------------------------------------------------
