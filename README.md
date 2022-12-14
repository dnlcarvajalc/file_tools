# file_tools

### YOLO LABELS
- class_counter.py ==> This is a tool that loads a batch of txt with YOLO label structure 
(class - center_x - center_y - width - height). It concatenates those txt and counts how many
labels are for each category. You can put a the name of each category and copy from terminal 
the table generated using pandas.

- filelist.py ==> This script generates two txt with a path list of images (train.txt and valid.txt).
You can specify percentage partition of total images. This is with the objective to train YOLO darknet.

- unpack_drive_folders.py ==> This util is useful when you download many files from google Drive. It 
creates a lot of folders and to unpack this manually it takes a lot of time. This script moves every 
single file from this subfolders to main folder. You can put many folders to un pack in the same script. 

------------
