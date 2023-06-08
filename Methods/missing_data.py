import pandas as pd
students = pd.read_excel("Raw_Datasets\students.xlsx")

# Create a mask to see null values with boolean
mask = students['State'].isnull()
print(mask)

# Get rows with mask (only null values)
filtered_rows = students[mask]
print(filtered_rows)

# Create a mask with logic
mask_logic = (students['City'] == 'Granger') & (students['State'] == 'IN')
print(mask_logic)

# Filter by the logic mask
  # you can also use: filtered_with_logic = students[mask_logic]
filtered_with_logic = students.loc[mask_logic, :]
print(filtered_with_logic)


# Remove every row with null values in it
students_every_row_null = students.dropna()
print(students_every_row_null)

# Remove rows with null values in specific columns
students_specific_column_row_null = students.dropna(subset=['State', 'Zip'], how= 'all')
print(students_specific_column_row_null)

# Remove columns that has rows with missing data
students_dropped_columns = students.dropna(axis=1)
print(students_dropped_columns)

# Remove columns that only have a specific number of null values:
students_dropped_columns_with_minimum_nulls = students.dropna(axis=1, thresh=10)
print(students_dropped_columns_with_minimum_nulls)

# Fill null values of some column with specific value:
students_filled_gender = students.fillna({'Gender':'Female'})
print(students_filled_gender)

# Fill null values with mean: Gets the column mean
students_age_mean = students = students.fillna({'Age':students['Age'].mean()})

# Fill null values with median: Gets the column median:
students_age_median = students = students.fillna({'Age':students['Age'].median()})