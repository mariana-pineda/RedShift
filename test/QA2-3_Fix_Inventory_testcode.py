import pytest

# Validation functions
def validate_lastdate_column(employees_data):
    for employee in employees_data:
        assert "LastDate" in employee, "LastDate column is missing in employees data."
        assert isinstance(employee["LastDate"], datetime.date), "LastDate should be of type datetime.date."

def validate_category_group_column(customers_data):
    for customer in customers_data:
        assert "CategoryGroup" in customer, "CategoryGroup column is missing in customers data."
        assert isinstance(customer["CategoryGroup"], str), "CategoryGroup should be of type str."
        assert customer["CategoryGroup"] in ["Retail", "Wholesale", "Online", "Direct"], "CategoryGroup value is not valid."

# Test cases
def test_employees_lastdate_column():
    employees_data = [
        {
            "EmployeeID": 1,
            "LastDate": datetime.date(2023, 1, 1),  # Example valid date
        },
        # Add more test cases as needed
    ]
    validate_lastdate_column(employees_data)

def test_customers_category_group_column():
    customers_data = [
        {
            "CustomerID": "C001",
            "CategoryGroup": "Retail",  # Example valid category
        },
        # Add more test cases as needed
    ]
    validate_category_group_column(customers_data)

if __name__ == "__main__":
    pytest.main()
