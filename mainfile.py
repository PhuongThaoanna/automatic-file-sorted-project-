import os
import shutil
import magic

# Define the source directory
source_directory = "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-"

# Create separate folders for each file type
folders = {
    "images": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Image",
    "documents": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/documents",
    "videos": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/videos",
    "audio": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/audio",
    "compressed": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Compressed folder",
    # Add more folders for other file types as needed
}

# Ensure folders exist or create them
for folder_path in folders.values():
    os.makedirs(folder_path, exist_ok=True)

# Get a list of all files in the source directory
all_files = os.listdir(source_directory)

# Initialize the magic library
magic_instance = magic.Magic()

# Iterate through each file and move it to the appropriate folder
for filename in all_files:
    file_path = os.path.join(source_directory, filename)
    file_extension = os.path.splitext(filename)[1].lower()

    # Use magic to detect the file type
    file_type = magic_instance.from_file(file_path, mime=True)

    if file_extension in (".jpg", ".png", ".gif"):
        # Move image files to the "images" folder
        shutil.move(file_path, folders["images"])
    elif file_extension in (".doc", ".pdf", ".txt"):
        # Move document files to the "documents" folder
        shutil.move(file_path, folders["documents"])
    elif file_extension in (".mp4", ".avi", ".mov"):
        # Move video files to the "videos" folder
        shutil.move(file_path, folders["videos"])
    elif file_extension in (".mp3", ".wav", ".flac"):
        # Move audio files to the "audio" folder
        shutil.move(file_path, folders["audio"])
    elif file_extension in (".zip", ".rar", ".7z"):
        # Move compressed files to the "compressed" folder
        shutil.move(file_path, folders["compressed"])
    # Add more conditions for other file types as needed

print("Sorted successfully!")
