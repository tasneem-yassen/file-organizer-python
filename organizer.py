import os
import shutil
import sys

def organize_folder() : 
    #to be continued 
    return 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organize.py <folder_path>")
    else:
        organize_folder(sys.argv[1])
