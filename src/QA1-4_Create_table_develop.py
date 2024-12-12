import sqlite3

def add_columns_to_tables():
    # Connect to the database (or create it if it doesn't exist)
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Add lastdate column to employees table
    cursor.execute('''
        ALTER TABLE employees ADD COLUMN lastdate DATE
    ''')

    # Add categoryGroup column to customers table
    cursor.execute('''
        ALTER TABLE customers ADD COLUMN categoryGroup TEXT
    ''')

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

# Call the function to add columns to the tables
add_columns_to_tables()
