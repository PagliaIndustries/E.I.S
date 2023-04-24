#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from CreateDatabases import createInventoryDatabase, createUserDatabase
from CreateImagesFolder import createImageFolder
from AdminMenu import Ui_MainDisplay
from MainMenu import Ui_MainMenu
  
class Ui_Loginscreen(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_Loginscreen, self).__init__(parent)
        self.setObjectName("Loginscreen")
        self.setFixedSize(500, 300)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Header = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Header.setFont(font)
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setObjectName("Header")
        self.gridLayout.addWidget(self.Header, 0, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.NameLabel)
        self.NameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NameInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NameInput.setText("")
        self.NameInput.setObjectName("NameInput")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NameInput)
        self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PasswordLabel.setFont(font)
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PasswordLabel)
        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        self.PasswordInput.setFont(font)
        self.PasswordInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordInput.setText("")
        self.PasswordInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PasswordInput.setObjectName("PasswordInput")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.PasswordInput)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;\n"
"padding: 4px;\n"
"")
        self.LoginButton.setObjectName("LoginButton")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.LoginButton)
        self.gridLayout.addLayout(self.formLayout_2, 1, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
  
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
  
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Loginscreen", "E.I.S"))
        self.Header.setText(_translate("Loginscreen", "Electronic Inventory System (E.I.S)"))
        self.NameLabel.setText(_translate("Loginscreen", "Name"))
        self.PasswordLabel.setText(_translate("Loginscreen", "Password"))
        self.label.setText(_translate("Loginscreen", "\n"
"\n"
"\n"
"\n"
"Electronic Inventory System (E.I.S)\n"
"Version: 5\n"
"Developed By: Paglia Industries\n"
"Last Updated: 04/24/2023\n"
"\n"
"\n"
""))
        self.LoginButton.setText(_translate("Loginscreen", "Log In"))

#----------------------------------------------------------------------------------------------------
#                                  Button Actions & Validator
#----------------------------------------------------------------------------------------------------
        #------------------------------------------
                        #Button Actions
        #------------------------------------------
        #When the Login button is clicked -> LoginClicked Function
        LoginButton = self.LoginButton
        LoginButton.clicked.connect(self.LoginClicked)
        #------------------------------------------
    #----------------------------------
    #           Validate User
    #----------------------------------
    def LoginClicked(self):
        #Store Name and Password
        userInputName = self.NameInput.text()
        userInputPassword = self.PasswordInput.text()

        print("The Login Button was clicked")
        #----------------------------------
        import sqlite3
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        cursor.execute(f"SELECT Privilege from Users WHERE Name ='{userInputName}' AND Password = '{userInputPassword}';")
        connection.commit()
        result = cursor.fetchone()
        print("Privilege Level: ",result)
        
        if result is None:
            print("Login Failed - Not a Valid User")
            #Call Invalid Credentials Popup
            self.invalidCredentials()

        else:
            privilege = ''.join(result)

            if privilege == "Admin":
                print('Success! You are now logged in as: ' + userInputName)
                #Switch from this screen to the AdminMenu Screen (Scene Swap):
                self.win = Ui_MainDisplay()
                self.win.show()
                self.close()

            elif privilege == "Standard":
                print('Success! You are now logged in as: ' + userInputName)
                #Switch from this screen to the MainMenu Screen
                self.win = Ui_MainMenu()
                self.win.show()
                self.close()
        
        #Close the connection
        connection.close()
        #----------------------------------
        #Print in terminal for testing:
        # print("Name: " + userInputName)
        # print("Password: " + userInputPassword)
        #----------------------------------
#-----------------------------------------------------------------
    #----------------------------------
    #   Invalid Credentials Popup
    #----------------------------------
    def invalidCredentials(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("You are not registered to use this program")
        msgBox.setWindowTitle("Invalid Credentials")
        msgBox.setStandardButtons(QMessageBox.Ok)
  
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('The user has acknowledged the Invalid Credentials')
#-----------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Loginscreen()
    ui.show()

    #----------------------------------
    #        First Run Setup
    #----------------------------------
    #Create the Inventory database if it does not exist 
    createInventoryDatabase()
    #Create the User database if one does not exist
    createUserDatabase()
    #Create a folder to store Product Images
    createImageFolder()
    #----------------------------------

    sys.exit(app.exec_())