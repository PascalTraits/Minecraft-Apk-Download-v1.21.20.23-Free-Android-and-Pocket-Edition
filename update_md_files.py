import os
from datetime import datetime

# Specify the directory you want to search for .md files
directory = '.'

# Walk through all files and directories within the specified directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'a') as f:
                f.write(f"\nUpdated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
