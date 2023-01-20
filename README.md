# file_tools

### YOLO LABELS
- data_notebooks ==> this folder contains jupyter notebooks to get o convert data. It contains: 
    - OpenImages_download.ipynb ==> with this notebook we can download images from OpenImagesV6 of a certain class.

- class_discriminator ==> This folder contains two files. This tool is useful for getting images with 
certain amount of each category. In config.ini there are two types of filter. In AND_CONDITIONALS, image
must fulfill all conditionals. In OR_CONDITIONALS, images must fulfill just one conditional. If there is 
no OR_CONDITIONAL, you must put at least one that you put before in AND_CONDITIONALS.

- class_counter.py ==> This is a tool that loads a batch of txt with YOLO label structure 
(class - center_x - center_y - width - height). It concatenates those txt and counts how many
labels are for each category. You can put a the name of each category and copy from terminal 
the table generated using pandas.

- filelist.py ==> This script generates two txt with a path list of images (train.txt and valid.txt).
You can specify percentage partition of total images. This is with the objective to train YOLO darknet.

- unpack_drive_folders.py ==> This util is useful when you download many files from google Drive. It 
creates a lot of folders and to unpack this manually it takes a lot of time. This script moves every 
single file from this subfolders to main folder. You can put many folders to un pack in the same script. 

- video_folder_sort.py ==> This script puts a video with its respective file with the information about detections in to an enumerated folder. 

------------
