import pandas as pd
# Load the new CSV file
file_1_path = '1.csv'
file_2_csv_path = 'Макрорегионы - Субъекты (копия) (копия).csv'

# Read the datasets
data_1 = pd.read_csv(file_1_path)
data_2 = pd.read_csv(file_2_csv_path)

# Display the first few rows of each dataframe to understand their structure
data_1.head(), data_2.head()



# Ensure the 'region' and 'Субъект' columns have the same format for merging
data_1['region'] = data_1['region'].str.strip()
data_2['Субъект'] = data_2['Субъект'].str.strip()

# Merge datasets on region name
merged_data = pd.merge(data_1, data_2[['Субъект', 'cartodb_id']], left_on='region', right_on='Субъект', how='left')

# Drop the redundant 'Субъект' column
merged_data = merged_data.drop(columns=['Субъект'])

# Save the result to a new Excel file
output_file_path = 'merged_data.xlsx'
merged_data.to_excel(output_file_path, index=False)

# Display the first few rows of the merged data to verify
merged_data.head()
