import os


def add_csp_to_html_files(folder_path):
    # Iterate through all HTML files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".html"):
            file_path = os.path.join(folder_path, file_name)
            modified_content = add_csp_to_html_file(file_path)

            # Write the modified content back to the HTML file
            with open(file_path, "w") as html_file:
                html_file.write(modified_content)

            print(f"Processed: {file_name}")

    print("Processing complete!")


def add_csp_to_html_file(file_path):
    # Read the HTML file content
    with open(file_path, "r") as html_file:
        html_content = html_file.read()

    # Find the position to insert the CSP meta tag
    head_index = html_content.find("<head>") + len("<head>")

    # Construct the CSP meta tag
    csp_meta_tag = '<meta http-equiv="content-security-policy" content="script-src \'self\' ./js/">\n'

    # Insert the CSP meta tag into the HTML content
    modified_content = html_content[:head_index] + csp_meta_tag + html_content[head_index:]

    return modified_content


# Get the folder path from the user
folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval' '\\'

# Add CSP to HTML files in the folder
add_csp_to_html_files(folder_path)
