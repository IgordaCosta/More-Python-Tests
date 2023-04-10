import os
import shutil
import re

def extract_css_js_files(folder_path):

    js_folder_path = os.path.join(folder_path, 'HTMLFiles')

    if not os.path.exists(js_folder_path):
        os.mkdir(js_folder_path)




    js_files = []

    print('start1')
    for root, dirs, files in os.walk(folder_path):
        print('start2')
        # print(files)
        for file in files:
        #     print('start3')
            # print(file)
            if file.endswith('.html'):
                print('start4')
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    print('start5')

                    contents = f.readlines()


                    for content0 in contents:



                        if "()" in content0:

                            content = content0.replace(' ', '')

                            if 'onclick=' in content:
                                print('ok')
                                if r'<!--' in content:
                                    pass
                                else:
                                    if r'-->' in content:
                                        pass
                                    else:    
                                        content2 = content.replace(' ', '').replace('"', "'").replace("'",'').replace("onclick=", "()").split("()")[1]
                            
                                        js_files.append(content2)
                



    js_files1 = list(set(js_files))


    js_files1.sort()

            
    with open(js_folder_path + '\\' + 'JsFunctionFilesInApp.txt', "w") as file:
        for item in js_files1:
            file.write(item + '\n')
        file.close()

    print('DONE')


                    
                         
                      



folder_path = r"C:\Users\Tigereye\Desktop\HTMLfiles\HTMLOriginal" + '\\'

extract_css_js_files(folder_path)
