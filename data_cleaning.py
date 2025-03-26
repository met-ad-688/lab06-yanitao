import pandas as pd
import os

input_file = 'lightcast_job_postings.csv'
output_file = '_output/lightcast_cleaned.csv'
os.makedirs('_output', exist_ok=True)

df = pd.read_csv(input_file, low_memory=False)

# Drop completely empty columns
df.dropna(axis=1, how='all', inplace=True)

# Drop rows with essential missing values
df.dropna(subset=['TITLE_NAME', 'SALARY_FROM', 'SALARY_TO'], inplace=True)

# Remove rows with zero salary
df = df[(df['SALARY_FROM'] > 0) & (df['SALARY_TO'] > 0)]

# Convert dates
date_columns = ['POSTED', 'EXPIRED', 'LAST_UPDATED_DATE']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Convert numerical columns
num_columns = ['SALARY_FROM', 'SALARY_TO', 'MIN_YEARS_EXPERIENCE']
for col in num_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Optional: Fill missing experience years with 0
df['MIN_YEARS_EXPERIENCE'] = df['MIN_YEARS_EXPERIENCE'].fillna(0)

# Calculate average salary
df['AVERAGE_SALARY'] = (df['SALARY_FROM'] + df['SALARY_TO']) / 2

# Save cleaned data
df.to_csv(output_file, index=False)
print("Cleaned data saved to _output/lightcast_cleaned.csv")
