import pandas as pd

# Ensure openpyxl is installed: pip install openpyxl

# List of male names from various regions
male_names = [
    "Aapo", "Mikko", "Juhani", "Matti", "Timo", "Antti",  # Finnish names
    "John", "Michael", "David", "James", "Robert",  # American names
    "Oliver", "George", "Harry", "Jack", "Charlie",  # British names
    "Liam", "Noah", "Lucas", "Ethan", "Mason",  # Australian names
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun"  # Indian names
]

file_path = 'malenames.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Check if the 'Name' column exists in the DataFrame
if 'Name' not in df.columns:
    print("Error: 'Name' column not found in the Excel file.")
else:
    # Store the row numbers of rows with male names
    male_name_rows = df[df['Name'].isin(male_names)].index

    # Delete rows with male names
    df.drop(male_name_rows, inplace=True)

    # Save the modified DataFrame back to the Excel file using openpyxl
    modified_file_path = 'modified_' + file_path
    df.to_excel(modified_file_path, index=False, engine='openpyxl')

    # Output the row numbers with male names
    print("Rows with male names:", list(male_name_rows))