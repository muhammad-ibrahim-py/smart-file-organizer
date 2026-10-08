# Smart File Organizer
# Author: Muhammad Ibrahim
# GitHub: github.com/muhammad-ibrahim-py
# Description: Organizes files into folders based on their extensions

from pathlib import Path
import shutil
CATEGORIES: dict = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".js", ".html", ".css"],
}
def organize_files(folder_path: str)->None:
    """ Organize files in the given folder into category folders."""
    folder = Path(folder_path)
    if not folder.exists():
        print(f"Folder not found: {folder_path}")
        return
    for file in folder.iterdir():
        if file.is_file():
            extension:str = file.suffix.lower()

# Find the right category for this file's extension

            category: str | None = None
            for cat,extensions in CATEGORIES.items():
                if extension in extensions:
                    category = cat
                    break

# If no category found, use "Others"

            if category is None:
                category = "Others" 

# Create the category folder if it doesn't exist

            category_folder: Path = folder / category
            category_folder.mkdir(exist_ok=True)
            destination: Path = category_folder / file.name

# Handle duplicate filenames
                              
            counter: int = 1
            while destination.exists():
                new_name: str = f"{file.stem}_{counter}{file.suffix}"
                destination = category_folder / new_name
                counter +=1

            # Move the file

            shutil.move(str(file), str(destination))      
            print(f"Moved {file.name}-> {category}/")

def main()->None:
    """Ask user for folder path and organize files."""
    folder_path: str = input("Enter folder path to organize: ")
    organize_files(folder_path)
    print("Done") 

# Run the script when executed directly

if __name__ =="__main__":
    main()    






    
