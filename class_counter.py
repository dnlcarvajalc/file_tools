"""This script helps to count how many labels of each category are in a folder with many txt with YOLO labels."""

import os
import pandas as pd

BATCH_1 = '/home/dcarvajal/labels'	#location with txt with labels
CLASS_NUMBER = [0, 1]
CLASS_NAME = ["Class1", "Class2"]	#Here is the name of the sequence of classes in "CLASS_NUMBER"

def files_list(location: str):
    _filelist = []
    for root, dirs, files in os.walk(location):
        _filelist = _filelist + [os.path.join(root, file) for file in files if file.endswith('.txt')]
    return _filelist

def count_classes(_yolo_label_txt:list):
    _all_labels = pd.DataFrame()
    for _txt in _yolo_label_txt:
        _yolo_labels = pd.read_csv(_txt, sep=' ', names=["class_label", "x", "y", "width", "height"])
        _all_labels = pd.concat([_all_labels, _yolo_labels])

    _all_labels["class_label"].replace(CLASS_NUMBER, CLASS_NAME, inplace=True)
    _all_labels = _all_labels["class_label"].value_counts()
    print(_all_labels)
    

if __name__ == "__main__":
    directory = files_list(BATCH_1)
    count_classes(directory)
