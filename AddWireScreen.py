#!/usr/bin/env python3

#----------------------------------------------------------------------------------------------
#                                  Table Of Contents/Overview
#----------------------------------------------------------------------------------------------
# Values for Main Category
# Values for Subcategory
# Max Values
# Button Actions
# Required Info Alerts
#----------------------------------------------------------------------------------------------

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sqlite3
from Constants import MaxValue, MainDatabase


class Ui_AddWireMenu(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_AddWireMenu, self).__init__(parent)
        self.setObjectName("AddWireMenu")
        self.setFixedSize(804, 638)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.AddItemTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.AddItemTitle.setFont(font)
        self.AddItemTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.AddItemTitle.setObjectName("AddItemTitle")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.AddItemTitle)
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.NameLabel)
        self.NameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NameInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NameInput.setText("")
        self.NameInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.NameInput.setObjectName("NameInput")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.NameInput)
        spacerItem = QtWidgets.QSpacerItem(0, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(0, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.PriceLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PriceLabel.setFont(font)
        self.PriceLabel.setObjectName("PriceLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.PriceLabel)
        self.PriceInput = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.PriceInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PriceInput.setObjectName("PriceInput")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.PriceInput)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.DescriptionLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DescriptionLabel.setFont(font)
        self.DescriptionLabel.setObjectName("DescriptionLabel")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.DescriptionLabel)
        self.DescriptionInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.DescriptionInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DescriptionInput.setObjectName("DescriptionInput")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.DescriptionInput)
        self.CategoryLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CategoryLabel.setFont(font)
        self.CategoryLabel.setObjectName("CategoryLabel")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.CategoryLabel)
        self.CategoryInput = QtWidgets.QComboBox(self.centralwidget)
        self.CategoryInput.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.CategoryInput.setObjectName("CategoryInput")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.CategoryInput)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(10, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.SubcategoryLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SubcategoryLabel.setFont(font)
        self.SubcategoryLabel.setObjectName("SubcategoryLabel")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.SubcategoryLabel)
        self.SubcategoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SubcategoryComboBox.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.SubcategoryComboBox.setObjectName("SubcategoryComboBox")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.SubcategoryComboBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(13, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.LocationLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LocationLabel.setFont(font)
        self.LocationLabel.setObjectName("LocationLabel")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.LocationLabel)
        self.LocationInput = QtWidgets.QLineEdit(self.centralwidget)
        self.LocationInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LocationInput.setObjectName("LocationInput")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.LocationInput)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(15, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.BarcodeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BarcodeLabel.setFont(font)
        self.BarcodeLabel.setObjectName("BarcodeLabel")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.BarcodeLabel)
        self.BarcodeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.BarcodeInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BarcodeInput.setObjectName("BarcodeInput")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.BarcodeInput)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(0, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(18, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.label_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(21, QtWidgets.QFormLayout.FieldRole, spacerItem7)
        #Buttons
        self.UploadImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.UploadImageButton.setMinimumSize(QtCore.QSize(0, 0))
        self.UploadImageButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.UploadImageButton.setFont(font)
        self.UploadImageButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UploadImageButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.UploadImageButton.setObjectName("UploadImageButton")
        self.formLayout_2.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.UploadImageButton)   
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.pushButton.setObjectName("pushButton")
        self.formLayout_2.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AddItemMenu", "Add Wire Window"))
        self.AddItemTitle.setText(_translate("AddItemMenu", "Add Wire Info"))
        self.NameLabel.setText(_translate("AddItemMenu", "Name"))
        self.PriceLabel.setText(_translate("AddItemMenu", "Price (of 1 Spool)"))
        self.DescriptionLabel.setText(_translate("AddItemMenu", "Description"))
        self.CategoryLabel.setText(_translate("AddItemMenu", "Main Category"))
        self.SubcategoryLabel.setText(_translate("AddItemMenu", "Subcategory"))
        self.LocationLabel.setText(_translate("AddItemMenu", "Location"))
        self.BarcodeLabel.setText(_translate("AddItemMenu", "Barcode #"))
        self.label_3.setText(_translate("AddItemMenu", "*Please generate a custom barcode for this item and enter that barcode number in this field "))
        self.label.setText(_translate("AddItemMenu", "Spool Length (ft)"))
        self.label_2.setText(_translate("AddItemMenu", "*Please provide the full spool length in feet. "))
        self.UploadImageButton.setText(_translate("AddItemMenu", "Upload Image"))
        self.pushButton.setText(_translate("AddItemMenu", "Submit"))
        self.label_5.setText(_translate("AddItemMenu", "*Please enter the price of one full spool. "))


#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#                                            Values
#----------------------------------------------------------------------------------------------------
#                                  Values for Main_Categories
#----------------------------------------------------------------------------------------------------
        MainCategoryListValue = ['Wire', 'Pipe']
        self.CategoryInput.addItems(MainCategoryListValue)
        self.CategoryInput.currentIndexChanged.connect(self.onCategoryChanged)
#----------------------------------------------------------------------------------------------------
#                                Values for Subcategories
#----------------------------------------------------------------------------------------------------
        #Connect to the Category database
        connection = sqlite3.connect(MainDatabase)
        cursor = connection.cursor()
        #Don't display the blank values and order results A->Z
        cursor.execute('''SELECT DISTINCT Subcategory FROM Categories WHERE Subcategory IS NOT NULL 
                AND Subcategory <> '' ORDER BY Subcategory ASC''')
        connection.commit()
        
        #Get the Categories from the Database
        CategoryList = cursor.fetchall()

        #Convert the SQL Results to a String List
        from itertools import chain
        StringCategoryList = list(chain.from_iterable(CategoryList))
     
        #Close the connection
        connection.close()

        #Add the SQL Results to the Dropdown List
        self.SubcategoryComboBox.addItems(StringCategoryList)
#----------------------------------------------------------------------------------------------------
#                           Max Value for Price, Quantity & Length SpinBox
#----------------------------------------------------------------------------------------------------
        self.PriceInput.setMaximum(MaxValue)
        self.spinBox.setMaximum(MaxValue)
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#                                       Button Actions
#----------------------------------------------------------------------------------------------------
        #------------------------------------------
                        #Upload Image Button
        #------------------------------------------
        #When the Upload Image button is clicked -> UploadImageClicked Function
        UploadImageButton = self.UploadImageButton
        UploadImageButton.clicked.connect(self.UploadImageClicked)
        #------------------------------------------
        #------------------------------------------
                        #Submit Button
        #------------------------------------------
        #When the Submit button is clicked -> submitClicked Function
        SubmitButton = self.pushButton
        SubmitButton.clicked.connect(self.SubmitClicked)
        #------------------------------------------

#------------------------------------------
#                   Add Pipe
#------------------------------------------        
    def onCategoryChanged(self):
        if self.CategoryInput.currentText() == "Pipe":
            self.updateUI()
        else:
            pass

    # Define the slot function
    def updateUI(self):
        self.AddItemTitle.setText("Add Pipe Info")
        self.PriceLabel.setText("Price")
        self.label.setText("Pipe Length (ft)")
        self.label_2.setText("*Please provide the full pipe length in feet. ")
        self.label_5.setText("*Please enter the price of one full pipe length. ")
#----------------------------------

#----------------------------------
    #Upload Image Function
    def UploadImageClicked(self):
        #Show file dialog to select an image from Product_Images Folder
        fname = QFileDialog.getOpenFileName(self, 'Select Image', './Product_Images')[0]

        # If user selects an image
        if fname:
            #--------------------------------------------------
            #Show file dialog to select an image from Product_Images Folder
            global image_path
            image_path = fname
            # If an image was selected
            if image_path:
                # Read image data from file
                with open(image_path, 'rb') as f:
                    image_data = f.read()
            else:
                image_data = None
            #--------------------------------------------------
        else:
            image_path = None
        
#----------------------------------

#----------------------------------
    #Submit Function
    def SubmitClicked(self):
        #Store the user's inputs
        ItemName = self.NameInput.text()
        Price = self.PriceInput.text()
        Description = self.DescriptionInput.toPlainText()
        Category = self.CategoryInput.currentText()
        Subcategory = self.SubcategoryComboBox.currentText()
        Location = self.LocationInput.text()
        Barcode = self.BarcodeInput.text()
        Length = self.spinBox.value()
        TotalLength = Length

        #So we don't get errors for Quantity and Price_$ columns during calculations 
        ItemQuantity = 0 
        ItemPrice = 0

        mylist = [ItemName, ItemQuantity, ItemPrice, Description, Category, Subcategory, 
                Location, Length, Price, TotalLength, Barcode, image_path]

        #--------------------------------------------------
        #Alert user of any empty values that should not be
        #left null, before adding the item to the database
        #--------------------------------------------------
        if ItemName == "":
            self.NameLabel.setStyleSheet("color: rgb(255,0,0);")
            self.LocationLabel.setStyleSheet("color: rgb(0,0,0);")
            self.PriceLabel.setStyleSheet("color: rgb(0,0,0);")
            self.NameLabel.setText("*Name (Required)")
            self.QuantityLabel.setText("Quantity")
            self.PriceLabel.setText("Price")
            self.LocationLabel.setText("Location")

        elif Price == "0.00":
            self.PriceLabel.setStyleSheet("color: rgb(255,0,0);")
            self.LocationLabel.setStyleSheet("color: rgb(0,0,0);")
            self.PriceLabel.setText("*Price (Required)")
            self.NameLabel.setText("Name")
            self.QuantityLabel.setText("Quantity")
            self.LocationLabel.setText("Location")

        elif Location == "":
            self.LocationLabel.setStyleSheet("color: rgb(255,0,0);")
            self.CategoryLabel.setStyleSheet("color: rgb(0,0,0);")
            self.NameLabel.setStyleSheet("color: rgb(0,0,0);")
            self.PriceLabel.setStyleSheet("color: rgb(0,0,0);")
            self.LocationLabel.setText("*Location (Required)")
            self.NameLabel.setText("Name")
            self.QuantityLabel.setText("Quantity")
            self.PriceLabel.setText("Price")

        else:
            #Print in terminal for testing:
            print("The Submit Button was clicked")

            #Connect to the inventory database (inventory.db)
            connection = sqlite3.connect(MainDatabase)
            cursor = connection.cursor()
            cursor.execute('''
                insert into items (Name, Quantity, Price_$, Description, Main_Category, Subcategory, 
                                    Location, Spool_or_Pipe_Length_Ft, Spool_or_Pipe_Price_$,
                                    Total_Length_Ft, Barcode, Image)
                values (?,?,?,?,?,?,?,?,?,?,?,?)
                ''', mylist)
            connection.commit()
            #Close the connection
            connection.close()

            self.close() #Close this screen 
#----------------------------------
#----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_AddWireMenu()
    ui.show()
    sys.exit(app.exec_())
