import os
import re
import shutil


def modify_html_files(folder_path):
    # Create the JsAddedFiles directory if it doesn't exist
    js_folder_path = os.path.join(folder_path, "JsAddedFiles")
    os.makedirs(js_folder_path, exist_ok=True)

    # Iterate through all HTML files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".html"):
            file_path = os.path.join(folder_path, file_name)
            js_file_path = os.path.join(js_folder_path, f"{file_name}CSP.js")
            function_names = modify_html_file(file_path, js_file_path)

            print(f"Processed: {file_name}")

    print("Processing complete!")


def modify_html_file(file_path, js_file_path):
    # Read the HTML file content
    with open(file_path, "r") as html_file:
        html_content = html_file.read()

    # Find lines with onclick attributes and extract function names
    onclick_lines = re.findall(r'<[^<>]*onclick="([^"]*)"[^<>]*>', html_content)
    function_names = []

    # Generate modified lines and function names
    modified_lines = []
    for line in onclick_lines:
        onclick_attr = line.strip()
        function_name = onclick_attr.strip("()")
        function_names.append(function_name)

        # Generate the modified line
        modified_line = f'<button type="button" id="{function_name}BNT" class="btn optionsbtn left btn-secondary">>Add to Database</button>'
        modified_lines.append(modified_line)

    # Insert the modified lines below the existing onclick lines
    modified_content = re.sub(r'<[^<>]*onclick="[^"]*"[^<>]*>', lambda m: f"{m.group(0)}\n{modified_lines.pop(0)}", html_content)

    # Write the modified content back to the HTML file
    with open(file_path, "w") as html_file:
        html_file.write(modified_content)

    # Create the JS file with event listeners
    with open(js_file_path, "w") as js_file:
        for function_name in function_names:
            js_line = f'document.getElementById("{function_name}BNT").addEventListener("click", {function_name});\n'
            js_file.write(js_line)

    return function_names


# Get the folder path from the user
folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval' '\\'

# Modify HTML files and create JS files
modify_html_files(folder_path)





