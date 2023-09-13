import os
import shutil

files_to_copy = []

SOURCE_FOLDER = "../DATA"
DESTINATION_FOLDER = "../TEMP"

for file_name in os.listdir(SOURCE_FOLDER):
    if file_name.startswith('p'):
        files_to_copy.append(file_name)

for file_to_copy in files_to_copy:
    file_path_to_copy = os.path.join(SOURCE_FOLDER, file_to_copy)
    shutil.copy(file_path_to_copy, DESTINATION_FOLDER)
