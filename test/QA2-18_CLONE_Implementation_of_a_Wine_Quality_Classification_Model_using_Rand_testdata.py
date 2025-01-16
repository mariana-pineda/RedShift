import pandas as pd
import numpy as np

# Happy Path Test Data
# Valid scenarios where all data points are within expected ranges
happy_path_data = pd.DataFrame({
    'fixed_acidity': [7.0, 6.3, 8.1, 7.2, 6.2],
    'volatile_acidity': [0.27, 0.3, 0.28, 0.23, 0.32],
    'citric_acid': [0.36, 0.34, 0.4, 0.32, 0.16],
    'residual_sugar': [20.7, 1.6, 6.9, 8.5, 7.0],
    'chlorides': [0.045, 0.049, 0.05, 0.058, 0.045],
    'free_sulfur_dioxide': [45, 14, 30, 47, 30],
    'total_sulfur_dioxide': [170, 132, 97, 186, 136],
    'density': [1.001, 0.994, 0.9951, 0.9956, 0.9949],
    'pH': [3.0, 3.3, 3.26, 3.19, 3.18],
    'sulphates': [0.45, 0.49, 0.44, 0.4, 0.47],
    'alcohol': [8.8, 9.5, 10.1, 9.9, 9.6],
    'quality': [6, 6, 6, 6, 6]
})

# Edge Case Test Data
# Boundary conditions such as minimum and maximum values
edge_case_data = pd.DataFrame({
    'fixed_acidity': [4.6, 15.9],  # Min and max observed values
    'volatile_acidity': [0.12, 1.58],  # Min and max observed values
    'citric_acid': [0.0, 1.66],  # Min and max observed values
    'residual_sugar': [0.6, 65.8],  # Min and max observed values
    'chlorides': [0.009, 0.346],  # Min and max observed values
    'free_sulfur_dioxide': [2, 289],  # Min and max observed values
    'total_sulfur_dioxide': [9, 440],  # Min and max observed values
    'density': [0.98711, 1.03898],  # Min and max observed values
    'pH': [2.72, 3.82],  # Min and max observed values
    'sulphates': [0.22, 2.0],  # Min and max observed values
    'alcohol': [8.0, 14.2],  # Min and max observed values
    'quality': [3, 9]  # Min and max observed values
})

# Error Case Test Data
# Invalid inputs such as negative values or non-numeric types
error_case_data = pd.DataFrame({
    'fixed_acidity': [-1.0, 'invalid'],  # Negative and non-numeric
    'volatile_acidity': [-0.5, 'invalid'],  # Negative and non-numeric
    'citric_acid': [-0.1, 'invalid'],  # Negative and non-numeric
    'residual_sugar': [-2.0, 'invalid'],  # Negative and non-numeric
    'chlorides': [-0.01, 'invalid'],  # Negative and non-numeric
    'free_sulfur_dioxide': [-5, 'invalid'],  # Negative and non-numeric
    'total_sulfur_dioxide': [-10, 'invalid'],  # Negative and non-numeric
    'density': [-0.99, 'invalid'],  # Negative and non-numeric
    'pH': [-3.0, 'invalid'],  # Negative and non-numeric
    'sulphates': [-0.5, 'invalid'],  # Negative and non-numeric
    'alcohol': [-9.0, 'invalid'],  # Negative and non-numeric
    'quality': [-1, 'invalid']  # Negative and non-numeric
})

# Special Character and Format Test Data
# Inputs with special characters or unusual formats
special_character_data = pd.DataFrame({
    'fixed_acidity': ['7.0%', '6.3*'],
    'volatile_acidity': ['0.27$', '0.3#'],
    'citric_acid': ['0.36@', '0.34!'],
    'residual_sugar': ['20.7^', '1.6&'],
    'chlorides': ['0.045(', '0.049)'],
    'free_sulfur_dioxide': ['45_', '14+'],
    'total_sulfur_dioxide': ['170=', '132~'],
    'density': ['1.001{', '0.994}'],
    'pH': ['3.0[', '3.3]'],
    'sulphates': ['0.45|', '0.49\\'],
    'alcohol': ['8.8:', '9.5;'],
    'quality': ['6<', '6>']
})

# Combine all test data into a single DataFrame
test_data = pd.concat([happy_path_data, edge_case_data, error_case_data, special_character_data], ignore_index=True)

# Output the test data
print(test_data)

