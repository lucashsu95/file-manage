import os
import shutil

def before_files():
    dir_path = os.getcwd()

    if os.path.isdir(dir_path):
        ignore_files = ('before.py', 'after.py', 'main.py','檔案分類器.exe')
        files = sorted([f for f in os.listdir() if os.path.isfile(f) and f not in ignore_files])

        for fileName in files:
            before = fileName.split('.')[0]
            if before not in os.listdir():
                os.mkdir(before)
            shutil.move(fileName, before)

        print('檔案整理完成！')
    else:
        print('沒有檔案')

if __name__ == '__main__':
    before_files()