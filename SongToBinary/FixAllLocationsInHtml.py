import os
import re

folder_path = r"C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller"  # replace with the path to your folder

for filename in os.listdir(folder_path):
    if filename.endswith(".html") or filename.endswith(".js"):  # only process HTML and JS files
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as f:
            lines = f.readlines()
        with open(file_path, "w") as f:
            for line in lines:
                stripped_line = line.strip().replace(" ", "")
                if re.search(r'href\s*=\s*[\'"]', stripped_line):
                    line = re.sub(r'href\s*=\s*[\'"]','''href="${path.join(__dirname, ' ''', line)
                elif re.search(r'src\s*=\s*[\'"]', stripped_line):
                    line = re.sub(r'src\s*=\s*[\'"]', '''src="${path.join(__dirname, ' ''', line)

                line = re.sub('''.css\s*"\s*>''','''.css')}">''', line )
                line = re.sub(""".css\s*'\s*>""",""".css')}'>""", line )


                line = re.sub('''.js\s*"\s*>''','''.js')}">''', line )
                line = re.sub(""".js\s*'\s*>""",""".js')}'>""", line )



                line = re.sub('''.png\s*"''','''.png')}"''', line )





                f.write(line)
