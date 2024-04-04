#!/usr/bin/env python
#
# Required packages: pandas, openpyxl
#
#     pip install pandas openpyxl
#
# Download XLSX file from GS1 and rename to 'gs1-products.xlsx'.
# Run this script to extract data from specific columns and write to text files.
#
import pandas as pd

# Load the Excel file
file_path = 'gs1-products.xlsx'

# Define the sheet name and column indices for each text file
# Assuming 'E' column is the 5th column, hence index 4 (zero-based indexing)
data_columns = {
    'gpc.txt': ('Reference Data', 4),
    'targetMarketCountry.txt': ('Reference Data', 1),  # Adjust based on actual Excel layout
    'language.txt': ('Reference Data', 2),  # Adjust based on actual Excel layout
    'measurementUnit.txt': ('Reference Data', 3),  # Adjust based on actual Excel layout
    'packagingType.txt': ('Reference Data', 0),  # Assuming 'packagingType' is in column 'A'
}

# Function to read data and write to a text file
def write_data_to_text(sheet_name, column_index, file_name):
    # Load specific sheet and column
    df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=[column_index], engine='openpyxl')
    
    # Write data to text file
    with open(file_name, 'w', encoding='utf-8') as file:
        for value in df.iloc[:, 0].dropna().values:
            file.write(str(value) + '\n')

# Process each specified column
for file_name, (sheet, column) in data_columns.items():
    write_data_to_text(sheet, column, file_name)

print('Text files have been created.')
