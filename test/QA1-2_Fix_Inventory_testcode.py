import datetime

# Mock database querying functions
def get_employees_schema():
    return {
        "columns": [
            {"name": "EmployeeID", "type": "int"},
            {"name": "LastName", "type": "string"},
            {"name": "FirstName", "type": "string"},
            {"name": "Title", "type": "string"},
            {"name": "TitleOfCourtesy", "type": "string"},
            {"name": "BirthDate", "type": "timestamp"},
            {"name": "HireDate", "type": "timestamp"},
            {"name": "Address", "type": "string"},
            {"name": "City", "type": "string"},
            {"name": "Region", "type": "string"},
            {"name": "PostalCode", "type": "string"},
            {"name": "Country", "type": "string"},
            {"name": "HomePhone", "type": "string"},
            {"name": "Extension", "type": "string"},
            {"name": "Photo", "type": "binary"},
            {"name": "Notes", "type": "string"},
            {"name": "ReportsTo", "type": "int"},
            {"name": "PhotoPath", "type": "string"},
            {"name": "lastdate", "type": "date", "default": datetime.date.today()},
        ]
    }

def get_customers_schema():
    return {
        "columns": [
            {"name": "customer_id", "type": "int"},
            {"name": "categoryGroup", "type": "string", "allowed_values": ["Premium", "Standard", "Basic"]},
        ]
    }

# Test for employees table
def test_employees_lastdate():
    schema = get_employees_schema()
    lastdate_column = next((col for col in schema["columns"] if col["name"] == "lastdate"), None)
    
    assert lastdate_column is not None, "Column 'lastdate' not found in employees table"
    assert lastdate_column["type"] == "date", f"Expected 'lastdate' to be of type 'date', got {lastdate_column['type']}"
    assert lastdate_column["default"] == datetime.date.today(), "Default value for 'lastdate' is not current date"

# Test for customers table
def test_customers_categoryGroup():
    schema = get_customers_schema()
    category_group_column = next((col for col in schema["columns"] if col["name"] == "categoryGroup"), None)
    
    assert category_group_column is not None, "Column 'categoryGroup' not found in customers table"
    assert category_group_column["type"] == "string", f"Expected 'categoryGroup' to be of type 'string', got {category_group_column['type']}"
    assert set(category_group_column["allowed_values"]) == {"Premium", "Standard", "Basic"}, "Allowed values for 'categoryGroup' do not match expected values"

# Run tests
test_employees_lastdate()
test_customers_categoryGroup()

print("All tests passed.")
