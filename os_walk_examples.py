import os
import shutil

START_FOLDER = "C:/py3intro"
DEST_FOLDER = "C:/copies"

skips = ['.git', '__pycache__', 'dist', 'cookiecutter-python-module']

for folder, subs, filenames in os.walk(START_FOLDER):
    for skip in skips:
        if skip in subs:
            subs.remove(skip)
    print(folder)
    for filename in filenames:
        if filename.endswith('.py') and filename.startswith('p'):
            file_path = os.path.join(folder, filename)
            shutil.copy(file_path, DEST_FOLDER)

# [(dir,subs,files),(dir,subs,files),(dir,subs,files), ...]    
