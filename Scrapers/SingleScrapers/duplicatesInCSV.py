import pandas as pd

def count_duplicates_in_first_column(csv_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Check if the DataFrame is not empty
    if df.empty:
        print("The CSV file is empty.")
        return
    
    # Use the first column for checking duplicates
    first_column = df.columns[0]
    
    # Count the number of duplicate entries in the first column
    duplicate_count = df[first_column].duplicated().sum()
    
    # Get the list of duplicate entries
    duplicates = df[df[first_column].duplicated(keep=False)]
    
    print(f"Number of duplicates in the first column: {duplicate_count}")
    print("\nList of duplicate entries:")
    print(duplicates)

# Example usage
csv_file_path = 'Updated Free_Spam_Disposable - Disposable domains.csv'  # Replace with your CSV file path

count_duplicates_in_first_column(csv_file_path)
