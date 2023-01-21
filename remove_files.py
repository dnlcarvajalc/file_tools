import os
from tqdm import tqdm

SOURCE_FOLDER_PATH = '<source-path>'
EXTENSION = '<extension>'
#EXTENSION = '.DS_Store'

def files_list(location: str):
    filelist=[]
    for root, dirs, files in os.walk(location):
        filelist = filelist + [os.path.join(root, file) for file in files if file.endswith(EXTENSION)]
    return filelist

def remove_files(filelist: str):
    for file in tqdm(filelist):
        os.system(f"rm {file}")

if __name__ == "__main__":
    filelist = files_list(SOURCE_FOLDER_PATH)
    remove_files(filelist)