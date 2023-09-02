import os
import chardet
from bs4 import BeautifulSoup

def remove_defer_from_head(location):
    for root, dirs, files in os.walk(location):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    raw_content = f.read()
                    encoding = chardet.detect(raw_content)["encoding"]
                html_content = raw_content.decode(encoding)

                soup = BeautifulSoup(html_content, "html.parser")
                head_tag = soup.find("head")
                if head_tag:
                    script_tags = head_tag.find_all("script", defer=True)
                    for script_tag in script_tags:
                        if not script_tag.find_parents("body"):
                            del script_tag["defer"]

                with open(file_path, "w", encoding=encoding) as f:
                    f.write(str(soup))
                print(f"Processed: {file_path}")



folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated9\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller' '\\' # Replace with the path to your folder containing HTML files
remove_defer_from_head(folder_path)
