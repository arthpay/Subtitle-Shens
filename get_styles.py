import ass
import glob
import os

# Get the current directory path
current_directory = r"D:\New folder"

# Search for .ass files in the current directory
sublist = glob.glob(f"{current_directory}/*.ass")
stylelist = set()

for sub in sublist:
    with open(sub, encoding='utf_8_sig') as sub_file:
        doc = ass.parse(sub_file)
        for styles in doc.styles._lines:
            stylelist.add(styles.name)

print(stylelist)