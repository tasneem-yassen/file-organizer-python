from pathlib import Path
import shutil

def organize_folder(folder_path) : 
    if folder_path.is_dir():
        for item in folder_path.iterdir() :     
            return 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organize.py <folder_path>")
    else:
        organize_folder(sys.argv[1])
