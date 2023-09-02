
def replace_newline(file_path):
    with open(file_path, 'rb') as f:
        content = f.read().decode('utf-8')

    content = content.replace(chr(0x90), chr(0x0A)).encode('utf-8')

    with open(file_path, 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    file_path = 'C:\Python311\Lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py'
    replace_newline(file_path)