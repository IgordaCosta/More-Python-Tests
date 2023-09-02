def join_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines) - 2:
        first_line = lines[i].rstrip()
        second_line = lines[i + 1].rstrip()
        third_line = lines[i + 2].rstrip()

        if first_line.endswith('>') and second_line.endswith(')') and third_line.endswith('>'):
            lines[i] = first_line.rstrip() +' ' + second_line.strip () + " " + third_line.strip() + '\n'
            del lines[i + 1:i + 3]
        else:
            i += 1

    with open(filename, 'w') as file:
        file.writelines(lines)



folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval' + '\\'  # Replace with the path to your folder
filename = folder_path + 'addInforToTheDocumentHTMLcall.js'
join_lines(filename)






# folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval' + '\\'
# filename =  folder_path + 'addInforToTheDocumentHTMLcall.js'
# with open(filename, 'r') as file:
#         lines = file.readlines()

# print(lines)