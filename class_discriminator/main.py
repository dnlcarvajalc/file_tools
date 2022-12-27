import os
import pandas as pd
from tqdm import tqdm
from configparser import ConfigParser

LOCATION_PATH = '<LOCATION_PATH>'

def files_list(location:str, extension:str):
    filelist = []
    for root, dirs, files in os.walk(location):
        filelist = filelist + [os.path.join(root, file) for file in files if file.endswith(extension)]

    if not os.path.isdir(f"{location}/filtered"):
        os.system(f"mkdir {location}/filtered")
    return filelist

def move_labels(filelist:list, categories_number:dict, and_conditionals:dict, or_conditionals:dict, image_extension:str):
    for label_file in tqdm(filelist):
        and_indicator = True
        or_indicator = False
        file_data = pd.read_csv(label_file, sep=' ', names=['class_label', 'x', 'y', 'width', 'height'])
        for key in categories_number.keys():
            file_data['class_label'].replace(int(categories_number[key]), key, inplace=True)

        class_counter = file_data['class_label'].value_counts()

        #File labels must achieve all conditions to be filtered
        for key in and_conditionals:
            try:
                if class_counter[key] < int(and_conditionals[key]):
                    and_indicator = False
            except KeyError:
                and_indicator = False

        #File labels must achive one condition to be filtered
        for key in or_conditionals:
            try:
                if class_counter[key] >= int(or_conditionals[key]):
                    or_indicator = True
            except KeyError:
                pass
        
        if(and_indicator, or_indicator) == (True, True):
            os.system(f'mv {label_file} {LOCATION_PATH}/filtered/')
            image_path = label_file.rsplit('.',1)[0] + image_extension
            os.system(f'mv {image_path} {LOCATION_PATH}/filtered/')
    

if __name__ == '__main__':
    config = ConfigParser()
    config.optionxform=str
    config.read('config.ini')

    CATEGORIES_NUMBER = dict(config.items('CATEGORIES'))
    AND_CONDITIONALS = dict(config.items('AND_CONDITIONALS'))
    OR_CONDITIONALS = dict(config.items('OR_CONDITIONALS'))
    IMAGE_EXTENSION = config['IMAGE_EXTENSION']['extension']
    LABEL_EXTENSION = config['LABEL_EXTENSION']['extension']
    
    filelist = files_list(LOCATION_PATH, LABEL_EXTENSION)
    move_labels(filelist, CATEGORIES_NUMBER, AND_CONDITIONALS, OR_CONDITIONALS, IMAGE_EXTENSION)