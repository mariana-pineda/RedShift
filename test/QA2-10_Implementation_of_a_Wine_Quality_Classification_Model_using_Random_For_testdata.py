import random
import pandas as pd

# Happy path test data: Valid, expected scenarios
# These records represent typical, valid inputs for the wine quality dataset.
happy_path_data = [
    # Valid record with average values
    {"fixed_acidity": 7.0, "volatile_acidity": 0.27, "citric_acid": 0.36, "residual_sugar": 20.7, "chlorides": 0.045, "free_sulfur_dioxide": 45, "total_sulfur_dioxide": 170, "density": 1.001, "pH": 3.0, "sulphates": 0.45, "alcohol": 8.8, "quality": 6},
    # Valid record with high quality
    {"fixed_acidity": 6.6, "volatile_acidity": 0.16, "citric_acid": 0.4, "residual_sugar": 1.5, "chlorides": 0.044, "free_sulfur_dioxide": 48, "total_sulfur_dioxide": 143, "density": 0.9912, "pH": 3.54, "sulphates": 0.52, "alcohol": 12.4, "quality": 7},
    # Valid record with low quality
    {"fixed_acidity": 5.5, "volatile_acidity": 0.485, "citric_acid": 0.0, "residual_sugar": 1.5, "chlorides": 0.065, "free_sulfur_dioxide": 8, "total_sulfur_dioxide": 103, "density": 0.994, "pH": 3.63, "sulphates": 0.4, "alcohol": 9.7, "quality": 4},
]

# Edge case test data: Boundary conditions
# These records test the boundaries of the dataset's constraints.
edge_case_data = [
    # Minimum boundary for fixed acidity
    {"fixed_acidity": 3.8, "volatile_acidity": 0.27, "citric_acid": 0.36, "residual_sugar": 20.7, "chlorides": 0.045, "free_sulfur_dioxide": 45, "total_sulfur_dioxide": 170, "density": 1.001, "pH": 3.0, "sulphates": 0.45, "alcohol": 8.8, "quality": 6},
    # Maximum boundary for alcohol
    {"fixed_acidity": 7.0, "volatile_acidity": 0.27, "citric_acid": 0.36, "residual_sugar": 20.7, "chlorides": 0.045, "free_sulfur_dioxide": 45, "total_sulfur_dioxide": 170, "density": 1.001, "pH": 3.0, "sulphates": 0.45, "alcohol": 14.9, "quality": 6},
]

# Error case test data: Invalid inputs
# These records include invalid inputs to test error handling.
error_case_data = [
    # Negative value for fixed acidity
    {"fixed_acidity": -1.0, "volatile_acidity": 0.27, "citric_acid": 0.36, "residual_sugar": 20.7, "chlorides": 0.045, "free_sulfur_dioxide": 45, "total_sulfur_dioxide": 170, "density": 1.001, "pH": 3.0, "sulphates": 0.45, "alcohol": 8.8, "quality": 6},
    # String value for alcohol
    {"fixed_acidity": 7.0, "volatile_acidity": 0.27, "citric_acid": 0.36, "residual_sugar": 20.7, "chlorides": 0.045, "free_sulfur_dioxide": 45, "total_sulfur_dioxide": 170, "density": 1.001, "pH": 3.0, "sulphates": 0.45, "alcohol": "high", "quality": 6},
]

# Special character and format test data
# These records include special characters and unusual formats.
special_character_data = [
    # Special characters in pH
    {"fixed_acidity": 7.0, "volatile_acidity": 0.27, "citric_acid": 0.36, "residual_sugar": 20.7, "chlorides": 0.045, "free_sulfur_dioxide": 45, "total_sulfur_dioxide": 170, "density": 1.001, "pH": "3.0*", "sulphates": 0.45, "alcohol": 8.8, "quality": 6},
    # Unusual format for sulphates
    {"fixed_acidity": 7.0, "volatile_acidity": 0.27, "citric_acid": 0.36, "residual_sugar": 20.7, "chlorides": 0.045, "free_sulfur_dioxide": 45, "total_sulfur_dioxide": 170, "density": 1.001, "pH": 3.0, "sulphates": "0.45%", "alcohol": 8.8, "quality": 6},
]

# Combine all test data into a single list
test_data = happy_path_data + edge_case_data + error_case_data + special_character_data

# Convert test data to a DataFrame
test_df = pd.DataFrame(test_data)

# Display the test data
print(test_df)


This code generates a set of test data for a wine quality dataset, covering happy path scenarios, edge cases, error cases, and special character/format cases. Each section is commented to explain the purpose of the test data, and the data is structured to test various conditions and constraints.