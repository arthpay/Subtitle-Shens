import os
import glob

def split_ass(ass_file_path):
    with_shad0_lines = []
    without_shad0_lines = []
    format_count = 0  # Count the occurrences of "Format:"
    split_keywords = ["Signs,","\shad0", "\pos", "\blur", "\fad"]

    # Open the ASS file for reading
    with open(ass_file_path, 'r', encoding='utf-8') as file:
        copying = True
        for line in file:
            if copying:
                with_style_lines.append(line)
                without_style_lines.append(line)

            if "Format:" in line:
                format_count += 1
            if format_count >= 2:
                copying = False

            
            for keyword in split_keywords:
                if keyword in line or "Sign," in line:
                    with_style_lines.append(line)
                    break  # Only add the line once to the "with_style" list
                else:
                    if format_count == 2 and "Format:" not in line:
                        without_style_lines.append(line)
                    break

    # Determine the output file paths
    file_dir, file_name = os.path.split(ass_file_path)
    with_style_output_path = os.path.join(file_dir, "Track_4.ass")
    without_style_output_path = os.path.join(file_dir, "Track_3.ass")

    # Write the lines to separate files
    with open(with_style_output_path, 'w', encoding='utf-8') as with_style_file:
        with_style_file.writelines(with_style_lines)

    with open(without_style_output_path, 'w', encoding='utf-8') as without_style_file:
        without_style_file.writelines(without_style_lines)

# Specify the folder where ASS files are located (and its subfolders)
folder_path = r"E:\01"

# Search for ASS files in the specified folder and its subfolders
ass_files = glob.glob(os.path.join(folder_path, "**", "*.ass"), recursive=True)
print(ass_files)
# Apply the split_ass function to each ASS file
for ass_file in ass_files:
    split_ass(ass_file)
