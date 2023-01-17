import os 
from tqdm import tqdm

LOCATION_PATH = '<folder-path>'
VIDEO_EXTENSION = '.mp4'
CLASSIFIER_EXTENSION = '.csv'

def files_list(location: str):
    filelist=[]
    for root, dirs, files in os.walk(location):
        filelist = filelist + [os.path.join(root, file) for file in files if file.endswith(CLASSIFIER_EXTENSION)]
    return filelist

def sort_videos_in_folders(filelist: list):
    folder_name_iterator = 1
    for file in tqdm(filelist):
        file_raw_name = os.path.splitext(file)[0]
        file_raw_name = file_raw_name.rsplit('-',1)[0]  #Comment this line if classifier files have raw names. 
        if os.path.exists(file_raw_name + VIDEO_EXTENSION):
            if not os.path.isdir(f"{LOCATION_PATH}/{folder_name_iterator}"):
                os.system(f"mkdir {LOCATION_PATH}/{folder_name_iterator}")
                os.system(f"mv {file} {LOCATION_PATH}/{folder_name_iterator}")
                os.system(f"mv {file_raw_name + VIDEO_EXTENSION} {LOCATION_PATH}/{folder_name_iterator}")
                folder_name_iterator += 1


if __name__ == "__main__":
    filelist = files_list(LOCATION_PATH)
    sort_videos_in_folders(filelist)