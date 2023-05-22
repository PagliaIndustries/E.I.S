import sqlite3

def categoryINTchecker():
    # Connect to the database
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Check the data type of the Low_Quantity_Value column in the Subcategories table
    c.execute("PRAGMA table_info(Subcategories)")
    for col in c.fetchall():
        if col[1] == 'Low_Quantity_Value':
            data_type = col[2]

    if data_type != 'INTEGER':
        # Update any non-integer values in the Low_Quantity_Value column to 0
        c.execute("UPDATE Subcategories SET Low_Quantity_Value = 0 WHERE NOT CAST(Low_Quantity_Value AS INTEGER) = Low_Quantity_Value")
        conn.commit()

    # Retrieve the Low_Quantity_Value values from the Subcategories table
    query = "SELECT Low_Quantity_Value FROM Subcategories"
    results = c.execute(query).fetchall()

    # Process the results
    for result in results:
        print(result[0])

    # Close the connection
    conn.close()
