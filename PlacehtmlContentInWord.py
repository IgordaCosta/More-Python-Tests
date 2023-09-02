import os
from bs4 import BeautifulSoup
from docx import Document
import subprocess

# Path to the folder containing the HTML files

def PlacehtmlContentInWord(folderPath):

    folder_path = folderPath + '\\'
    # Iterate through all HTML files in the folder

    docPathList = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".html"):
            # Construct the file paths for HTML and DOCX files
            html_file_path = os.path.join(folder_path, file_name)
            docx_file_path = os.path.join(folder_path, file_name.replace(".html", ".docx"))

            # Parse the HTML file and extract the content
            with open(html_file_path, "r") as html_file:
                html_content = html_file.read()
                soup = BeautifulSoup(html_content, "html.parser")
                content = soup.get_text()

            # Create a new DOCX document
            doc = Document()
            # Add each line of the content as a paragraph in the DOCX file
            for line in content.splitlines():
                doc.add_paragraph(line)

            # Save the DOCX file with the same name as the HTML file
            doc.save(docx_file_path)
            # print(f"Created: {docx_file_path}")

            docPathList.append(docx_file_path)



    for docPath in docPathList:
    # Open the created DOCX file
        subprocess.Popen(["start", "", docPath], shell=True)

    print('DONE')




folderPath = r"C:\Users\Tigereye\Desktop\Stuff\PlacehtmlContentInWord"
PlacehtmlContentInWord(folderPath)