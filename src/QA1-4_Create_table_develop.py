from sqlalchemy import create_engine, MetaData, Table, Column, Date, String

# Create an engine and metadata object
engine = create_engine('sqlite:///:memory:')
metadata = MetaData()

# Define the employees table with the new lastdate column
employees = Table('employees', metadata,
                  Column('employee_id', String, primary_key=True),
                  Column('lastdate', Date, default='2023-01-01'))

# Define the customers table with the new categoryGroup column
customers = Table('customers', metadata,
                  Column('customer_id', String, primary_key=True),
                  Column('categoryGroup', String, default='Uncategorized'))

# Create the tables in the database
metadata.create_all(engine)
