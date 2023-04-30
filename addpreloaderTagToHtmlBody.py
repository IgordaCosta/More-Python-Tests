import os
from bs4 import BeautifulSoup

# folder_path = '/path/to/folder' # Replace with the path to your folder
folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Presentable5AddSpinner\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller'

for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        filepath = os.path.join(folder_path, filename)
        with open(filepath) as f:
            soup = BeautifulSoup(f, 'html.parser')
            body = soup.body
            preloader_div = soup.new_tag('div', id='preloader')
            spinner_div = soup.new_tag('div', **{'class': 'spinner'})
            preloader_div.append(spinner_div)
            body.insert(0, preloader_div)
        with open(filepath, 'w') as f:
            f.write(str(soup))
