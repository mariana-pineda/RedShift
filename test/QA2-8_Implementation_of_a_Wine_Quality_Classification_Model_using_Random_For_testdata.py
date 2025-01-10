import pandas as pd
import numpy as np

# Generate synthetic data for testing
np.random.seed(42)

# Number of records to generate
num_records = 30

# Generate random data for features
fixed_acidity = np.random.uniform(4, 15, num_records)
volatile_acidity = np.random.uniform(0.1, 1.5, num_records)
citric_acid = np.random.uniform(0, 1, num_records)
residual_sugar = np.random.uniform(0.5, 15, num_records)
chlorides = np.random.uniform(0.01, 0.2, num_records)
free_sulfur_dioxide = np.random.uniform(1, 72, num_records)
total_sulfur_dioxide = np.random.uniform(6, 289, num_records)
density = np.random.uniform(0.990, 1.004, num_records)
pH = np.random.uniform(2.8, 4, num_records)
sulphates = np.random.uniform(0.2, 1.2, num_records)
alcohol = np.random.uniform(8, 14, num_records)

# Generate random quality scores between 3 and 9
quality = np.random.randint(3, 10, num_records)

# Convert quality to binary high_quality based on threshold >6
high_quality = quality > 6  # Condition: Convert 'quality' to 'high_quality'

# Create a DataFrame
test_data = pd.DataFrame({
    'fixed_acidity': fixed_acidity,
    'volatile_acidity': volatile_acidity,
    'citric_acid': citric_acid,
    'residual_sugar': residual_sugar,
    'chlorides': chlorides,
    'free_sulfur_dioxide': free_sulfur_dioxide,
    'total_sulfur_dioxide': total_sulfur_dioxide,
    'density': density,
    'pH': pH,
    'sulphates': sulphates,
    'alcohol': alcohol,
    'quality': quality,
    'high_quality': high_quality
})

# Display the generated test data
print(test_data)
