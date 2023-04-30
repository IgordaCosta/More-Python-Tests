import os

folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Presentable5AddSpinner\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\css'

for filename in os.listdir(folder_path):
    if filename.endswith(".css"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r+") as f:
            content = f.read()
            content = content.replace("background:black", "background: white")
            f.seek(0)
            f.write(content)
            f.truncate()
