import os

START_FOLDER = "."

for folder, subs, filenames in os.walk(START_FOLDER):
    if '.git' in subs:
        subs.remove('.git')
    print(folder)
    for filename in filenames:
        if filename.startswith('p'):
            file_path = os.path.join(folder, filename)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:10d} {filename}")
