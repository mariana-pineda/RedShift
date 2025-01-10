import random
from datetime import datetime, timedelta

# Generate test data for Employees table
def generate_employee_data(num_records):
    employees = []
    for i in range(num_records):
        employee = {
            "EmployeeID": i + 1,
            "LastName": f"LastName{i}",
            "FirstName": f"FirstName{i}",
            "Title": f"Title{i}",
            "TitleOfCourtesy": f"Mr./Ms. {i}",
            "BirthDate": datetime(1970, 1, 1) + timedelta(days=random.randint(0, 20000)),
            "HireDate": datetime(2000, 1, 1) + timedelta(days=random.randint(0, 8000)),
            "Address": f"Address {i}",
            "City": f"City{i}",
            "Region": f"Region{i}",
            "PostalCode": f"{random.randint(10000, 99999)}",
            "Country": f"Country{i}",
            "HomePhone": f"{random.randint(1000000000, 9999999999)}",
            "Extension": f"{random.randint(1000, 9999)}",
            "Photo": None,
            "Notes": f"Notes {i}",
            "ReportsTo": random.randint(1, num_records) if i > 0 else None,
            "PhotoPath": f"/photos/{i}.jpg",
            "LastDate": datetime.now().date()  # Validate default lastdate
        }
        employees.append(employee)
    return employees

# Generate test data for Customers table
def generate_customer_data(num_records):
    category_options = ["VIP", "Regular", "New", "Uncategorized"]
    customers = []
    for i in range(num_records):
        category = random.choice(category_options)
        customer = {
            "CustomerID": f"CUST{i:05d}",
            "CompanyName": f"CompanyName{i}",
            "ContactName": f"ContactName{i}",
            "ContactTitle": f"ContactTitle{i}",
            "Address": f"Address {i}",
            "City": f"City{i}",
            "Region": f"Region{i}",
            "PostalCode": f"{random.randint(10000, 99999)}",
            "Country": f"Country{i}",
            "Phone": f"{random.randint(1000000000, 9999999999)}",
            "Fax": f"{random.randint(1000000000, 9999999999)}",
            "CategoryGroup": category if category != "Uncategorized" else "Uncategorized"  # Validate categoryGroup
        }
        customers.append(customer)
    return customers

# Generate 20-30 records for each table
employee_data = generate_employee_data(25)
customer_data = generate_customer_data(25)

# Print the generated data
print("Employee Data:")
for emp in employee_data:
    print(emp)

print("\nCustomer Data:")
for cust in customer_data:
    print(cust)
