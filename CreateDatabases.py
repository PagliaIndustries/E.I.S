import sqlite3

#----------------------------------------------------------------------------------------------
#                                 Create Inventory Database
#----------------------------------------------------------------------------------------------
def createInventoryDatabase():
        #Create a database (inventory.db)
        connection = sqlite3.connect("inventory.db")
        cursor = connection.cursor()

        table = """CREATE TABLE IF NOT EXISTS Items
                (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
                Name                TEXT    NOT NULL,
                Quantity            INT     NOT NULL,
                Price_$             DOUBLE  NOT NULL,
                Sell_Price_$        DOUBLE,
                Description         TEXT,
                Main_Category       TEXT,
                Subcategory         TEXT,
                Location            TEXT    NOT NULL,
                Spool_Length_Ft     INT,
                Spool_Price_$       DOUBLE  NOT NULL,
                Spool_Sell_Price_$  DOUBLE,
                Price_Per_Ft        INT, 
                Total_Length_Ft     INT,
                Barcode             INT,
                Date Updated        datetime default current_timestamp);"""

        #Execute the creation of the table
        cursor.execute(table)
        #print("The database has been created")
        #Commit the changes
        connection.commit()

        #Create the Categories Table
        table2 = """CREATE TABLE IF NOT EXISTS Categories
                (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
                Main_Category       TEXT,
                Subcategory         TEXT,
                Low_Quantity_Value  INT);"""
 
        #Execute the creation of the table
        cursor.execute(table2)
        #print("The database has been created")
        #Commit the changes
        connection.commit()

        #Add default values to the table:
        defaultValues = cursor.execute(
        """SELECT COUNT(*) FROM Categories """).fetchone()[0]
        if defaultValues == 0:      
                #Add a default category
                cursor.execute('''
                INSERT into Categories (Main_Category, Subcategory, Low_Quantity_Value)
                VALUES ('N/A','N/A','0')
                ''')
                connection.commit()
                connection.close()
        else:
                connection.close() 
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
#                                   Create User Database
#----------------------------------------------------------------------------------------------
def createUserDatabase():
        #Create a database (users.db)
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
 
        table = """CREATE TABLE IF NOT EXISTS Users
                (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
                Name           TEXT    NOT NULL,
                Password       TEXT    NOT NULL,
                Privilege      TEXT    NOT NULL);"""
 
        #Execute the creation of the table
        cursor.execute(table)
        #print("The database has been created")
        #Commit the changes
        connection.commit()

         #Add default values to table:
        defaultValues = cursor.execute(
        """SELECT * FROM Users """).fetchall()
        if len(defaultValues) == 0:      
                #Add a default Admin Login
                cursor.execute('''
                insert into Users (Name, Password, Privilege)
                VALUES ('Admin',1234,'Admin')
        ''')
                connection.commit()
                connection.close()
        else:
                connection.close() 
#----------------------------------------------------------------------------------------------
