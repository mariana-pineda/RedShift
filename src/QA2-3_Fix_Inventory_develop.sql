ALTER TABLE qa.employees
ADD COLUMN lastdate DATE DEFAULT CURRENT_DATE;

ALTER TABLE qa.customers
ADD COLUMN categorygroup VARCHAR DEFAULT 'Uncategorized';



import psycopg2

def update_schema():
    connection = psycopg2.connect(
        dbname='qa',
        user='user',
        password='password',
        host='localhost'
    )
    cursor = connection.cursor()

    try:
        # Add lastdate column to employees table
        cursor.execute("""
        ALTER TABLE qa.employees
        ADD COLUMN lastdate DATE DEFAULT CURRENT_DATE;
        """)

        # Add categoryGroup column to customers table
        cursor.execute("""
        ALTER TABLE qa.customers
        ADD COLUMN categorygroup VARCHAR DEFAULT 'Uncategorized';
        """)

        # Commit changes
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    update_schema()
