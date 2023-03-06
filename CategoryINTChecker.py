import sqlite3
#----------------------------------------------------------------------------------------------
#                                 Low Quantity Value INT Checker 
#----------------------------------------------------------------------------------------------
#------------------------------------------
# Checks Integrity of Categories Table 
# to ensure the Low Quantity Values are INTs. 
# If not, it changes them to a default value of 0  
#------------------------------------------
def categoryINTchecker():
    # Connect to the database
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Check the data type of the Low_Quantity_Value column
    c.execute("PRAGMA table_info(Categories)")
    for col in c.fetchall():
        if col[1] == 'Low_Quantity_Value':
            data_type = col[2]

    if data_type != 'INTEGER':
        # Update any non-integer values in the Low_Quantity_Value column to 0
        c.execute("UPDATE Categories SET Low_Quantity_Value = 0 WHERE NOT CAST(Low_Quantity_Value AS INTEGER) = Low_Quantity_Value")
        conn.commit()

    # Retrieve the Low_Quantity_Value values from the Categories table
    query = "SELECT Low_Quantity_Value FROM Categories"
    results = c.execute(query).fetchall()

    # # Process the results
    # for result in results:
    #     print(result[0])

    # Close the connection
    conn.close()


