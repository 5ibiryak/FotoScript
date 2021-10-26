import os
from os import listdir
import time
import shutil


file_path = '/home/laim/Downloads/sample_photo'
path_folders = '/home/laim/Downloads'
all_photo = sorted(listdir(file_path))
first_folder = 1
photo_previos = ''
count=1
# перейти в папку и выбрать следующий файл
# создать папку, если время между последним файлом и настоящим отличается на минуту, иначе
# скопировать файл в эту папку
# os.chdir(path_folders)
# os.mkdir(str(first_folder))

for photo in all_photo:
    photo_presnt=photo

    if photo_previos=='':
        os.chdir(path_folders)
        os.mkdir(str(first_folder))
        os.chdir(str(first_folder))
        shutil.copy(str(file_path)+'/'+str(photo_presnt),str(photo_presnt))

    elif os.path.getmtime(str(file_path)+'/'+str(photo_presnt))-os.path.getmtime(str(file_path)+'/'+str(photo_previos))<=10 :
        shutil.copy(str(file_path) + '/' + str(photo_presnt),  str(photo_presnt))

    else:
        count+=1
        os.chdir(path_folders)
        os.mkdir(str(count))
        os.chdir(str(count))
        shutil.copy(str(file_path) + '/' + str(photo_presnt), str(photo_presnt))
    photo_previos = photo_presnt



print(os.path.getmtime('/home/laim/Downloads/sample_photo/24_09_2021_DJI_P4V2_OBJ_f001_0001.JPG'))
print(os.path.getmtime('/home/laim/Downloads/sample_photo/24_09_2021_DJI_P4V2_OBJ_f001_0002.JPG'))
print(time.gmtime(os.path.getmtime('/home/laim/Downloads/sample_photo/24_09_2021_DJI_P4V2_OBJ_f001_0001.JPG')))
#os.popen('/home/laim/Downloads/sample_photo/24_09_2021_DJI_P4V2_OBJ_f001_0001.JPG /home/laim/Downloads/fg.JPG')
# shutil.copy('/home/laim/Downloads/sample_photo/24_09_2021_DJI_P4V2_OBJ_f001_0001.JPG', '/home/laim/Downloads/fg.JPG')