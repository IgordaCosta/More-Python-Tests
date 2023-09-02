import os

def find_words_with_py(folder_path, output_file_path):
  """
  This function searches for all files in a folder and returns all word texts that have the string "py" in them and place them into a txt file one line per word at a user defined location.

  Args:
    folder_path: The path to the folder to search.
    output_file_path: The path to the output file.

  Returns:
    None.
  """

  # Get a list of all files in the folder.
  files = os.listdir(folder_path)

  # Create a set to store the words found.
  words = []

  # Iterate over the files.
  for file in files:
    # If the file is a Python file, open it and read its contents.
    if file.endswith(".js"):
      with open(os.path.join(folder_path, file), "r") as f:
        contents = f.read()

      # Split the contents into words.
      words_in_file = contents.split()

      # Add the words to the set of words found if they contain "py".
      for word in words_in_file:
        if ".py" in word:
          words.append(word)

  # Open the output file and write the words to it, one word per line.
  with open(output_file_path, "w") as f:
    for word in words:
      f.write(word + "\n")



folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated92\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\js' + '\\'
output_file_path = r'C:\Users\Tigereye\Desktop\Stuff\LocationOfText\outputTextLocations.txt'

# Find the words with "py" in them and write them to the output file.
find_words_with_py(folder_path, output_file_path)