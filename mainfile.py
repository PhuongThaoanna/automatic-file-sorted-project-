import os
import shutil

# Define the source directory where your files are located
source_directory = "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-"

# Create separate folders for each file type
folders = {
    "images": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Image",
    "documents": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/documents",
    "videos": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/videos",
    "audio": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/audio ",
    "compressed": "/Users/thaonguyen/Desktop/self-study/Python challenge/automatic-file-sorted-project-/Compressed folder",
    # Add more folders for other file types as needed
}

# Get a list of all files in the source directory
all_files = os.listdir(source_directory)

# Iterate through each file and move it to the appropriate folder
for filename in all_files:
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension in (".jpg", ".png", ".gif"):
        # Move image files to the "images" folder
        shutil.move(os.path.join(source_directory, filename), folders["images"])
    elif file_extension in (".doc", ".pdf", ".txt"):
        # Move document files to the "documents" folder
        shutil.move(os.path.join(source_directory, filename), folders["documents"])
    elif file_extension in (".mp4", ".avi", ".mov"):
        # Move video files to the "videos" folder
        shutil.move(os.path.join(source_directory, filename), folders["videos"])
    elif file_extension in (".mp3", ".wav", ".flac"):
        # Move audio files to the "audio" folder
        shutil.move(os.path.join(source_directory, filename), folders["audio"])
    elif file_extension in (".zip", ".rar", ".7z"):
        # Move compressed files to the "compressed" folder
        shutil.move(os.path.join(source_directory, filename), folders["compressed"])
    # Add more conditions for other file types as needed

print("Sorted successfully!")
