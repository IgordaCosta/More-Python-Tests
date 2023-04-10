import os
import shutil
import re

def extract_css_js_files(folder_path):
    css_folder_path = os.path.join(folder_path, 'CSSfiles')
    js_folder_path = os.path.join(folder_path, 'JSfiles')

    if not os.path.exists(css_folder_path):
        os.makedirs(css_folder_path)

    if not os.path.exists(js_folder_path):
        os.makedirs(js_folder_path)


    js_files = []
    css_files = []    

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
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

                        if '.js' in content:
                            if '<!--' in content:
                                pass
                            else:

                                content2 = content.replace(" ", "").replace('.js', './js/').split("./js/")[1]
                                # print(content2)

                                # print(content2)
                    
                                js_files.append(content2 + '.js')



                    for content in contents:
                        
                        # if '.css' in content and all(x not in content for x in ('.min', '<!--')):
                        if '.css' in content:
                            if '<!--' in content:
                                pass
                            else:

                                content2 = content.replace(" ", "").replace('.css', './css/').split("./css/")[1]
                                # print(content2)

                                # print(content2)
                    
                                css_files.append(content2 + '.css')


    css_files1 = list(set(css_files))

    js_files1 = list(set(js_files))


    css_files1.sort()

    js_files1.sort()


    # print(css_files1)
                

                        

    with open(css_folder_path + '\\' + 'CSSFilesInApp.txt', "w") as file:
        for item in css_files1:
            file.write(item + '\n')
        file.close()



    with open(js_folder_path + '\\' + 'JsFilesInApp.txt', "w") as file:
        for item in js_files1:
            file.write(item + '\n')
        file.close()


                    
                         
                      



folder_path = r"C:\Users\Tigereye\Desktop\HTMLfiles" + '\\'

extract_css_js_files(folder_path)
