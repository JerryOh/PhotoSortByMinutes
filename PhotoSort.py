import os, shutil
from PIL import Image
import datetime

#For current directory, '.'
parent_path = 'C:/Users/ohjun/Desktop/test1'
time_arr = []
path_arr = []

for f in os.listdir(parent_path):
    full_path = os.path.join(parent_path, f)
    img = Image.open(full_path)
    exif = img.getexif()
    t = datetime.time(int(exif[36867][11:13]), int(exif[36867][14:16]))
    dt = datetime.datetime.combine(datetime.date.today(), t)

    time_arr.append(dt)
    path_arr.append(full_path)
    img.close()

j = 1
k = 0
os.chdir(parent_path)

while k < len(time_arr):
    os.mkdir(str(j))
    new_path = os.path.join(parent_path, str(j))
    j += 1
    shutil.move(path_arr[k], new_path)
    k += 1

    while k < len(time_arr):
        diff = time_arr[k] - time_arr[k - 1]
        if (diff.seconds <= 900):
            shutil.move(path_arr[k], new_path)
            k += 1
        else:
            break







