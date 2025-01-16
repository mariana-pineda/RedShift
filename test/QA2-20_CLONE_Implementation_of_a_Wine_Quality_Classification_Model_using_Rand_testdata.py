import random
import pandas as pd

# Define the number of records for each test data category
happy_path_count = 10
edge_case_count = 5
error_case_count = 5
special_char_count = 5

# Define the threshold for high quality
quality_threshold = 7

# Happy Path Test Data
# Valid scenarios with expected inputs
happy_path_data = [
    {
        'fixed_acidity': random.uniform(6.0, 9.0),
        'volatile_acidity': random.uniform(0.2, 0.5),
        'citric_acid': random.uniform(0.2, 0.4),
        'residual_sugar': random.uniform(1.0, 5.0),
        'chlorides': random.uniform(0.03, 0.06),
        'free_sulfur_dioxide': random.uniform(15, 30),
        'total_sulfur_dioxide': random.uniform(100, 150),
        'density': random.uniform(0.990, 1.000),
        'pH': random.uniform(3.0, 3.5),
        'sulphates': random.uniform(0.4, 0.6),
        'alcohol': random.uniform(9.0, 12.0),
        'quality': random.randint(quality_threshold, 10)  # High quality
    }
    for _ in range(happy_path_count)
]

# Edge Case Test Data
# Boundary conditions
edge_case_data = [
    {
        'fixed_acidity': 6.0,  # Lower boundary
        'volatile_acidity': 0.2,  # Lower boundary
        'citric_acid': 0.2,  # Lower boundary
        'residual_sugar': 1.0,  # Lower boundary
        'chlorides': 0.03,  # Lower boundary
        'free_sulfur_dioxide': 15,  # Lower boundary
        'total_sulfur_dioxide': 100,  # Lower boundary
        'density': 0.990,  # Lower boundary
        'pH': 3.0,  # Lower boundary
        'sulphates': 0.4,  # Lower boundary
        'alcohol': 9.0,  # Lower boundary
        'quality': quality_threshold  # Boundary for high quality
    },
    {
        'fixed_acidity': 9.0,  # Upper boundary
        'volatile_acidity': 0.5,  # Upper boundary
        'citric_acid': 0.4,  # Upper boundary
        'residual_sugar': 5.0,  # Upper boundary
        'chlorides': 0.06,  # Upper boundary
        'free_sulfur_dioxide': 30,  # Upper boundary
        'total_sulfur_dioxide': 150,  # Upper boundary
        'density': 1.000,  # Upper boundary
        'pH': 3.5,  # Upper boundary
        'sulphates': 0.6,  # Upper boundary
        'alcohol': 12.0,  # Upper boundary
        'quality': quality_threshold - 1  # Just below high quality
    }
] + [
    {
        'fixed_acidity': random.uniform(6.0, 9.0),
        'volatile_acidity': random.uniform(0.2, 0.5),
        'citric_acid': random.uniform(0.2, 0.4),
        'residual_sugar': random.uniform(1.0, 5.0),
        'chlorides': random.uniform(0.03, 0.06),
        'free_sulfur_dioxide': random.uniform(15, 30),
        'total_sulfur_dioxide': random.uniform(100, 150),
        'density': random.uniform(0.990, 1.000),
        'pH': random.uniform(3.0, 3.5),
        'sulphates': random.uniform(0.4, 0.6),
        'alcohol': random.uniform(9.0, 12.0),
        'quality': quality_threshold  # Boundary for high quality
    }
    for _ in range(edge_case_count - 2)
]

# Error Case Test Data
# Invalid inputs
error_case_data = [
    {
        'fixed_acidity': -1.0,  # Invalid negative value
        'volatile_acidity': 0.5,
        'citric_acid': 0.3,
        'residual_sugar': 3.0,
        'chlorides': 0.05,
        'free_sulfur_dioxide': 20,
        'total_sulfur_dioxide': 120,
        'density': 0.995,
        'pH': 3.3,
        'sulphates': 0.5,
        'alcohol': 10.0,
        'quality': 5
    },
    {
        'fixed_acidity': 7.0,
        'volatile_acidity': 0.5,
        'citric_acid': 0.3,
        'residual_sugar': 3.0,
        'chlorides': 0.05,
        'free_sulfur_dioxide': 20,
        'total_sulfur_dioxide': 120,
        'density': 0.995,
        'pH': 3.3,
        'sulphates': 0.5,
        'alcohol': 10.0,
        'quality': 11  # Invalid quality value
    }
] + [
    {
        'fixed_acidity': random.uniform(6.0, 9.0),
        'volatile_acidity': random.uniform(0.2, 0.5),
        'citric_acid': random.uniform(0.2, 0.4),
        'residual_sugar': random.uniform(1.0, 5.0),
        'chlorides': random.uniform(0.03, 0.06),
        'free_sulfur_dioxide': random.uniform(15, 30),
        'total_sulfur_dioxide': random.uniform(100, 150),
        'density': random.uniform(0.990, 1.000),
        'pH': random.uniform(3.0, 3.5),
        'sulphates': random.uniform(0.4, 0.6),
        'alcohol': random.uniform(9.0, 12.0),
        'quality': random.choice([-1, 11])  # Invalid quality values
    }
    for _ in range(error_case_count - 2)
]

# Special Character and Format Test Data
# Testing special characters and formats
special_char_data = [
    {
        'fixed_acidity': '7.0',  # String instead of float
        'volatile_acidity': '0.3',
        'citric_acid': '0.3',
        'residual_sugar': '3.0',
        'chlorides': '0.05',
        'free_sulfur_dioxide': '20',
        'total_sulfur_dioxide': '120',
        'density': '0.995',
        'pH': '3.3',
        'sulphates': '0.5',
        'alcohol': '10.0',
        'quality': '5'
    },
    {
        'fixed_acidity': '7,0',  # Comma instead of dot
        'volatile_acidity': '0,3',
        'citric_acid': '0,3',
        'residual_sugar': '3,0',
        'chlorides': '0,05',
        'free_sulfur_dioxide': '20',
        'total_sulfur_dioxide': '120',
        'density': '0,995',
        'pH': '3,3',
        'sulphates': '0,5',
        'alcohol': '10,0',
        'quality': '5'
    }
] + [
    {
        'fixed_acidity': random.uniform(6.0, 9.0),
        'volatile_acidity': random.uniform(0.2, 0.5),
        'citric_acid': random.uniform(0.2, 0.4),
        'residual_sugar': random.uniform(1.0, 5.0),
        'chlorides': random.uniform(0.03, 0.06),
        'free_sulfur_dioxide': random.uniform(15, 30),
        'total_sulfur_dioxide': random.uniform(100, 150),
        'density': random.uniform(0.990, 1.000),
        'pH': random.uniform(3.0, 3.5),
        'sulphates': random.uniform(0.4, 0.6),
        'alcohol': random.uniform(9.0, 12.0),
        'quality': random.choice(['5', '6'])  # String quality
    }
    for _ in range(special_char_count - 2)
]

# Combine all test data
test_data = happy_path_data + edge_case_data + error_case_data + special_char_data

# Convert to DataFrame for easy manipulation
test_data_df = pd.DataFrame(test_data)

# Output the test data
print(test_data_df)

