import os
import shutil

# Define the directory path
ddir = r"C:\Users\banga\Downloads"

# Create subdirectories if they don't exist
if not os.path.exists(ddir + "/Images"):
    os.makedirs(ddir + "/Images")
    print("Created directory: Images")
if not os.path.exists(ddir + "/Music"):
    os.makedirs(ddir + "/Music")
    print("Created directory: Music")
if not os.path.exists(ddir + "/Video"):
    os.makedirs(ddir + "/Videos")
    print("Created directory: Videos")
if not os.path.exists(ddir + "/Documents"):
    os.makedirs(ddir + "/Documents")
    print("Created directory: Documents")
if not os.path.exists(ddir + "/Code"):
    os.makedirs(ddir + "/Code")
    print("Created directory: Code")
if not os.path.exists(ddir + "/Other"):
    os.makedirs(ddir + "/Other")
    print("Created directory: Other")

# Lists of file extensions for different categories
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
music_extensions = [".mp3", ".wav", ".aiff"]
video_extensions = [".mp4"]
doc_extensions = [".txt", ".pdf", ".docx", ".doc"]
code_extensions = [".py", ".html", ".css", ".js", ".md"]

# Iterate through files in the directory
for file in os.listdir(ddir):
    # Skip processing if the item is a subdirectory
    if os.path.isdir(ddir + "/" + file):
        continue

    # Skip processing of .DS_Store files
    if file == ".DS_Store":
        continue

    # Get the file extension in lowercase
    extension = os.path.splitext(file)[1].lower()

    # Move the file to appropriate subdirectories based on the extension
    if extension in image_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Images")
        print(f"Moved {file} to Images")
    elif extension in music_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Music")
        print(f"Moved {file} to Music")
    elif extension in video_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Video")
        print(f"Moved {file} to Videos")
    elif extension in doc_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Documents")
        print(f"Moved {file} to Documents")
    elif extension in code_extensions:
        shutil.move(ddir + "/" + file, ddir + "/Code")
        print(f"Moved {file} to Code")
    else:
        shutil.move(ddir + "/" + file, ddir + "/Other")
        print(f"Moved {file} to Other")
