import os
import random

LOCATION = '<folder_path>'
EXTENSION = '.png'
PERCENTAGE_PARTITION = 0.7

def files_list(location: str, extension:str):
    _filelist = []
    for root, dirs, files in os.walk(location):
        _filelist = _filelist + [os.path.join(root, file) for file in files if file.endswith(extension)]
    

    new_filelist = []
    for files in _filelist:
        new_filelist.append("/".join(files.rsplit("/",3)[-3:]))

    random.shuffle(new_filelist)
    number_images = len(new_filelist)
    number_train_images = int(number_images * PERCENTAGE_PARTITION)

    train_list = new_filelist[:number_train_images]
    valid_list = new_filelist[number_train_images:]

    
    with open(f'{location.rsplit("/",1)[0]}/train.txt', 'w') as train_file:
        for train in train_list:
            train_file.write(train + ('\n'))

    with open(f'{location.rsplit("/",1)[0]}/valid.txt', 'w') as valid_file:
        for valid in valid_list:
            valid_file.write(valid + ('\n'))

    print(len(train_list))
    print(len(valid_list))
    
    
if __name__ == "__main__":
    files_list(LOCATION, EXTENSION)