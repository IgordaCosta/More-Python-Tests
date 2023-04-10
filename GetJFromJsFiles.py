import os
import shutil
import re

def extract_css_js_files(folder_path):
    # css_folder_path = os.path.join(folder_path, 'CSSfiles'
    js_folder_path = os.path.join(folder_path, 'JSfilesFromJS')


    if not os.path.exists(js_folder_path):
        os.makedirs(js_folder_path)


    js_files = []
     

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)

                # js_files = []
                # css_files = []     
                with open(file_path, 'r') as f:
                    # contents = f.read()
                    contents = f.readlines()

                    # js_files = []
                    # css_files = []                   
                    for content in contents:
                        
                        # if '.js' in content and all(x not in content for x in ('.min', '<!--')):

                        if './js/' in content:
                            if '//' in content:
                                pass
                            else:

                                content2 = content.replace(" ", "").replace("'", '"').replace('"','').replace(";",'').replace("))","./js/").split("./js/")[1]
                                # print(content2)

                                # print(content2)
                    
                                js_files.append(content2 + '.js')



                    




    js_files1 = list(set(js_files))



    js_files1.sort()


    # print(css_files1)
                

                        



    with open(js_folder_path + '\\' + 'JsFilesInJsInApp.txt', "w") as file:
        for item in js_files1:
            file.write(item + '\n')
        file.close()


                    
                         
                      



folder_path = r"C:\Users\Tigereye\Desktop\HTMLfiles" + '\\'

extract_css_js_files(folder_path)
