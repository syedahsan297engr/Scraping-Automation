import os
import csv

def read_txt_files(file_paths):
    """
    Read multiple txt files and combine their contents into a set to avoid duplicates.
    """
    content = set()
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            for line in file:
                content.add(line.strip())
    return content

def read_existing_txt_file(file_path):
    """
    Read the existing content of a txt file if it exists and return it as a set.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return {line.strip() for line in file}
    return set()

def write_to_txt_file(content, output_file_path):
    """
    Write the unique content to a txt file, avoiding duplicates with existing content.
    """
    existing_content = read_existing_txt_file(output_file_path)
    new_content = content - existing_content
    
    with open(output_file_path, 'a') as file:  # Append mode
        for line in new_content:
            file.write(line + '\n')

def read_csv_file(csv_file_path):
    """
    Read the csv file and return its contents as a set.
    """
    content = set()
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            content.add(row[0])  # Assuming the relevant entries are in the first column
    return content

def write_to_csv_file(entries, csv_file_path):
    """
    Append new entries to the csv file.
    """
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        for entry in entries:
            writer.writerow([entry])

def main(txt_file_paths, csv_file_path):
    output_txt_file_path = 'merged_output.txt'  # Default output txt file path
    
    # Step 1: Read and merge txt files
    txt_content = read_txt_files(txt_file_paths)
    
    # Step 2: Write merged content to a new txt file, avoiding duplicates with existing content
    write_to_txt_file(txt_content, output_txt_file_path)
    
    # Step 3: Read the csv file
    csv_content = read_csv_file(csv_file_path)
    
    # Step 4: Find entries in txt file that are not in the csv file
    unique_entries = txt_content - csv_content
    print(f"Number of entries in txt file that are not in csv file: {len(unique_entries)}")
    
    # Step 5: Append these unique entries to the csv file
    write_to_csv_file(unique_entries, csv_file_path)

if __name__ == "__main__":
    # Example usage
    txt_file_paths = ['staticDomains.txt', 'dynamicDomains.txt', 'dropdowns.txt', 'OneScrap.txt']  # replace with your txt file paths
    csv_file_path = 'Updated Free_Spam_Disposable - Disposable domains.csv'  # replace with your csv file path
    
    main(txt_file_paths, csv_file_path)
