import os

# Specify the directory to search in
directory = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller' + '\\'

# Iterate through all files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            # Open the file for reading and writing
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding="utf-8") as f:
                lines = f.readlines()

            # Remove the <base href="app://./" /> tag from the file
            with open(filepath, 'w', encoding="utf-8") as f:
                for line in lines:
                    if '<base href="app://./" />' in line:
                        continue
                    f.write(line)