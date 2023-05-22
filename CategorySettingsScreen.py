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

#----------------------------------------------------------------------------------------------
#                                 Category Settings
#----------------------------------------------------------------------------------------------
class Ui_CategoryEdit(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_CategoryEdit, self).__init__(parent)
        self.setObjectName("Category Edit")
        self.setFixedSize(638, 472)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.CategoryComboBox = QtWidgets.QComboBox(self.frame)
        self.CategoryComboBox.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.CategoryComboBox.setObjectName("CategoryComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CategoryComboBox)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.CategoryLineEdit = QtWidgets.QLineEdit(self.frame)
        self.CategoryLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CategoryLineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.CategoryLineEdit)
        self.AddCategoryButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AddCategoryButton.setFont(font)
        self.AddCategoryButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.AddCategoryButton.setObjectName("pushButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.AddCategoryButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.SubCategoryCombobox = QtWidgets.QComboBox(self.frame)
        self.SubCategoryCombobox.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.SubCategoryCombobox.setObjectName("comboBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.SubCategoryCombobox)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.SubCategoryLineEdit = QtWidgets.QLineEdit(self.frame)
        self.SubCategoryLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SubCategoryLineEdit.setObjectName("lineEdit_2")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.SubCategoryLineEdit)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.LowQuantityValueSpinBox = QtWidgets.QSpinBox(self.frame)
        self.LowQuantityValueSpinBox.setStyleSheet("background-color: rgb(210, 210, 210);")
        self.LowQuantityValueSpinBox.setObjectName("spinBox")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.LowQuantityValueSpinBox)
        self.AddSubCategoryButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AddSubCategoryButton.setFont(font)
        self.AddSubCategoryButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"padding: 4px;")
        self.AddSubCategoryButton.setObjectName("pushButton_2")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.AddSubCategoryButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(14, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
#----------------------------------------------------------------------------------------------
        #------------------------------------------
        #            Add Category Button
        #------------------------------------------
        #When the Add button is clicked -> AddCategoryClicked Function
        AddCategoryButton = self.AddCategoryButton
        AddCategoryButton.clicked.connect(self.AddCategoryClicked)
        #------------------------------------------
        #---------------------------------------------------------------
        #------------------------------------------
        #            Add SubCategory Button
        #------------------------------------------
        #When the Add button is clicked -> AddCategoryClicked Function
        AddSubCategoryButton = self.AddSubCategoryButton
        AddSubCategoryButton.clicked.connect(self.AddSubCategoryClicked)
        #---------------------------------------------------------------

        # ------------------------------------------
        # Connect to Database
        # ------------------------------------------
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        # Don't display the blank values and order results A->Z
        c.execute('''SELECT DISTINCT Main_Category FROM Categories WHERE Main_Category IS NOT NULL 
                AND Main_Category <> '' ORDER BY Main_Category ASC''')
        main_category_data = c.fetchall()
        c.close()
        main_category_combo_data = []
        for row in main_category_data:
                main_category_combo_data.append(row[0])

        # ------------------------------------------
        # Category Dropdown
        # ------------------------------------------
        CategoryComboBox = self.CategoryComboBox
        CategoryComboBox.addItems(main_category_combo_data)
        CategoryComboBox.currentIndexChanged.connect(self.onCategorySelected)
        CategoryComboBox.show()
        # ------------------------------------------
        # SubCategory Dropdown
        # ------------------------------------------
        SubCategoryComboBox = self.SubCategoryCombobox
        SubCategoryComboBox.show()
        
        #------------------------------------------
        # When Main category is Changed Display Associated Subcategories
        #------------------------------------------
    def onCategorySelected(self):
        selected_main_category = self.CategoryComboBox.currentText()

        # Connect to Database
        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()

        # Retrieve subcategories for the selected main category using a JOIN and additional condition
        c.execute('''SELECT DISTINCT S.Subcategory 
                        FROM Subcategories S 
                        JOIN Categories C ON S.category_id = C.ID 
                        WHERE C.Main_Category = ? 
                        AND S.Subcategory IS NOT NULL 
                        AND S.Subcategory <> '' 
                        AND C.Main_Category = ? 
                        ORDER BY S.Subcategory ASC''', (selected_main_category, selected_main_category))
        subcategory_data = c.fetchall()
        c.close()

        subcategory_combo_data = []
        for row in subcategory_data:
                subcategory_combo_data.append(row[0])

        # Clear and update the SubCategoryComboBox
        self.SubCategoryCombobox.clear()
        self.SubCategoryCombobox.addItems(subcategory_combo_data)
        #------------------------------------------

        #------------------------------------------
        #       Add SubCategory Clicked Function
        #------------------------------------------
    def AddSubCategoryClicked(self):
        # Define LowQuantitySpinBox
        self.LowQuantityValueSpinBox.setMaximum(MaxValue) # Set Max Value for SpinBox
        LowQuantityValue = self.LowQuantityValueSpinBox.text() # Get the SpinBox's Current Value
        
        # Define SubCategory Input
        NewSubCategory = self.SubCategoryLineEdit.text()
        
        # Get the currently selected main category
        selected_main_category = self.CategoryComboBox.currentText()

        print("SubCategory Add Button Clicked")
        
        if NewSubCategory == "":
                print("Nothing new to add")
        else:
                # Insert the new subcategory into the Subcategories table and associate it with the selected main category
                conn = sqlite3.connect('inventory.db')
                c = conn.cursor()
                c.execute('''INSERT INTO Subcategories (Subcategory, category_id, Low_Quantity_Value)
                        VALUES (?, (SELECT ID FROM Categories WHERE Main_Category = ?), ?)''',
                        (NewSubCategory, selected_main_category, LowQuantityValue))
                conn.commit()
                c.close()

        # Refresh the SubCategory dropdown to display the updated list
        self.onCategorySelected()
        
        # Clear the input fields
        self.SubCategoryLineEdit.clear()
        self.LowQuantityValueSpinBox.clear()
        #------------------------------------------
        #        Add Category Clicked Function 
        #------------------------------------------
    def AddCategoryClicked(self):
        NewMainCategory = self.CategoryLineEdit.text()
        if NewMainCategory == "":
             print("Nothing new to add")
        else:
             NewMainCategoryValue = [NewMainCategory]
             conn = sqlite3.connect('inventory.db')
             c = conn.cursor()
             c.execute('''INSERT into Categories (Main_Category) values (?)''', NewMainCategoryValue)
             conn.commit()
             c.close()
        
        #Close and reopen the app (Refresh to see changes)
        self.win = Ui_CategoryEdit()
        self.win.show()
        self.close()
        #------------------------------------------
#----------------------------------------------------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Category Edit"))
        self.label.setText(_translate("MainWindow", "Category Settings"))
        self.label_7.setText(_translate("MainWindow", "Main Category"))
        self.label_2.setText(_translate("MainWindow", "Category"))
        self.label_5.setText(_translate("MainWindow", "Input New Category"))
        self.AddCategoryButton.setText(_translate("MainWindow", "Add"))
        self.label_8.setText(_translate("MainWindow", "Subcategory"))
        self.label_3.setText(_translate("MainWindow", "Subcategory"))
        self.label_6.setText(_translate("MainWindow", "Input New Subcategory"))
        self.label_4.setText(_translate("MainWindow", "Low Quantity Value"))
        self.AddSubCategoryButton.setText(_translate("MainWindow", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_CategoryEdit()
    win.show()
    sys.exit(app.exec_())
