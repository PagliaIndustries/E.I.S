#!/usr/bin/env python3

#-----------------------------------------------
#Electronic Inventory System (EIS)
#Version 3 
#Last Updated: 08/08/22
#Developed by Paglia Industries
#Total Time Spent: 75 hours
#-----------------------------------------------

#----------------------------------------------------------------------------------------------
#                                  Table Of Contents/Overview
#----------------------------------------------------------------------------------------------
# Inventory Display
# Search Filter
# Sort Columns A->Z 
# Update Inventory
# Auto Sell Price Update
# Auto Price/Ft Update
# Make Certain Columns Read-Only
# Calculate Total Inventory Value With & Without Markup
# Low Quantity Alert
# Retranslate Ui
# Button Actions
# Button Functions
# Checkout Popup
# Return Popup
# Wire Checkout Popup
# Wire Return Popup
# Low Quantity Popup
# Settings Screen
# Run the Program
#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------
#                                           TODO
#----------------------------------------------------------------------------------------------
# (1)
# Make Tutorial(PDF) 
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

from AddItemScreen import Ui_AddItemMenu
from AddWireScreen import Ui_AddWireMenu
from ScanBarcodePopup import Ui_ScanBarcodePopup

from Constants import MainDatabase, MaxValue, UserDatabase


class Ui_MainDisplay(QMainWindow):
    def __init__(self, parent = None):
        super(Ui_MainDisplay, self).__init__(parent)
        self.setObjectName("MainDisplay")
        self.resize(1123, 903)
        self.showMaximized()
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AddItemButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AddItemButton.setFont(font)
        self.AddItemButton.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"\n"
