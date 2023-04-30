import os


def GetLocationOfWordsInJsFile(words_file_path, js_folder_path, output_file_path):
    # Read list of words from file
    with open(words_file_path, "r") as words_file:
        words = [word.strip() for word in words_file]

    # Search for words in JS files and write results to output file
    with open(output_file_path, "w") as output_file:
        written_lines = set()
        for filename in os.listdir(js_folder_path):
            if filename.endswith(".js"):
                file_path = os.path.join(js_folder_path, filename)
                with open(file_path, "r") as js_file:
                    new_file_path = True
                    for line_number, line in enumerate(js_file, start=1):
                        for word in words:
                            if word in line:
                                result_line = f"{word} {file_path}:{line_number}\n"
                                if result_line not in written_lines:
                                    if new_file_path:
                                        output_file.write("\n")
                                        new_file_path = False
                                    output_file.write(result_line)
                                    written_lines.add(result_line)
                if not new_file_path:
                    output_file.write("\n")
    

   

                    
                    





# Prompt user to enter paths to input and output files

js_folder_path = r'C:\Users\Tigereye\Desktop\AddToHtmlEndBodyTag\jsFolder' +'\\'
textFileNameInput = 'GetAllParanteseFunctionsInHtmlClean2.txt'
textFileNameOutput = 'LocationOfWordsInFile.txt'
PathFileName =  r'C:\Users\Tigereye\Desktop\AddToHtmlEndBodyTag\GetAllParanteseFunctionsInHtml' +'\\'
words_file_path = PathFileName+ textFileNameInput
output_file_path = PathFileName + textFileNameOutput



GetLocationOfWordsInJsFile(words_file_path, js_folder_path, output_file_path)