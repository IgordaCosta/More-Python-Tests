import os


def AddScriptToHtml(folder_path, ScriptString):

    folder_path1 = folder_path + '\\'
    for filename in os.listdir(folder_path1):
        if filename.endswith(".html"):
            file_path = os.path.join(folder_path1, filename)
            with open(file_path, "r+") as f:
                html = f.read()
                body_index = html.find("</body>")
                if body_index != -1:
                    new_html = html[:body_index] + ScriptString + html[body_index:]
                    f.seek(0)
                    f.write(new_html)
                    f.truncate()




folder_path = r'C:\Users\Tigereye\Desktop\AddToHtmlEndBodyTag'
ScriptString = '<script type="text/javascript" src="RemoveGotResultsOnHtml.js" defer></script>\n'


AddScriptToHtml(folder_path, ScriptString)