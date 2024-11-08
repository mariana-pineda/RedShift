import random
import datetime
import string

# Generate test data for qa.employees table
def generate_employees_data(num_records):
    employees_data = []
    for i in range(num_records):
        employee = {
            'EmployeeID': i + 1,
            'LastName': ''.join(random.choices(string.ascii_uppercase, k=5)),
            'FirstName': ''.join(random.choices(string.ascii_uppercase, k=5)),
            'Title': random.choice(['Manager', 'Salesperson', 'Clerk']),
            'TitleOfCourtesy': random.choice(['Mr.', 'Ms.', 'Mrs.', 'Dr.']),
            'BirthDate': datetime.datetime(1970, 1, 1) + datetime.timedelta(days=random.randint(0, 18000)),
            'HireDate': datetime.datetime(1990, 1, 1) + datetime.timedelta(days=random.randint(0, 10000)),
            'Address': ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            'City': ''.join(random.choices(string.ascii_uppercase, k=5)),
            'Region': ''.join(random.choices(string.ascii_uppercase, k=3)),
            'PostalCode': ''.join(random.choices(string.digits, k=5)),
            'Country': random.choice(['USA', 'Canada', 'UK']),
            'HomePhone': ''.join(random.choices(string.digits, k=10)),
            'Extension': ''.join(random.choices(string.digits, k=4)),
            'Photo': bytes(random.getrandbits(8) for _ in range(10)),
            'Notes': ''.join(random.choices(string.ascii_letters + string.digits, k=20)),
            'ReportsTo': random.randint(0, num_records),
            'PhotoPath': '/images/employee' + str(i) + '.jpg',
            'lastdate': datetime.date.today().strftime('%Y-%m-%d')  # Validate default value is current date
        }
        employees_data.append(employee)
    return employees_data

# Generate test data for qa.customers table
def generate_customers_data(num_records):
    category_groups = ['Premium', 'Standard', 'Basic']
    customers_data = []
    for i in range(num_records):
        customer = {
            'CustomerID': i + 1,
            'CompanyName': ''.join(random.choices(string.ascii_uppercase, k=10)),
            'ContactName': ''.join(random.choices(string.ascii_uppercase, k=7)),
            'ContactTitle': random.choice(['Owner', 'Purchasing Manager', 'Sales Representative']),
            'Address': ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            'City': ''.join(random.choices(string.ascii_uppercase, k=5)),
            'Region': ''.join(random.choices(string.ascii_uppercase, k=3)),
            'PostalCode': ''.join(random.choices(string.digits, k=5)),
            'Country': random.choice(['USA', 'Canada', 'UK']),
            'Phone': ''.join(random.choices(string.digits, k=10)),
            'Fax': ''.join(random.choices(string.digits, k=10)),
            'categoryGroup': random.choice(category_groups)  # Validate categoryGroup accepts 'Premium', 'Standard', 'Basic'
        }
        customers_data.append(customer)
    return customers_data

# Generate 25 employee records
employees_test_data = generate_employees_data(25)
# Generate 25 customer records
customers_test_data = generate_customers_data(25)

# Output the test data (if needed for verification)
# print(employees_test_data)
# print(customers_test_data)
