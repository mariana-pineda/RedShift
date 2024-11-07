import random
import datetime

# Function to generate random past dates for "lastdate" column
def generate_random_lastdate():
    # Random days between 1 and 365 to go back in past
    past_days = random.randint(1, 365)
    return (datetime.datetime.now() - datetime.timedelta(days=past_days)).strftime('%Y-%m-%d %H:%M:%S')

# Function to generate random category group for "categoryGroup" column
def generate_random_category_group():
    category_groups = ['Retail', 'Wholesale', 'Online', 'Corporate', 'Individual']
    # Randomly select a category group from the list
    return random.choice(category_groups)

# Generate test data for employees table
employees_test_data = []
for i in range(25):  # Generate 25 test records
    employee_record = {
        'employee_id': i + 1,
        # Validate "lastdate" column is of timestamp type and represents last working day
        'lastdate': generate_random_lastdate()
    }
    employees_test_data.append(employee_record)

# Generate test data for customers table
customers_test_data = []
for i in range(25):  # Generate 25 test records
    customer_record = {
        'customer_id': i + 1,
        # Validate "categoryGroup" column is of string type and represents grouping category
        'categoryGroup': generate_random_category_group()
    }
    customers_test_data.append(customer_record)

# Print generated test data
print("Employees Test Data:")
for data in employees_test_data:
    print(data)

print("\nCustomers Test Data:")
for data in customers_test_data:
    print(data)
