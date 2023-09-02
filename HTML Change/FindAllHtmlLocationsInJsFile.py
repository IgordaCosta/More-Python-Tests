import os
import csv
import re

def find_div_tags(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.finditer(r'<div', content, re.IGNORECASE)
        return [match.start() for match in matches]

def process_js_files(folder_path):
    js_files = [file for file in os.listdir(folder_path) if file.endswith('.js')]
    
    csv_data = []
    
    for js_file in js_files:
        file_path = os.path.join(folder_path, js_file)
        div_locations = find_div_tags(file_path)
        csv_data.append([js_file, div_locations[0] if div_locations else 'N/A'])
    
    return csv_data

def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['JavaScript File', 'First <div> Location'])
        writer.writerows(data)

# Usage example
folder_path = 'path/to/js/folder'
output_csv_path = 'output.csv'

csv_data = process_js_files(folder_path)
write_csv(output_csv_path, csv_data)
