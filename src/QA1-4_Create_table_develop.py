from sqlalchemy import create_engine, MetaData, Table, Column, Date, String

# Connect to the database
engine = create_engine('sqlite:///mydatabase.db')
metadata = MetaData(bind=engine)

# Reflect existing tables
employees = Table('employees', metadata, autoload_with=engine)
customers = Table('customers', metadata, autoload_with=engine)

# Add lastdate column to employees table
if 'lastdate' not in [col.name for col in employees.columns]:
    with engine.connect() as conn:
        conn.execute('ALTER TABLE employees ADD COLUMN lastdate DATE DEFAULT "2023-01-01"')

# Add categoryGroup column to customers table
if 'categoryGroup' not in [col.name for col in customers.columns]:
    with engine.connect() as conn:
        conn.execute('ALTER TABLE customers ADD COLUMN categoryGroup STRING DEFAULT "Uncategorized"')
