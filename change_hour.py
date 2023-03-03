import os

#video name example 20230221T095000-20230221T095500.dav
EXTENSIONS = ['.mp4', '.dav']
SOURCE_PATH = 'folder_path'
HOUR_DIFF = -15

def files_list(location:str):
    filelist = []
    for extension in EXTENSIONS:
        for root, dirs, files in os.walk(location):
            filelist = filelist + [os.path.join(root, x) for x in files if x.endswith(extension)]
    return filelist

def change_video_names():
    filelist = files_list(SOURCE_PATH)

    if not os.path.isdir(f'{SOURCE_PATH}/renamed'):
        os.mkdir(f'{SOURCE_PATH}/renamed')

    for file in filelist:
        folder_path, video_name = file.rsplit('/',1)
        video_name, extension = video_name.rsplit('.',1)
        new_video_name = change_hour(video_name)
        os.system(f'cp {file} {folder_path}/renamed/{new_video_name}.{extension}')

def change_hour(video_name:str) -> str:
    dates = []
    dates = video_name.split('-')
    for iterator, date in enumerate(dates):
        new_day, new_hour = date.split('T')
        new_hour = int(new_hour) + HOUR_DIFF*10000
        if new_hour >= 240000:
            new_hour = new_hour - 240000
            new_day = int(new_day) + 1
        if new_hour < 0:
            new_hour = new_hour + 240000
            new_day = int(new_day) - 1
        if new_hour < 100000 and new_hour > 0:
            new_hour = '0' + str(new_hour) 
        if float(new_hour) < 10000 and float(new_hour) > 0:
            new_hour = '0' + str(new_hour)
        if new_hour == 0:
            new_hour = '000000'
        
        dates[iterator] = str(new_day) + 'T' + str(new_hour)
    new_video_name = '-'.join(dates)
    return new_video_name

if __name__ == "__main__":
    change_video_names()