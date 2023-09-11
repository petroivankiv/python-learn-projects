import os
import shutil
import promptlib


def create_folder(path: str, folder_name: str) -> str:
    folder_path = os.path.join(path, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    return folder_path

def sort_files(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            extension: str = os.path.splitext(filename)[1]
            
            if extension:
                # skip dot -> .png - png
                folder_name = extension[1:]
                target_folder: str = create_folder(source_path, folder_name)
                target_path: str = os.path.join(target_folder, filename)
                file_path: str = os.path.join(root_dir, filename)
                
                shutil.move(file_path, target_path)
                
def rm_empty_folders(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for curr_dir in sub_dir:
            dir_path: str = os.path.join(root_dir, curr_dir)
            
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                
def main():
    prompter = promptlib.Files()
    dir_path = prompter.dir()
    
    if os.path.exists(dir_path):
        sort_files(dir_path)
        rm_empty_folders(dir_path)
        print('Файли посортовані!')
    else:
        print('Шлях не правильний!')
        

if __name__ == '__main__':
    main()