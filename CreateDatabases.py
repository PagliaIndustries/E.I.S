import sqlite3

#----------------------------------------------------------------------------------------------
#                                 Create Inventory Database
#----------------------------------------------------------------------------------------------
def createInventoryDatabase():
        #Create a database (inventory.db)
        connection = sqlite3.connect("inventory.db")
        cursor = connection.cursor()

        table = """CREATE TABLE IF NOT EXISTS Items
                (Image                          TEXT,
                Name                            TEXT,
                Quantity                        INT,
                Price_$                         DOUBLE,
                Sell_Price_$                    DOUBLE,
                Description                     TEXT,
                Main_Category                   TEXT,
                Subcategory                     TEXT,
                Location                        TEXT,
                Spool_or_Pipe_Length_Ft         INT,
                Spool_or_Pipe_Price_$           DOUBLE,
                Spool_or_Pipe_Sell_Price_$      DOUBLE,
                Price_Per_Ft_$                  INT, 
                Total_Length_Ft                 INT,
                Barcode                         INT,
                Date Updated                    datetime default current_timestamp);"""

        #Execute the creation of the table
        cursor.execute(table)
        #print("The database has been created")
        #Commit the changes
        connection.commit()

#-------------------
        # -------------------
        # Create Categories table
        # -------------------
        table2 = """CREATE TABLE IF NOT EXISTS Categories
                (ID INTEGER PRIMARY KEY,
                Main_Category TEXT);"""
        # Execute the creation of the table
        cursor.execute(table2)
        # Commit the changes
        connection.commit()

        # -------------------
        # Create Subcategories table
        # -------------------
        # Create Subcategories table
        table3 = """CREATE TABLE IF NOT EXISTS Subcategories
                (id INTEGER PRIMARY KEY,
                Subcategory TEXT,
                Low_Quantity_Value INTEGER,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES Categories(ID));"""

        # Execute the creation of the table
        cursor.execute(table3)
        # Commit the changes
        connection.commit()
#------------------------------
        # Print the contents of the Items table
        cursor.execute("SELECT * FROM Items")
        items_data = cursor.fetchall()
        print("Items:")
        for item in items_data:
                print(item)

        # Print the contents of the Categories table
        cursor.execute("SELECT * FROM Categories")
        categories_data = cursor.fetchall()
        print("Categories:")
        for category in categories_data:
                print(category)

        # Print the contents of the Subcategories table
        cursor.execute("SELECT * FROM Subcategories")
        subcategories_data = cursor.fetchall()
        print("Subcategories:")
        for subcategory in subcategories_data:
                print(subcategory)

        # Close the database connection
        connection.close()
#------------------------------
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
