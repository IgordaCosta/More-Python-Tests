

# Iterate over all files in the folder
import os
from bs4 import BeautifulSoup
import os
import chardet
from bs4 import BeautifulSoup

def add_defer_to_body_scripts(location):
    for root, dirs, files in os.walk(location):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    raw_content = f.read()
                    encoding = chardet.detect(raw_content)["encoding"]
                html_content = raw_content.decode(encoding)

                soup = BeautifulSoup(html_content, "html.parser")
                body_tag = soup.find("body")
                if body_tag:
                    script_tags = body_tag.find_all("script")
                    for script_tag in script_tags:
                        if not script_tag.find_parents("head"):
                            script_tag["defer"] = ""

                with open(file_path, "w", encoding=encoding) as f:
                    f.write(str(soup))
                print(f"Processed: {file_path}")

# Usage example



location= r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated9\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller' '\\' # Replace with the path to your folder containing HTML files
add_defer_to_body_scripts(location)