# Import necessary Python modules
import os
import shutil

# --- INSTRUCTIONS ---
# 1. Place this script inside the folder you want to organize (e.g., your 'Downloads' folder).
# 2. Run the script from your terminal using: python folder_organizer.py
# 3. The script will create new folders (like 'Images', 'Documents', etc.) and
#    move the files into their respective folders.

def organize_folder():
    """
    This function organizes files in its current directory into subfolders
    based on their file extension.
    """
    # Get the path of the directory where the script is located
    # This is the folder we are going to organize
    target_path = os.getcwd()
    
    # Get a list of all files and folders in the target directory
    all_items = os.listdir(target_path)

    print(f"Starting to organize files in: {target_path}\n")

    # This dictionary maps folder names to the file extensions they should contain.
    # You can easily add more file types here!
    file_mappings = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xls", ".xlsx", ".odt"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Scripts & Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".sh"],
        "Executables": [".exe", ".msi"]
    }

    # Loop through every item in the directory
    for item_name in all_items:
        # Construct the full path of the item
        item_path = os.path.join(target_path, item_name)

        # Skip directories and the script file itself
        if os.path.isdir(item_path) or item_name == "folder_organizer.py":
            continue

        # Get the file extension (e.g., '.txt')
        file_extension = os.path.splitext(item_name)[1].lower()

        # Variable to track if the file has been moved
        moved = False
        
        # Check if the file extension matches any category in our mapping
        for folder_name, extensions in file_mappings.items():
            if file_extension in extensions:
                # This is the destination folder path
                destination_folder_path = os.path.join(target_path, folder_name)

                # Create the destination folder if it doesn't exist
                if not os.path.exists(destination_folder_path):
                    os.makedirs(destination_folder_path)
                    print(f"Created folder: {folder_name}")

                # Move the file
                shutil.move(item_path, destination_folder_path)
                print(f"Moved '{item_name}' to '{folder_name}'")
                moved = True
                break # Stop checking once moved

        # If the file type was not in our mapping, move it to an 'Other' folder
        if not moved:
            other_folder_path = os.path.join(target_path, "Other")

            # Create the 'Other' folder if it doesn't exist
            if not os.path.exists(other_folder_path):
                os.makedirs(other_folder_path)
                print("Created folder: Other")

            # Move the file
            shutil.move(item_path, other_folder_path)
            print(f"Moved '{item_name}' to 'Other'")

    print("\nFolder organization complete!")

# This makes sure the function runs only when the script is executed directly
if __name__ == "__main__":
    organize_folder()