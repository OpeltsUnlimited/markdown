'''
    os.path.exists
    os.listdir
    os.path.join
    os.path.isfile
    os.mkdir
    shutil.copy
    shutil.rmtree

'''

import os
import shutil

def copy_Recursive(source_dir, target_dir):
    dir_list = os.listdir(source_dir)
    for entry in dir_list:
        source_path = os.path.join(source_dir,entry)
        target_path = os.path.join(target_dir,entry)
        if os.path.isfile(source_path):
            shutil.copy(source_path,target_path)
        else:
            os.mkdir(target_path)
            copy_Recursive(source_path, target_path)

def my_copy(source_dir, target_dir):
    try:
         shutil.rmtree(target_dir)
    except FileNotFoundError:
         pass
    os.mkdir(target_dir)
    copy_Recursive(source_dir, target_dir)
    print(os.listdir(source_dir))