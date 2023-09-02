import os

def process_line(line):
    line = line.strip()
    if "<script>" in line and "</script>" in line and "DragnDrop2" in line:
        return ""
    elif "DragnDrop2" in line:
        return "<!-- " + line + " -->"
    else:
        return line

def block_or_delete_lines_with_keywords(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    html_files = [file for file in files if file.endswith('.html')]

    # Iterate over each HTML file
    for html_file in html_files:
        file_path = os.path.join(folder_path, html_file)

        # Read the file contents
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Process each line and filter out lines
        modified_lines = [process_line(line) for line in lines]

        # Write the modified lines back to the file
        with open(file_path, 'w') as f:
            f.write('\n'.join(modified_lines))

    print("Processing complete.")

# Provide the folder path where your HTML files are located
folder_path = '/path/to/html/files/folder'
block_or_delete_lines_with_keywords(folder_path)
