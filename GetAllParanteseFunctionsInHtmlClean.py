


import os


def GetAllParanteseFunctionsInHtml(folder_path, output_file_path):

    folder_path1 = folder_path + '\\'
    with open(output_file_path, "w") as output_file:
        for filename in os.listdir(folder_path1):
            if filename.endswith(".html"):
                file_path = os.path.join(folder_path1, filename)
                with open(file_path, "r") as html_file:
                    for line in html_file:
                        if "()" in line:
                            words = line.split()
                            for i in range(len(words)):
                                if "()" in words[i]:
                                    word = words[i].replace("'",'"').replace('"','').replace('>OK</button>','').replace('onclick=','').replace('</script>','').replace('<script>','').replace('()','')
                                    output_file.write(word + "\n")
                                    break




folder_path = r'C:\Users\Tigereye\Desktop\AddToHtmlEndBodyTag'

output_file_path = folder_path + '\\GetAllParanteseFunctionsInHtml' + '\\' + 'GetAllParanteseFunctionsInHtml.txt'

GetAllParanteseFunctionsInHtml(folder_path, output_file_path)