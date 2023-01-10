import os
import shutil

PATH_FOLDER = '<folder_path>'
EXTENSION = '.jpg'

def files_list(location: str):
    _filelist = []
    for root, dirs, files in os.walk(location):
        _filelist = _filelist + [os.path.join(root, file) for file in files if file.endswith(EXTENSION)]
    return _filelist

def rename_files(filelist: list):
    i = 0
    for file in filelist:
        root_folder_name = file.rsplit("/",1)[0]
        if not os.path.isdir(f"{root_folder_name}/renamed"):
            os.system(f"mkdir {root_folder_name}/renamed")
        shutil.copy(file, f'{root_folder_name}/renamed/{i}{EXTENSION}')
        i += 1

if __name__ == "__main__":
    filelist = files_list(PATH_FOLDER)
    rename_files(filelist)
