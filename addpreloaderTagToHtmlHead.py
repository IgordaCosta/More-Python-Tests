import os
from bs4 import BeautifulSoup

# folder_path = '/path/to/folder' # Replace with the path to your folder

folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Presentable5AddSpinner\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller'
script_src = 'preloader.js'

for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        filepath = os.path.join(folder_path, filename)
        with open(filepath) as f:
            soup = BeautifulSoup(f, 'html.parser')
            head = soup.head
            script_tag = soup.new_tag('script', type='text/javascript', src='./js/' + script_src)
            head.insert(0, script_tag)
        with open(filepath, 'w') as f:
            f.write(str(soup))
