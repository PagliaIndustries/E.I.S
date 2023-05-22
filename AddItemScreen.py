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


class Ui_AddItemMenu(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_AddItemMenu, self).__init__(parent)
        self.setObjectName("AddItemMenu")
        self.setFixedSize(704, 538)
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
        self.QuantityLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.QuantityLabel.setFont(font)
        self.QuantityLabel.setObjectName("QuantityLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.QuantityLabel)
        self.QuantityInput = QtWidgets.QSpinBox(self.centralwidget)
        self.QuantityInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.QuantityInput.setObjectName("QuantityInput")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.QuantityInput)
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
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.image_path = None #Declare image_path at the class level

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AddItemMenu", "Add Item Window"))
        self.AddItemTitle.setText(_translate("AddItemMenu", "Add Item Info"))
        self.NameLabel.setText(_translate("AddItemMenu", "Name"))
        self.QuantityLabel.setText(_translate("AddItemMenu", "Quantity"))
        self.PriceLabel.setText(_translate("AddItemMenu", "Price (per unit)"))
        self.DescriptionLabel.setText(_translate("AddItemMenu", "Description"))
        self.CategoryLabel.setText(_translate("AddItemMenu", "Main Category"))
        self.SubcategoryLabel.setText(_translate("AddItemMenu", "Subcategory"))
        self.LocationLabel.setText(_translate("AddItemMenu", "Location"))
        self.BarcodeLabel.setText(_translate("AddItemMenu", "Barcode #"))
        self.label_3.setText(_translate("AddItemMenu", "*Please generate a custom barcode for this item and enter that barcode number in this field "))
        self.UploadImageButton.setText(_translate("AddItemMenu", "Upload Image"))
        self.pushButton.setText(_translate("AddItemMenu", "Submit"))
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#                                            Values
#----------------------------------------------------------------------------------------------------
        # Connect to the Category database
        connection = sqlite3.connect(MainDatabase)
        cursor = connection.cursor()

        # ------------------------------------------
        # Main Category Dropdown
        # ------------------------------------------
        cursor.execute('''SELECT DISTINCT Main_Category FROM Categories WHERE Main_Category IS NOT NULL 
                        AND Main_Category <> '' ORDER BY Main_Category ASC''')
        main_category_data = cursor.fetchall()

        # Convert the SQL Results to a String List
        main_category_combo_data = [row[0] for row in main_category_data]

        # Close the connection
        connection.close()

        # Add the Main Categories to the Dropdown List
        self.CategoryInput.addItems(main_category_combo_data)

        # ------------------------------------------
        # Function to retrieve and display associated subcategories
        # ------------------------------------------
        def displayAssociatedSubcategories():
            # Get the selected main category
            selected_main_category = self.CategoryInput.currentText()

            # Connect to the Category database
            connection = sqlite3.connect(MainDatabase)
            cursor = connection.cursor()

            # Retrieve associated subcategories for the selected main category
            cursor.execute('''SELECT DISTINCT Subcategory FROM Subcategories
                            WHERE category_id IN (
                                SELECT ID FROM Categories
                                WHERE Main_Category = ?
                            )
                            AND Subcategory IS NOT NULL 
                            AND Subcategory <> ''
                            ORDER BY Subcategory ASC''', (selected_main_category,))

            # Get the Subcategories from the Database
            subcategory_data = cursor.fetchall()

            # Convert the SQL Results to a String List
            subcategory_combo_data = [row[0] for row in subcategory_data]

            # Close the connection
            connection.close()

            # Clear and update the SubcategoryComboBox
            self.SubcategoryComboBox.clear()
            self.SubcategoryComboBox.addItems(subcategory_combo_data)

        # Connect the onCategorySelected function to the CategoryInput's currentIndexChanged signal
        self.CategoryInput.currentIndexChanged.connect(displayAssociatedSubcategories)

#----------------------------------------------------------------------------------------------------
#                           Max Value for Price & Quantity SpinBox
#----------------------------------------------------------------------------------------------------
        self.PriceInput.setMaximum(MaxValue)
        self.QuantityInput.setMaximum(MaxValue)
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
#----------------------------------
    #Upload Image Function
    def UploadImageClicked(self):
        # Show file dialog to select an image from Product_Images Folder
        fname = QFileDialog.getOpenFileName(self, 'Select Image', './Product_Images')[0]

        # If user selects an image
        if fname:
            # Update the image_path variable
            self.image_path = fname
            # Read image data from file
            with open(self.image_path, 'rb') as f:
                image_data = f.read()
        else:
            self.image_path = None
