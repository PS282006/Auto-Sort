import os
import shutil

# Define the paths
DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
DESTINATIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Code": [".py", ".js", ".html", ".dart"],
    "Videos": [".mp4", ".mov", ".mkv"]
}

def organize_downloads():
    for filename in os.listdir(DOWNLOADS_PATH):
        file_ext = os.path.splitext(filename)[1].lower()
        
        for folder, extensions in DESTINATIONS.items():
            if file_ext in extensions:
                dest_folder = os.path.join(DOWNLOADS_PATH, folder)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                shutil.move(os.path.join(DOWNLOADS_PATH, filename), 
                            os.path.join(dest_folder, filename))
                print(f"Moved: {filename} ➡️ {folder}")

if __name__ == "__main__":
    organize_downloads()