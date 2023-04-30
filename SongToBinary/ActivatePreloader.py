import os

def replace_location_replace(folder_path):
    # Loop through all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".js"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as f:
                # Read in the contents of the file
                contents = f.read()

            # Split the contents into individual lines
            lines = contents.split("\n")

            # Loop through each line and replace any instances of location.replace
            for i in range(len(lines)):
                if "location.replace(" in lines[i]:
                    # Replace single quotes with double quotes
                    line = lines[i].replace("'", "\"")

                    # Get the URL being replaced
                    url = line.split("\"")[1]

                    # Replace the line with the preloader code and the new URL
                    new_line = (
                        'var preloader = document.getElementById("preloader");\n' +
                        'preloader.style.display = "block";\n' +
                        f'setTimeout(function() {{\n' +
                        f'    window.location.href = "{url}";\n' +
                        '}, 1000);'
                    )
                    lines[i] = new_line

            # Write the updated contents back to the file
            with open(file_path, "w") as f:
                f.write("\n".join(lines))



folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Presentable5AddSpinner\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\js'

replace_location_replace(folder_path)