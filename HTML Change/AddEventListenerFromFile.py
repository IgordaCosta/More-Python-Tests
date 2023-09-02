def add_event_listeners(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        with open(output_file, 'w') as file:
            for line in lines:
                placeholder = line.strip()
                modified_line = line.replace(placeholder, 'try{ document.getElementById("' + placeholder + '").addEventListener("click", ' + placeholder + '); }catch{}')
                file.write(modified_line)
        
        print("Event listeners added successfully!")
    
    except FileNotFoundError:
        print("Input file not found!")

# User-defined inputs
txt_file = input("Enter the path of the input text file: ")
output_path = input("Enter the directory path to save the EventListeners.js file: ")

output_file = output_path + "/EventListeners.js"
add_event_listeners(txt_file, output_file)
