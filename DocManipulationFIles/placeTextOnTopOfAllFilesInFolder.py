import os

def add_require_to_files_in_folder(folder_path, require_statement):
    # List all files in the folder
    file_list = os.listdir(folder_path)
    
    # Loop through each file
    for filename in file_list:
        if filename.endswith(".js"):  # Assuming the files are JavaScript files
            file_path = os.path.join(folder_path, filename)
            
            # Read the content of the file
            with open(file_path, 'r') as file:
                file_content = file.read()
            
            # Add the require statement to the beginning of the file content
            updated_content = f"{require_statement}\n{file_content}"
            
            # Write the updated content back to the file
            with open(file_path, 'w') as file:
                file.write(updated_content)

# Usage example:
folder_path = r"C:\Users\Tigereye\Desktop\js"  # Replace with the actual folder path
require_statement = '''try{
  const { requireModule } = require("./index"); // Require the function from the central module
  
  // Create a dynamic require function
  let dynamicRequire = requireModule();
  }catch{}'''
add_require_to_files_in_folder(folder_path, require_statement)
