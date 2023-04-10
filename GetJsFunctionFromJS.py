import os
import shutil
import re

def extract_css_js_files(folder_path):

    js_folder_path = os.path.join(folder_path, 'JSFunctionfiles')


    if not os.path.exists(js_folder_path):
        os.makedirs(js_folder_path)


    js_files = []


    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:

                    contents = f.readlines()

                    for content in contents:
                        
                        if '()' in content:
                            if '<!--' in content:
                                pass
                            else:
                                content2 = content.replace(" ", "").replace('"', "'").replace("'",'').replace('onclick=', '()').split("()")[1]
                    
                                js_files.append(content2)
                



    js_files1 = list(set(js_files))


    js_files1.sort()

            
    with open(js_folder_path + '\\' + 'JsFunctionFilesInApp.txt', "w") as file:
        for item in js_files1:
            file.write(item + '\n')
        file.close()


                    
                         
                      



folder_path = r"C:\Users\Tigereye\Desktop\HTMLfiles" + '\\'

extract_css_js_files(folder_path)
