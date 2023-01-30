import os
import shutil

def files_list(location:str, extensions:list):
    _filelist = []
    for extension in extensions:
        for root, dirs, files in os.walk(location):
            _filelist = _filelist + [os.path.join(root, x) for x in files if x.endswith(extension)]
    return _filelist

def new_structure_folders(source_path:str, output_path:str, extensions:list):
    filelist = files_list(source_path, extensions)
    folders = output_path.split('/')
    type_folder = '/'.join(folders[:-1])

    if not os.path.isdir(f"{type_folder}"):
        os.mkdir(type_folder)
    if not os.path.isdir(f"{output_path}"):
        os.mkdir(output_path)

    for file in filelist:
        file_name = file.rsplit('/',1)[-1]
        file_destination = f'{output_path}/{file_name}'
        shutil.move(file, file_destination)

if __name__ == "__main__":
    source_path1 = '/home/ubuntu/dataset/train'
    output_path1 = '/home/ubuntu/dataset/output/images/train'

    source_path2 = '/home/ubuntu/dataset/valid'
    output_path2 = '/home/ubuntu/dataset/output/images/valid'

    extensions1 = ['.png', '.jpg']

    source_path3 = '/home/ubuntu/dataset/train'
    output_path3 = '/home/ubuntu/dataset/output/labels/train'

    source_path4 = '/home/ubuntu/dataset/valid'
    output_path4 = '/home/ubuntu/dataset/output/labels/valid'

    extensions2 = ['.txt']

    new_structure_folders(source_path1, output_path1, extensions1)
    new_structure_folders(source_path2, output_path2, extensions1)

    new_structure_folders(source_path3, output_path3, extensions2)
    new_structure_folders(source_path4, output_path4, extensions2)