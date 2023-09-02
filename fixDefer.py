import os

def substitute_defer(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()

                updated_content = content.replace('defer=""', 'defer')

                with open(file_path, "w") as f:
                    f.write(updated_content)

                print(f"Processed: {file_path}")

# Usage example
folderLocation = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated9\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller' '\\' # Replace with the path to your folder containing HTML files
substitute_defer(folderLocation)
