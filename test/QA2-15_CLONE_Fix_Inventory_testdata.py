import random
import datetime

# Happy Path Test Data
# Valid scenarios for employees with default lastdate
happy_path_employees = [
    {
        "EmployeeID": i,
        "LastName": f"LastName{i}",
        "FirstName": f"FirstName{i}",
        "Title": "Manager",
        "TitleOfCourtesy": "Mr.",
        "BirthDate": datetime.datetime(1980, 1, 1),
        "HireDate": datetime.datetime(2010, 1, 1),
        "Address": f"Address {i}",
        "City": "CityName",
        "Region": "RegionName",
        "PostalCode": "12345",
        "Country": "CountryName",
        "HomePhone": "123-456-7890",
        "Extension": "1234",
        "Photo": None,
        "Notes": "Notes about employee",
        "ReportsTo": None,
        "PhotoPath": "http://example.com/photo.jpg",
        "LastDate": datetime.date.today()  # Default value
    }
    for i in range(1, 6)
]

# Valid scenarios for customers with default categoryGroup
happy_path_customers = [
    {
        "CustomerID": f"CUST{i:05}",
        "CompanyName": f"CompanyName{i}",
        "ContactName": f"ContactName{i}",
        "ContactTitle": "CEO",
        "Address": f"Address {i}",
        "City": "CityName",
        "Region": "RegionName",
        "PostalCode": "12345",
        "Country": "CountryName",
        "Phone": "123-456-7890",
        "Fax": "123-456-7890",
        "CategoryGroup": "Uncategorized"  # Default value
    }
    for i in range(1, 6)
]

# Edge Case Test Data
# Boundary conditions for employees
edge_case_employees = [
    {
        "EmployeeID": 0,  # Minimum possible ID
        "LastName": "EdgeLastName",
        "FirstName": "EdgeFirstName",
        "Title": "Intern",
        "TitleOfCourtesy": "Ms.",
        "BirthDate": datetime.datetime(2000, 1, 1),
        "HireDate": datetime.datetime(2020, 1, 1),
        "Address": "Edge Address",
        "City": "Edge City",
        "Region": "Edge Region",
        "PostalCode": "00000",
        "Country": "Edge Country",
        "HomePhone": "000-000-0000",
        "Extension": "0000",
        "Photo": None,
        "Notes": "Edge case notes",
        "ReportsTo": None,
        "PhotoPath": "http://example.com/edgephoto.jpg",
        "LastDate": datetime.date.today()  # Default value
    }
]

# Boundary conditions for customers
edge_case_customers = [
    {
        "CustomerID": "CUST00000",  # Minimum possible ID
        "CompanyName": "EdgeCompanyName",
        "ContactName": "EdgeContactName",
        "ContactTitle": "Intern",
        "Address": "Edge Address",
        "City": "Edge City",
        "Region": "Edge Region",
        "PostalCode": "00000",
        "Country": "Edge Country",
        "Phone": "000-000-0000",
        "Fax": "000-000-0000",
        "CategoryGroup": "VIP"  # Valid category
    }
]

# Error Case Test Data
# Invalid inputs for employees
error_case_employees = [
    {
        "EmployeeID": -1,  # Invalid ID
        "LastName": "",  # Invalid LastName
        "FirstName": "",  # Invalid FirstName
        "Title": "InvalidTitle",
        "TitleOfCourtesy": "Invalid",
        "BirthDate": "InvalidDate",  # Invalid date format
        "HireDate": "InvalidDate",  # Invalid date format
        "Address": "",
        "City": "",
        "Region": "",
        "PostalCode": "Invalid",
        "Country": "",
        "HomePhone": "Invalid",
        "Extension": "Invalid",
        "Photo": None,
        "Notes": "",
        "ReportsTo": None,
        "PhotoPath": "",
        "LastDate": "InvalidDate"  # Invalid date format
    }
]

# Invalid inputs for customers
error_case_customers = [
    {
        "CustomerID": "",  # Invalid ID
        "CompanyName": "",
        "ContactName": "",
        "ContactTitle": "",
        "Address": "",
        "City": "",
        "Region": "",
        "PostalCode": "Invalid",
        "Country": "",
        "Phone": "Invalid",
        "Fax": "Invalid",
        "CategoryGroup": "InvalidCategory"  # Invalid category
    }
]

# Special Character and Format Test Data
# Special characters in employee names
special_char_employees = [
    {
        "EmployeeID": 999,
        "LastName": "O'Conner",
        "FirstName": "Anne-Marie",
        "Title": "Lead Developer",
        "TitleOfCourtesy": "Dr.",
        "BirthDate": datetime.datetime(1990, 1, 1),
        "HireDate": datetime.datetime(2015, 1, 1),
        "Address": "123 Main St.",
        "City": "New York",
        "Region": "NY",
        "PostalCode": "10001",
        "Country": "USA",
        "HomePhone": "(123) 456-7890",
        "Extension": "1234",
        "Photo": None,
        "Notes": "Special character test",
        "ReportsTo": None,
        "PhotoPath": "http://example.com/photo.jpg",
        "LastDate": datetime.date.today()  # Default value
    }
]

# Special characters in customer names
special_char_customers = [
    {
        "CustomerID": "CUST99999",
        "CompanyName": "O'Reilly Media",
        "ContactName": "Anne-Marie",
        "ContactTitle": "Editor-in-Chief",
        "Address": "123 Main St.",
        "City": "New York",
        "Region": "NY",
        "PostalCode": "10001",
        "Country": "USA",
        "Phone": "(123) 456-7890",
        "Fax": "(123) 456-7890",
        "CategoryGroup": "Regular"  # Valid category
    }
]

# Combine all test data
test_data = {
    "employees": happy_path_employees + edge_case_employees + error_case_employees + special_char_employees,
    "customers": happy_path_customers + edge_case_customers + error_case_customers + special_char_customers
}

# Print test data for verification
for category, data in test_data.items():
    print(f"Test Data for {category.capitalize()}:")
    for record in data:
        print(record)
    print("\n")
