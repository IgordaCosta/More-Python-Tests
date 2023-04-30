import os

directory = r"C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Presentable5AddSpinner\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\js"
for filename in os.listdir(directory):
    if filename.endswith(".js"):
        with open(os.path.join(directory, filename), "r") as f:
            content = f.readlines()
        
        with open(os.path.join(directory, filename), "w") as f:
            for line in content:
                if "//" in line:
                    line = line.split("//")[0] + "\n"
                f.write(line)