#----------------------------------
    #Submit Function
    def SubmitClicked(self):
        #Store the user's inputs
        ItemName = self.NameInput.text()
        Quantity = self.QuantityInput.text()
        Price = self.PriceInput.text()
        Description = self.DescriptionInput.toPlainText()
        Category = self.CategoryInput.currentText()
        Subcategory = self.SubcategoryComboBox.currentText()
        Location = self.LocationInput.text()
        Barcode = self.BarcodeInput.text()
        
        #So we don't get errors for Wire columns during calculations 
        SpoolPrice = 0
        Length = 0
        TotalLength = Length

        if self.image_path is None:
            self.image_path = "./Product_Images/na.jpg"  # Default image path
        

        mylist = [ItemName, Quantity, Price,  Description, Category, Subcategory, 
                Location, Length, SpoolPrice, TotalLength, Barcode , self.image_path]

        #--------------------------------------------------
        #Alert user of any empty values that should not be
        #left null, before adding the item to the database
        #--------------------------------------------------
        if ItemName == "":
            self.NameLabel.setStyleSheet("color: rgb(255,0,0);")
            self.QuantityLabel.setStyleSheet("color: rgb(0,0,0);")
            self.LocationLabel.setStyleSheet("color: rgb(0,0,0);")
            self.PriceLabel.setStyleSheet("color: rgb(0,0,0);")
            self.NameLabel.setText("*Name (Required)")
            self.QuantityLabel.setText("Quantity")
            self.PriceLabel.setText("Price")
            self.LocationLabel.setText("Location")

        elif Quantity == "0":
            self.QuantityLabel.setStyleSheet("color: rgb(255,0,0);")
            self.NameLabel.setStyleSheet("color: rgb(0,0,0);")
            self.LocationLabel.setStyleSheet("color: rgb(0,0,0);")
            self.PriceLabel.setStyleSheet("color: rgb(0,0,0);")
            self.QuantityLabel.setText("*Quantity (Required)")
            self.NameLabel.setText("Name")
            self.PriceLabel.setText("Price")
            self.LocationLabel.setText("Location")

        elif Price == "0.00":
            self.PriceLabel.setStyleSheet("color: rgb(255,0,0);")
            self.QuantityLabel.setStyleSheet("color: rgb(0,0,0);")
            self.LocationLabel.setStyleSheet("color: rgb(0,0,0);")
            self.PriceLabel.setText("*Price (Required)")
            self.NameLabel.setText("Name")
            self.QuantityLabel.setText("Quantity")
            self.LocationLabel.setText("Location")

        elif Category == "N/A" or Category == '---':
            self.CategoryLabel.setStyleSheet("color: rgb(255,0,0);")
            self.LocationLabel.setStyleSheet("color: rgb(0,0,0);")
            self.QuantityLabel.setStyleSheet("color: rgb(0,0,0);")
            self.NameLabel.setStyleSheet("color: rgb(0,0,0);")
            self.PriceLabel.setStyleSheet("color: rgb(0,0,0);")
            self.CategoryLabel.setText("*Main Category (Required)")
            self.LocationLabel.setText("Location")
            self.NameLabel.setText("Name")
            self.QuantityLabel.setText("Quantity")
            self.PriceLabel.setText("Price")

        elif Location == "":
            self.LocationLabel.setStyleSheet("color: rgb(255,0,0);")
            self.CategoryLabel.setStyleSheet("color: rgb(0,0,0);")
            self.QuantityLabel.setStyleSheet("color: rgb(0,0,0);")
            self.NameLabel.setStyleSheet("color: rgb(0,0,0);")
            self.PriceLabel.setStyleSheet("color: rgb(0,0,0);")
            self.LocationLabel.setText("*Location (Required)")
            self.NameLabel.setText("Name")
            self.QuantityLabel.setText("Quantity")
            self.PriceLabel.setText("Price")
            self.CategoryLabel.setText("Main Category")

        else:
            #Print in terminal for testing:
            print("The Submit Button was clicked")
            print(ItemName, Quantity, Price, Description, Category, Subcategory, Location, Barcode)

            #Connect to the inventory database (inventory.db)
            connection = sqlite3.connect(MainDatabase)
            cursor = connection.cursor()
            cursor.execute('''
                insert into items (name, quantity, price_$, description, Main_Category, subcategory, 
                                    location, Spool_or_Pipe_Length_Ft, Spool_or_Pipe_Price_$, Total_Length_Ft, Barcode, image)
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
    ui = Ui_AddItemMenu()
    ui.show()
    sys.exit(app.exec_())
