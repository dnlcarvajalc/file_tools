import os
from tqdm import tqdm

def unpack_folder(folder_path:str):
    filelist = []
    for root, dirs, files in os.walk(folder_path):
        filelist = filelist + [os.path.join(root, x) for x in files]


    for file in tqdm(filelist):
        os.system(f"mv {file} {folder_path}/")

unpack_folder('path_folder_1')
unpack_folder('path_folder_2')
unpack_folder('path_folder_3')
unpack_folder('path_folder_4')