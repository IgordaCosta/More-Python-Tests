import os
import re

def remove_script_from_files(folder_path):
    script_pattern = r"<script>[\s\S]*?</script>"
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith('.html') or file_path.endswith('.htm'):
                with open(file_path, 'r') as file:
                    content = file.read()
                
                # Remove the <script> block from the file content
                modified_content = re.sub(script_pattern, '', content)
                
                # Write the modified content back to the file
                with open(file_path, 'w') as file:
                    file.write(modified_content)

# Usage example
folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval\js' '\\'
remove_script_from_files(folder_path)
