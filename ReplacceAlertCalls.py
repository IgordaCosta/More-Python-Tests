import os

def remove_spaces(text):
    return text.replace(" ", "")

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Remove spaces from the original text
    old_text_no_spaces = remove_spaces(old_text)
    content_no_spaces = remove_spaces(content)

    # Perform replacement on the original text without removing spaces
    new_content = content.replace(old_text_no_spaces, new_text)

    # Perform replacement on the original text with spaces removed
    final_content = new_content.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(final_content)

def process_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(('.html', '.js')):
                file_path = os.path.join(root, file_name)
                replace_text_in_file(file_path, A1, A2)
                replace_text_in_file(file_path, B1, B2)

# Define the values of A1, A2, B1, and B2
A1 = '<div id="alert MissingData" class="positionAndLocation" >\n        <div id= "identifiersMissingAlert" class="alert alert-dismissible hidden">\n            <button type="button" class="close" data-dismiss="alert">&times;</button>'
A2 = '<div id="alert MissingData" class="positionAndLocation" >\n\t<div id= "identifiersMissingAlert" class="alert alert-warning alert-dismissible fade hidden" role="alert">\n  \t\t<button type="button" class="close" data-dismiss="alert" aria-label="Close">\n    \t\t<span aria-hidden="true">&times;</span>\n  \t\t</button>'
B1 = 'class="close"'
B2 = 'class="closebtn"'


folder_path = r'C:\Users\Tigereye\Desktop\Stuff\ReplaceAlertCalls' + '\\'

# Process the files in the folder
process_files(folder_path)

print("Replacement complete.")