def generate_files(input_file_path, output_file_name):


    output_file_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval\OutputFunctions' + '\\' + output_file_name
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()


        # print(lines)
        # print('lines')
    linesToWrite = ''
    for line in lines:
        line = line.replace('\n', '')

        print(line)
        print('line')
        replaceSentence = 'try{{\n    = document.getElementById("XXXX").addEventListener("click", XXXX);}catch{}\n'
        replaceValue = 'XXXX'

        replaceSentence = replaceSentence.replace(replaceValue,line )

        linesToWrite = linesToWrite + replaceSentence


        # linesToWrite = + linesToWrite + f'try{{\n    document.getElementById("{line}").addEventListener("click", {line});\n}}catch{{}}' + '\n'

    with open(output_file_path, 'w') as output_file:
        output_file.write(linesToWrite)

    # print(f"Created file: {output_file_path}")



input_file_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval' + '\\' + 'outuputFile.txt'
output_file_name =  'outuputFile2.txt'

generate_files(input_file_path, output_file_name)