"")
        self.AddItemButton.setObjectName("AddItemButton")
        self.verticalLayout.addWidget(self.AddItemButton)
        self.DeleteItemButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteItemButton.setFont(font)
        self.DeleteItemButton.setStyleSheet("background-color: rgb(255, 65, 68);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.DeleteItemButton.setObjectName("DeleteItemButton")
        self.verticalLayout.addWidget(self.DeleteItemButton)
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
        self.SettingsButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SettingsButton.setFont(font)
        self.SettingsButton.setStyleSheet("background-color: rgb(196, 17, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.SettingsButton.setObjectName("SettingsButton")
        self.verticalLayout.addWidget(self.SettingsButton)
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

        #Sort Columns From A->Z When Their Headers are Clicked
        self.InventoryDisplay.horizontalHeader().sectionClicked.connect(self.header_clicked)

        #Call the Low Quanity Alert function
        self.LowQuantityAlert()

        #Call the function to calculate the SellPrice
        self.calculate_sellprice()
    
        #Call the function to calculate the Price/Ft of Wire
        self.calculate_PricePerFt()
        
        #Call the functions to calculate the total inventory values
        self.calculate_TotalValue_NoMarkup()
        self.calculate_TotalValue_Markup()

    def initializeModel(self):
       self.model.setTable('items')#Table name for database
       self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
       self.model.select()

    #------------------------------------------
    #               Search/Filter
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

    #------------------------------------------
    #      Sort Columns by A->Z
    #------------------------------------------
    def header_clicked(self, index):
        self.InventoryDisplay.sortByColumn(index, Qt.AscendingOrder)
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
#----------------------------------
    #------------------------------------------------------------------------
    #When Price is Updated, Automatically Update SellPrice When Refresh is Hit
    #------------------------------------------------------------------------
    def calculate_sellprice(self):
        for row in range(self.InventoryDisplay.model().rowCount()):
                sell_price = float(self.InventoryDisplay.model().index(row, 3).data())

                if sell_price < 50:
                    Markup = 1.50

                elif sell_price < 150:
                    Markup = 1.45

                elif sell_price <= 1000:
                    Markup = 1.35

                elif sell_price < 2000:
                    Markup = 1.30

                elif sell_price < 3000:
                    Markup = 1.20

                elif sell_price < 4000:
                    Markup = 1.15

                else:
                    Markup = 1.10
                
                #Calculation: Price*Markup
                sell_price = f'{sell_price * Markup:.2f}'
                self.InventoryDisplay.model().setData(self.InventoryDisplay.model().index(row, 4), sell_price)
    
        #Calculate Wire Sell Price
        for row in range(self.InventoryDisplay.model().rowCount()):
                sell_price = float(self.InventoryDisplay.model().index(row, 10).data())

                if sell_price < 50:
                    Markup = 1.50

                elif sell_price < 150:
                    Markup = 1.45

                elif sell_price <= 1000:
                    Markup = 1.35

                elif sell_price < 2000:
                    Markup = 1.30

                elif sell_price < 3000:
                    Markup = 1.20

                elif sell_price < 4000:
                    Markup = 1.15

                else:
                    Markup = 1.10
                
                #Calculation: Price*Markup
                sell_price = f'{sell_price * Markup:.2f}'
                self.InventoryDisplay.model().setData(self.InventoryDisplay.model().index(row, 11), sell_price)

        #----------------------------------
        #Make Specific Columns Un-Editable/ReadOnly
        #----------------------------------
        class ReadOnlyDelegate(QStyledItemDelegate):
                def createEditor(self, parent, option, index):
                        print('This column is Read-Only')
                        return 

        delegate = ReadOnlyDelegate(self)
        self.InventoryDisplay.setItemDelegateForColumn(0, delegate) #ID
        self.InventoryDisplay.setItemDelegateForColumn(2, delegate) #Quantity
        self.InventoryDisplay.setItemDelegateForColumn(4, delegate) #SellPrice
        self.InventoryDisplay.setItemDelegateForColumn(6, delegate) #Main Category
        self.InventoryDisplay.setItemDelegateForColumn(7, delegate) #Subcategory
        self.InventoryDisplay.setItemDelegateForColumn(9, delegate) #Spool_Length_Ft
        self.InventoryDisplay.setItemDelegateForColumn(11, delegate) #Spool_Sell_Price_$
        self.InventoryDisplay.setItemDelegateForColumn(12, delegate) #Price/Ft
        self.InventoryDisplay.setItemDelegateForColumn(13, delegate) #Total_Length_Ft
        self.InventoryDisplay.setItemDelegateForColumn(15, delegate) #Date Added
        #----------------------------------

    #------------------------------------------------------------------------
    #When Price is Updated, Automatically Update Price/Ft When Refresh is Hit
    #------------------------------------------------------------------------
    def calculate_PricePerFt(self):
        for row in range(self.InventoryDisplay.model().rowCount()):
                sell_price = float(self.InventoryDisplay.model().index(row, 11).data())
                length = float(self.InventoryDisplay.model().index(row, 9).data())
                
                #Calculation: Sell_Price/Length with ZeroDivisionError Handler
                sell_price = f'{sell_price / length:.2f}' if length !=0 else 0
                self.InventoryDisplay.model().setData(self.InventoryDisplay.model().index(row, 12), sell_price)
    #------------------------------------------------------------------------

    #------------------------------------------------------------------------
    #  Calculate The Total Inventory Value Without Markup (Quantity*Price)
    #------------------------------------------------------------------------
    def calculate_TotalValue_NoMarkup(self):
        global totalPriceNoMarkup
        totalPrice = 0.0
        totalWirePrice = 0.0
        for row in range(self.InventoryDisplay.model().rowCount()):
            QuantityValue = float(self.InventoryDisplay.model().index(row, 2).data())
            PriceValue = float(self.InventoryDisplay.model().index(row, 3).data())
            QuanityPriceValue = QuantityValue*PriceValue

            totalPrice += QuanityPriceValue

        #Calculate Total Value for Wire Without Markup (PricePerftNoMarkup*TotalLength)
        for row in range(self.InventoryDisplay.model().rowCount()):
            SpoolLength = float(self.InventoryDisplay.model().index(row, 9).data())
            SpoolPrice = float(self.InventoryDisplay.model().index(row, 10).data())
            Price_Per_Ft_NoMarkup = f'{SpoolPrice/SpoolLength:.2f}' if SpoolLength !=0 else 0

            TotalLength = float(self.InventoryDisplay.model().index(row, 13).data())
            TotalWireValue =  f'{float(Price_Per_Ft_NoMarkup)*TotalLength:.2f}'
            totalWirePrice += float(TotalWireValue)

        totalPriceNoMarkup = str(totalPrice + totalWirePrice)
        print('Total value of all items (No Markup): $', totalPriceNoMarkup)
            
    #----------------------------------

    #------------------------------------------------------------------------
    #  Calculate The Total Inventory Value With Markup (Quantity*SellPrice)
    #------------------------------------------------------------------------
    def calculate_TotalValue_Markup(self):
        global totalPriceMarkup
        totalPrice = 0.0
        totalWirePrice = 0.0
        for row in range(self.InventoryDisplay.model().rowCount()):
            #Calculate Items with Wire
            QuantityValue = float(self.InventoryDisplay.model().index(row, 2).data())
            SellPriceValue = float(self.InventoryDisplay.model().index(row, 4).data())
            QuanityPriceValue = QuantityValue*SellPriceValue

            totalPrice += QuanityPriceValue
       
        #Calculate Total Value for Wire Without Markup (PricePerft*TotalLength)
        for row in range(self.InventoryDisplay.model().rowCount()):
            Price_Per_Ft = float(self.InventoryDisplay.model().index(row, 12).data())
            TotalLength = float(self.InventoryDisplay.model().index(row, 13).data())

            TotalWireValue =  f'{Price_Per_Ft*TotalLength:.2f}'
            totalWirePrice += float(TotalWireValue)

        totalPriceMarkup = str(totalPrice + totalWirePrice)
        print('Total value of all items (With Markup): $', totalPriceMarkup)
    #----------------------------------

#------------------------------------------------------------------------
#                     Low Quantity Alert
#------------------------------------------------------------------------
    def LowQuantityAlert(self):
        #Connect to the Inventory database
        connection = sqlite3.connect(MainDatabase)
        cursor = connection.cursor()

        #Get the item name, Total_Length, & subcategory if it's wire & less than the low quantity value
        cursor.execute('''
            SELECT I.Name as CURRENT
            from Categories as C, Items as I
            WHERE C.Subcategory = I.Subcategory 
            AND I.Main_Category = 'Wire'
            AND I.Total_Length_Ft < C.Low_Quantity_Value
            ''')
        connection.commit()
        #Return the items with low quantity values
        WireResult = cursor.fetchall()

        #Get the item name, quantity, & subcategory if it's not wire & less than the low quantity value
        cursor.execute('''
            SELECT I.Name as CURRENT
            from Categories as C, Items as I
            WHERE C.Subcategory = I.Subcategory
            AND I.Main_Category != 'Wire'
            AND I.Quantity < C.Low_Quantity_Value
            ''')
        connection.commit()
        #Return the items with low quantity values
        ItemResult = cursor.fetchall()

        #Close the connection
        connection.close()

        #Convert Results from Tuple to List
        from itertools import chain
        LowQuantityItemsList = list(chain.from_iterable(ItemResult))
        print("StringLowQuantityItems:", LowQuantityItemsList)
        #Then Convert the List to a String
        global LowQuantityItems
        LowQuantityItems = ", ".join(str(x) for x in LowQuantityItemsList)

        #Convert Wire Results from Tuple to List
        from itertools import chain
        LowQuantityWireList = list(chain.from_iterable(WireResult))
        print("StringLowQuantityWire:", LowQuantityWireList)
        #Then Convert the List to a String
        global LowQuantityWire
        LowQuantityWire = ", ".join(str(x) for x in LowQuantityWireList)

        #If Result return an empty list Quanity is good, else call popup
        if ItemResult == [] and WireResult == []:
            print("Quantity All Good")  
        else:
            self.ex = Ui_LowQuantityAlertPopup(parent=self)
            self.ex.show()
#----------------------------------
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#                                      Retranslate Ui
#----------------------------------------------------------------------------------------------------
    def retranslateUi(self, MainDisplay):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainDisplay", "AdminMenu"))
        self.AddItemButton.setText(_translate("MainDisplay", "Add New Item"))
        self.DeleteItemButton.setText(_translate("MainDisplay", "Delete Item"))
        self.CheckoutButton.setText(_translate("MainDisplay", "Check Out"))
        self.ReturnButton.setText(_translate("MainDisplay", "Return"))
        self.ScanBarcodeButton.setText(_translate("MainDisplay", "Scan Barcode"))
        self.SettingsButton.setText(_translate("MainDisplay", "Settings"))
        self.RefreshButton.setText(_translate("MainDisplay", "Refresh"))
        self.LogoutButton.setText(_translate("MainDisplay", "Log Out"))
        self.Header.setText(_translate("MainDisplay", "Admin Menu"))

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
                        #Add Item Button
        #------------------------------------------
        #When the AddItem button is clicked -> AddItem Function
        AddItemButton = self.AddItemButton
        AddItemButton.clicked.connect(self.AddItemClicked)
        #------------------------------------------
        #------------------------------------------
                     #Remove Item Button
        #------------------------------------------
        #When the RemoveItem button is clicked -> RemoveItem Function
        RemoveItemButton = self.DeleteItemButton
        RemoveItemButton.clicked.connect(self.RemoveItemClicked)
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
                     #Settings Button
        #------------------------------------------
        #When the Settings button is clicked -> Settings Function
        SettingsButton = self.SettingsButton
        SettingsButton.clicked.connect(self.SettingsClicked)
        #------------------------------------------
        #------------------------------------------
                     #Refresh Button
        #------------------------------------------
        #When the More Info button is clicked -> MoreInfo Function
        RefreshButton = self.RefreshButton
        RefreshButton.clicked.connect(self.RefreshClicked)
        #------------------------------------------

#----------------------------------
#       Logout Function
#----------------------------------
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
#      Add Item Function
#----------------------------------
    def AddItemClicked(self):
        #Print in terminal for testing:
        print("The Add Item Button was clicked")
        self.IsItWirePopup()

    #----------------------------------
    #      Is it wire Popup
    #----------------------------------
    def IsItWirePopup(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Is the Item you are adding wire?")
        msgBox.setWindowTitle("Is it Wire?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            #Switch from this screen to the AddWire Screen (Scene Swap):
            self.win = Ui_AddWireMenu()
            self.win.show()
            #self.close()
        else:
            #Switch from this screen to the AddItems Screen (Scene Swap):
            self.win = Ui_AddItemMenu()
            self.win.show()
            #self.close()
#----------------------------------

#----------------------------------
#      Remove Item Function
#----------------------------------
    def RemoveItemClicked(self):
        #Print in terminal for testing:
        print("The Delete Item Button was clicked")

        if self.InventoryDisplay.selectedIndexes():
            self.DeleteConfirmation()
        else:
            msgBox = QMessageBox.warning(None, "Error", 
                                     "No row is selected!\nPlease select a row", 
                                     QMessageBox.Close)
    #----------------------------------
    #   Delete Item Confirmation
    #----------------------------------
    def DeleteConfirmation(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Are you sure you want to delete this item?")
        msgBox.setInformativeText("*This cannot be undone")
        msgBox.setWindowTitle("Delete Item Confirmation")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
  
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
                row = self.InventoryDisplay.currentIndex().row()
                self.model.removeRow(row)
                self.initializeModel()
                self.InventoryDisplay.selectRow(row)
#----------------------------------

#----------------------------------
#       Checkout Function
#----------------------------------
    def CheckoutClicked(self):
        #Print in terminal for testing:
        print("The Checkout Button was clicked")

        if self.InventoryDisplay.selectedIndexes():
            #Connect to the inventory database (inventory.db)
            connection = sqlite3.connect(MainDatabase)
            cursor = connection.cursor()
            #Select Main_Category
            cursor.execute("SELECT Main_Category FROM items WHERE Name = ?",(SelectedItemName,))
            connection.commit()
            Result = cursor.fetchone()
            #Close the connection
            connection.close()

            if Result == ('Wire',):
                print('The item is wire')
                #Go to Wire Checkout Popup
                self.ex = Ui_WireCheckoutPopup(parent=self)
                self.ex.show()

            else:
                self.ex = Ui_CheckoutPopup(parent=self)
                self.ex.show()
        else:
            msgBox = QMessageBox.warning(None, "Error", 
                                     "No row is selected!\nPlease select a row", 
                                     QMessageBox.Close)
#----------------------------------

#----------------------------------
#       Return Function
#----------------------------------
    def ReturnClicked(self):
        #Print in terminal for testing:
        print("The Return Button was clicked")

        if self.InventoryDisplay.selectedIndexes():
            #Connect to the inventory database (inventory.db)
            connection = sqlite3.connect(MainDatabase)
            cursor = connection.cursor()
            #Select Main_Category
            cursor.execute("SELECT Main_Category FROM items WHERE Name = ?",(SelectedItemName,))
            connection.commit()
            Result = cursor.fetchone()
            #Close the connection
            connection.close()

            if Result == ('Wire',):
                print('The item is wire')
                #Go to Wire Return Popup
                self.ex = Ui_WireReturnPopup(parent=self)
                self.ex.show()

            else:
                self.ex = Ui_ReturnPopup(parent=self)
                self.ex.show()  
        else:
            msgBox = QMessageBox.warning(None, "Error", 
                                     "No row is selected!\nPlease select a row", 
                                     QMessageBox.Close)
#----------------------------------

#----------------------------------
#     Scan Barcode Function
#----------------------------------
    def ScanBarcodeClicked(self):
        #Print in terminal for testing:
        print("The Scan Barcode Button was clicked")
        #Switch from this screen to the Scan Barcode Options Popup Screen (Scene Swap):
        self.win = Ui_ScanBarcodePopup()
        self.win.show()
        #self.close()
#----------------------------------

#----------------------------------
#       Settings Function
#----------------------------------
    def SettingsClicked(self):
        #Print in terminal for testing:
        print("The Settings Button was clicked")

        self.ex = Ui_SettingsScreen(parent=self)
        self.ex.show()
        #self.close()
#----------------------------------

#----------------------------------
#       Refresh Function
#----------------------------------
    def RefreshClicked(self):
        #Print in terminal for testing:
        print("The Refresh Button was clicked")
        #Close and reopen the app (Refresh)
        self.win = Ui_MainDisplay()
        self.win.show()
        self.close()
#----------------------------------
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
      cursor.execute("UPDATE items SET Total_Length_Ft = Total_Length_Ft - ? WHERE Name = ?",(CheckoutQuantity, SelectedItemName,))
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
      cursor.execute("UPDATE items SET Total_Length_Ft = Total_Length_Ft + ? WHERE Name = ?",(CheckoutQuantity, SelectedItemName,))
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
#                              Low Quantity Alert Popup
#----------------------------------------------------------------------------------------------------
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

        #------------------------------------------
        #     Display Low Quantity Item Names 
        #------------------------------------------
        self.TextBrowser.setText("All these items are low in quantity:\n\n" + 
                                LowQuantityItems + ", " + LowQuantityWire +
                                "\n\nBe sure to order more!")
        #------------------------------------------

        #------------------------------------------
        #             Acknowledge Button
        #------------------------------------------
        AcknowledgeButton = self.AcknowledgeButton
        AcknowledgeButton.clicked.connect(self.AcknowledgeClicked)
    def AcknowledgeClicked(self):
      #Close the window
      self.parent()
      self.close()
    #------------------------------------------

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Low Quantity Alert!"))
        self.LowQuantityAlertHeader.setText(_translate("MainWindow", "Low Quantity Alert!"))
        self.ItemsWithLowQuantityAmountLable.setText(_translate("MainWindow", "()Items are Low in Quantity!"))
        self.TextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.AcknowledgeButton.setText(_translate("MainWindow", "Acknowledge"))
#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------
#                                       Settings Screen
#----------------------------------------------------------------------------------------------------
class Ui_SettingsScreen(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_SettingsScreen, self).__init__(parent)
        self.setObjectName("MainWindow")
        self.resize(942, 841)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.SettingsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.SettingsLabel.setFont(font)
        self.SettingsLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.SettingsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SettingsLabel.setObjectName("SettingsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.SettingsLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.DataBaseLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DataBaseLabel.setFont(font)
        self.DataBaseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DataBaseLabel.setObjectName("DataBaseLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.DataBaseLabel)
        self.DataBaseComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DataBaseComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DataBaseComboBox.setObjectName("DataBaseComboBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.DataBaseComboBox)
        self.OtherDatabasesLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OtherDatabasesLabel.setFont(font)
        self.OtherDatabasesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OtherDatabasesLabel.setObjectName("OtherDatabasesLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.OtherDatabasesLabel)
        self.OtherDatabasesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.OtherDatabasesComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OtherDatabasesComboBox.setObjectName("OtherDatabasesComboBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.OtherDatabasesComboBox)

        self.SecretButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SecretButton.setFont(font)
        self.SecretButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
        "border-style: none;")
        self.SecretButton.setObjectName("SecretButton")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.SecretButton)

        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(15, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.RegisterUserLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.RegisterUserLabel.setFont(font)
        self.RegisterUserLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.RegisterUserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RegisterUserLabel.setObjectName("RegisterUserLabel")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.SpanningRole, self.RegisterUserLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(18, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.NameLabel)
        self.NameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NameInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NameInput.setObjectName("NameInput")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.NameInput)
        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.PasswordLabel)
        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordInput.setObjectName("PasswordInput")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.PasswordInput)
        self.PrivilegeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PrivilegeLabel.setFont(font)
        self.PrivilegeLabel.setObjectName("PrivilegeLabel")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.PrivilegeLabel)
        self.PrivilegeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.PrivilegeComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PrivilegeComboBox.setObjectName("PrivilegeComboBox")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.PrivilegeComboBox)
        self.SubmitUserButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SubmitUserButton.setFont(font)
        self.SubmitUserButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.SubmitUserButton.setObjectName("SubmitUserButton")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.LabelRole, self.SubmitUserButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(26, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.MoreInfoLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.MoreInfoLabel.setFont(font)
        self.MoreInfoLabel.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.MoreInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MoreInfoLabel.setObjectName("MoreInfoLabel")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.SpanningRole, self.MoreInfoLabel)
        self.TotalValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalValueLabel.setFont(font)
        self.TotalValueLabel.setObjectName("TotalValueLabel")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.LabelRole, self.TotalValueLabel)
        self.TotalValueResultLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalValueResultLabel.setFont(font)
        self.TotalValueResultLabel.setStyleSheet("color: rgb(0, 110, 0);")
        self.TotalValueResultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TotalValueResultLabel.setObjectName("TotalValueResultLabel")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.FieldRole, self.TotalValueResultLabel)
        self.InfoLabel2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.InfoLabel2.setFont(font)
        self.InfoLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.InfoLabel2.setObjectName("InfoLabel2")
        self.formLayout.setWidget(29, QtWidgets.QFormLayout.LabelRole, self.InfoLabel2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(30, QtWidgets.QFormLayout.LabelRole, spacerItem4)
        self.TotalValueMarkUpLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalValueMarkUpLabel.setFont(font)
        self.TotalValueMarkUpLabel.setObjectName("TotalValueMarkUpLabel")
        self.formLayout.setWidget(31, QtWidgets.QFormLayout.LabelRole, self.TotalValueMarkUpLabel)
        self.TotalValueMarkUpResultLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalValueMarkUpResultLabel.setFont(font)
        self.TotalValueMarkUpResultLabel.setStyleSheet("color: rgb(0, 255, 0);")
        self.TotalValueMarkUpResultLabel.setObjectName("TotalValueMarkUpResultLabel")
        self.formLayout.setWidget(31, QtWidgets.QFormLayout.FieldRole, self.TotalValueMarkUpResultLabel)
        self.InfoLabel3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.InfoLabel3.setFont(font)
        self.InfoLabel3.setObjectName("InfoLabel3")
        self.formLayout.setWidget(32, QtWidgets.QFormLayout.LabelRole, self.InfoLabel3)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        #------------------------------------------
        #           Main Database Dropdown
        #------------------------------------------
        #Choose a database to access
        MainDatabases = [MainDatabase]
        self.DataBaseComboBox.addItems(MainDatabases)
        #------------------------------------------

        #------------------------------------------
        #        Other Database Table Display
        #------------------------------------------
        #Create a New Table
        self.CategoryTableView = QTableView()
        self.CategoryTableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CategoryTableView.clicked.connect(self.findrow)

        #Load Category Database as a Default
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(MainDatabase)
        self.model = QSqlTableModel()
        self.delrow = -1
        self.model.setTable("Categories")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()  
        self.CategoryTableView.setModel(self.model) 
        self.formLayout.setWidget(11,0, self.CategoryTableView)

        #Hide Column 0 (ID)
        self.CategoryTableView.setColumnHidden(0, True)
        
        #------------------------------------------
        #          Other Database Dropdown
        #------------------------------------------
        #Choose a database to access
        OtherDatabases = [MainDatabase, UserDatabase]
        self.OtherDatabasesComboBox.addItems(OtherDatabases)

        CurrentDatabase = self.OtherDatabasesComboBox
        CurrentDatabase.currentTextChanged.connect(self.DisplayDatabase)
        #------------------------------------------

        #------------------------------------------
        #               Secret Button
        #------------------------------------------
        #When the Secret button is clicked -> SecretButton Function
        SecretButton = self.SecretButton
        SecretButton.clicked.connect(self.SecretButtonClicked)

    def SecretButtonClicked(self):
        #Show the Password Column (Column 2)
        self.CategoryTableView.setColumnHidden(2, False)
        #------------------------------------------

    def DisplayDatabase(self):
        SelectedDatabase = self.OtherDatabasesComboBox.currentText()

        if SelectedDatabase == MainDatabase:
                TableName = "Categories"
                
                #Show Column 2
                self.CategoryTableView.setColumnHidden(2, False)
        
        elif SelectedDatabase == UserDatabase:
                TableName = "Users"
                
                #Hide Password Column (Column 2)
                self.CategoryTableView.setColumnHidden(2, True)
            
        else: 
                TableName = ""

        #------------------------------------------
        #          Other Database Display
        #------------------------------------------
        #Connect to Database
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(SelectedDatabase)
        self.model = QSqlTableModel()
        self.delrow = -1

        #Initialize Model
        self.model.setTable(TableName)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()  

        #Load the Data
        self.CategoryTableView.setModel(self.model) 

        #Set Table Position on GUI:
        self.formLayout.setWidget(11,0, self.CategoryTableView)

        #Only Selects Cells
        self.CategoryTableView.setSelectionBehavior(0)
        # 0 Selecting single items.
        # 1 Selecting only rows.
        # 2 Selecting only columns.

        #Make Specific Columns Un-Editable/ReadOnly
        class ReadOnlyDelegate(QStyledItemDelegate):
                def createEditor(self, parent, option, index):
                        print('This column is Read-Only')
                        return 
        delegate = ReadOnlyDelegate(self)
        self.CategoryTableView.setItemDelegateForColumn(0, delegate) #ID
        self.CategoryTableView.setItemDelegateForColumn(3, delegate) #Privilege (for users.db)

    def findrow(self, i):
        self.delrow = i.row()

    def getCellText(self):
        if self.CategoryTableView.selectedIndexes():
            model = self.CategoryTableView.model()
            row = self.selectedRow()
            column = 1 
                        
    def selectedRow(self):
        if self.CategoryTableView.selectionModel().hasSelection():
            row =  self.CategoryTableView.selectionModel().selectedIndexes()[0].row()
            return int(row)
 
    def selectedColumn(self):
        column =  self.CategoryTableView.selectionModel().selectedIndexes()[0].column()
        return int(column)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Settings"))
        self.SettingsLabel.setText(_translate("MainWindow", "Settings"))
        self.DataBaseLabel.setText(_translate("MainWindow", "Main Database"))
        self.OtherDatabasesLabel.setText(_translate("MainWindow", "Other Databases"))
        self.SecretButton.setText(_translate("MainWindow", ""))
        self.RegisterUserLabel.setText(_translate("MainWindow", "Register New User"))
        self.NameLabel.setText(_translate("MainWindow", "Name:"))
        self.PasswordLabel.setText(_translate("MainWindow", "Password:"))
        self.PrivilegeLabel.setText(_translate("MainWindow", "Privilege:"))
        self.SubmitUserButton.setText(_translate("MainWindow", "Submit User"))
        self.MoreInfoLabel.setText(_translate("MainWindow", "More Info"))
        self.TotalValueLabel.setText(_translate("MainWindow", "Total Inventory Value Without Markup:"))
        self.TotalValueResultLabel.setText(_translate("MainWindow", "$  "))
        self.InfoLabel2.setText(_translate("MainWindow", " "))
        self.TotalValueMarkUpLabel.setText(_translate("MainWindow", "Total Inventory Value With Markup:"))
        self.TotalValueMarkUpResultLabel.setText(_translate("MainWindow", "$ "))
        self.InfoLabel3.setText(_translate("MainWindow", " "))

        #------------------------------------------
        #      View Total Inventory Values
        #------------------------------------------
        self.TotalValueResultLabel.setText("$" + totalPriceNoMarkup)
        self.TotalValueMarkUpResultLabel.setText("$" + totalPriceMarkup)
        #------------------------------------------

        #------------------------------------------
        #           Register New User
        #------------------------------------------
        #Define Privilege Levels
        PrivilegeList = ['Admin','Standard']
        self.PrivilegeComboBox.addItems(PrivilegeList)

        #When the Submit User button is clicked -> SubmitUserClicked Function
        SubmitUserButton = self.SubmitUserButton
        SubmitUserButton.clicked.connect(self.SubmitUserClicked)
    #----------------------------------
    #   Submit User Clicked Function
    #----------------------------------
    def SubmitUserClicked(self):
        #Store the inputted values
        userInputName = self.NameInput.text()
        userInputPassword = self.PasswordInput.text()
        userInputPrivilege = self.PrivilegeComboBox.currentText()
        myList = [userInputName, userInputPassword, userInputPrivilege]

        if userInputName == "":
                self.NameLabel.setStyleSheet("color: rgb(255,0,0);")
                self.PasswordLabel.setStyleSheet("color: rgb(0,0,0);")

        elif userInputPassword == "":
                self.PasswordLabel.setStyleSheet("color: rgb(255,0,0);")
                self.NameLabel.setStyleSheet("color: rgb(0,0,0);")

        else:
                #Add the user to the users database
                import sqlite3
                connection = sqlite3.connect(UserDatabase)
                cursor = connection.cursor()
                cursor = connection.cursor()
                cursor.execute('''
                insert into Users (Name, Password, Privilege)
                values (?,?,?)
                ''', myList)
                connection.commit()
                connection.close()

                #Call User Added Popup
                self.UserAdded()
                
                #Clear the inputs
                self.NameInput.clear()
                self.PasswordInput.clear()
    #----------------------------------
    #       User Added Popup
    #----------------------------------
    def UserAdded(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("The user was successfully added to the database")
        msgBox.setWindowTitle("User Added")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('The Ok button was clicked')
    #------------------------------------------
#----------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------
#                                       Run this Program
#----------------------------------------------------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    win = Ui_MainDisplay()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
#----------------------------------------------------------------------------------------------------
