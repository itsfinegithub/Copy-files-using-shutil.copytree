
from zipfile import ZipFile
import os
import shutil



def unzip():
    with ZipFile('/home/ubuntu/Downloads/tiny_shoppee_train.zip')as zip:
        zip.extractall()
        

    src = '/home/ubuntu/Desktop/tiny_shoppee_train'
    dest = '/home/ubuntu/Desktop/newfolder'
    destination = shutil.copytree(src, dest) 
    shutil.make_archive('newfolder1','zip','newfolder')

if __name__ == '__main__':
    unzip()








































    
  