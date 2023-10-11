import pandas as pd
import numpy as np
#---------read the attribute names first------------------
with open('Names.txt', 'r') as file:
    attributes = file.readlines()
columnNames = [line.split()[-2] for line in attributes if line.startswith('@attribute')]        #we are only interested in the name itself, delete everything else

#---------read the data-----------------
dataset = pd.read_csv('communities.data', header=None)
dataset.columns = columnNames
#dataset.to_csv('DatasetWithHeaders', index=False)

datasetWithHeaders = pd.read_csv('DatasetWithHeaders')

# Calculate Minimum (Min)
population_min = datasetWithHeaders['population'].min()

# Calculate Maximum (Max)
population_max = datasetWithHeaders['population'].max()

# Calculate Mean
population_mean = datasetWithHeaders['population'].mean()

# Calculate Standard Deviation (SD)
population_std = datasetWithHeaders['population'].std()

# Calculate Median
population_median = datasetWithHeaders['population'].median()

# Calculate Mode
population_mode = datasetWithHeaders['population'].mode().values[0]  # Mode may have multiple values, we take the first one

# Count Missing Values
missing_values = datasetWithHeaders['population'].isnull().sum()

# Print the results
print(f"Minimum (Min): {population_min}")
print(f"Maximum (Max): {population_max}")
print(f"Mean: {population_mean}")
print(f"Standard Deviation (SD): {population_std}")
print(f"Median: {population_median}")
print(f"Mode: {population_mode}")
print(f"Missing Values: {missing_values}")



