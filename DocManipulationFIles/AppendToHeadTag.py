import os

def process_and_rewrite_files_in_folder(folder_path):
    js_code = '''<script type="text/javascript">
    global.MaincurrentWorkingDirectory = __dirname
</script>
'''

    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                temp_file_path = os.path.join(root, f"temp_{filename}")

                with open(file_path, 'r') as input_file, open(temp_file_path, 'w') as output_file:
                    for line in input_file:
                        if '<head>' in line:
                            line += js_code
                        output_file.write(line)

                # Replace the original file with the modified temp file
                os.remove(file_path)
                os.rename(temp_file_path, file_path)

# Example usage:
input_folder = r'C:\Users\Tigereye\Desktop\html'
process_and_rewrite_files_in_folder(input_folder)



