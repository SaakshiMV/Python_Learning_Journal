import os
import shutil

# Change this to your folder path
FOLDER_PATH = "test_folder"

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
}

def organize_files():
    if not os.path.exists(FOLDER_PATH):
        print("Folder not found!")
        return

    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            moved = False

            for folder, extensions in FILE_TYPES.items():
                if any(file.endswith(ext) for ext in extensions):
                    dest_folder = os.path.join(FOLDER_PATH, folder)
                    os.makedirs(dest_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(FOLDER_PATH, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

    print("Files organized successfully!")

if __name__ == "__main__":
    organize_files()
