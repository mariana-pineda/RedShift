from sqlalchemy import create_engine, MetaData, Table, Column, Date, String

# Connect to the database
engine = create_engine('sqlite:///your_database.db')
metadata = MetaData(bind=engine)

# Reflect the existing employees table
employees = Table('employees', metadata, autoload_with=engine)

# Add lastdate column to employees table
with engine.connect() as conn:
    conn.execute('ALTER TABLE employees ADD COLUMN lastdate DATE DEFAULT "2023-01-01"')

# Reflect the existing customers table
customers = Table('customers', metadata, autoload_with=engine)

# Add categoryGroup column to customers table
with engine.connect() as conn:
    conn.execute('ALTER TABLE customers ADD COLUMN categoryGroup STRING DEFAULT "Uncategorized"')
