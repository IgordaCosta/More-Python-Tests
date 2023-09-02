import codecs

def check_for_chr(file_path, chr_to_find):
    with open(file_path, 'rb') as f:
        content = f.read().decode('utf-8')

    if chr_to_find in content:
        return True
    else:
        return False

if __name__ == '__main__':
    file_path = 'C:\Python311\Lib\site-packages\PyInstaller\lib\modulegraph\modulegraph.py'
    chr_to_find = '0A'

    if check_for_chr(file_path, chr_to_find):
        print('The character {} was found in the file.'.format(chr_to_find))
    else:
        print('The character {} was not found in the file.'.format(chr_to_find))