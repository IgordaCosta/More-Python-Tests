import os
import csv

# Function to search for a string in a file
def search_string_in_file(file_path, search_string):
    with open(file_path, 'rb') as file:
        lines = file.readlines()
        for line_number, line_bytes in enumerate(lines, start=1):
            try:
                line = line_bytes.decode('utf-8')
                if search_string in line:
                    return line, line_number
            except UnicodeDecodeError:
                continue
    return None, None

# Function to search for a string in all files in a folder
def search_string_in_folder(folder_path, search_string, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['File Name', 'Line with String', 'Line Number'])

        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                line, line_number = search_string_in_file(file_path, search_string)
                if line is not None:
                    csv_writer.writerow([file_name, line.strip(), line_number])

if __name__ == "__main__":

    search_string = "GetDbData.py"  # Replace with the string you want to search for
    folder_path = r"E:\Apps\CSSAutoFormFiller7_Updated92Before3\CSSAutoFormFiller\js"   # Replace with the path to your folder
    output_csv = r"C:\Users\Tigereye\Desktop\Stuff\SearchTextLocation\search_results.csv"  # The name of the output CSV file

    search_string_in_folder(folder_path, search_string, output_csv)
    print(f"Search results saved to {output_csv}")
