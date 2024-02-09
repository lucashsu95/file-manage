import os
import shutil

dir_path = os.getcwd()

if os.path.isdir(dir_path):
    files = sorted([f for f in os.listdir() if os.path.isfile(f) and f not in ('README.md', 'before.py', 'after.py')])

    for fileName in files:
        before = fileName.split('.')[0]
        if before not in os.listdir():
            os.mkdir(before)
        shutil.move(fileName, before)

    print('檔案整理完成！')
else:
    print('沒有檔案')
