from pathlib import Path
import shutil
import sys 
file_types = {".jpg" : "Images" ,
              ".png" : "Images" ,
              ".svg" : "Images" , 
              ".docx" : "Documents" ,
              ".pdf" : "Documents" , 
              ".txt" : "Documents" ,
              ".mp3" : "Audio" , 
              ".wav" : "Audio" , 
              ".mp4" : "Video" ,
              ".mov" : "Video" , 
              ".zip" : "Archives" ,
              ".rar" : "Archives" , 
              ".py" : "Code" ,
              ".js" : "Code" ,
              ".html" : "Code" ,
              }

def organize_folder(folder_path_str,dry_run) :
    folder_path = Path(folder_path_str)
    if folder_path.is_dir():
        for item in folder_path.iterdir() :     
            if item.is_file(): 
                extension= item.suffix
                if not extension : 
                    folder_name = "Other"
                else: 
                    folder_name= file_types.get(extension)  
                    if not folder_name : 
                        folder_name= "Other" 
                target_folder = folder_path / folder_name
                if not dry_run :
                    target_folder.mkdir(exist_ok=True)
                    print("Moving",item.name ,"→",folder_name)
                    shutil.move(item,target_folder)
                else:
                        print("Would move",item.name ,"→",folder_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python organize.py <folder_path>")
    else:
        if "--dry-run" in sys.argv : 
            dry_run = True
        else:
            dry_run = False 
        organize_folder(sys.argv[1],dry_run)
