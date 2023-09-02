import os
import re
import csv

def find_matching_lines(folder_path):
    matches = []
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".js"):  # Change the extension if needed
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for line_number, line in enumerate(lines, start=1):
                        if not line.startswith("\\") and re.search(r'\b.py\b', line):
                            words = line.split()
                            for word in words:
                                if re.search(r'\b.py\b', word):
                                    matches.append((word, line_number, file))
    
    return matches

def save_to_csv(matches, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Word", "Line Number", "Document Name"])
        csv_writer.writerows(matches)

if __name__ == "__main__":
    folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated92\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\js' + '\\'
    output_file = r'C:\Users\Tigereye\Desktop\Stuff\LocationOfText\outputTextLocations.csv'

    
    matches = find_matching_lines(folder_path)
    save_to_csv(matches, output_file)
    print(f"Found {len(matches)} matches. Results saved in {output_file}.")
