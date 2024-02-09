import os
import shutil

# 定義檔案擴展名和對應的類別
file_extensions = {
    'pdf': 'PDF', 'png': '圖片', 'jpg': '圖片', 'jpeg': '圖片', 'gif': '圖片',
    'doc': '文件', 'docx': '文件', 'csv': '文件', 'xlsx': 'Excel', 'pptx': 'PowerPoint',
    'ini': '設定檔', 'txt': '文字檔', 'srt': '文字檔', 'zip': '壓縮檔', 'rar': '壓縮檔',
    'exe': '執行檔', 'wav': '音樂', 'mp3': '音樂', 'mp4': '影片', 'avi': '影片',
    'flv': '影片', 'wmv': '影片', 'webm': '影片', 'ai': 'Illustrator', 'psd': 'Photoshop',
    # 新增其他檔案樣例
    'html': '網頁', 'css': '網頁', 'js': '網頁', 'php': 'PHP檔案',
}

# 定義要忽略的檔案列表
ignore_files = ('README.md', 'before.py', 'after.py')

dir_path = os.getcwd()

if os.path.isdir(dir_path):
    for file_name in os.listdir():
        # 忽略要忽略的檔案
        if file_name in ignore_files:
            continue
        if os.path.isfile(file_name):
            extension = file_name.split('.')[-1].lower()
            folder = file_extensions.get(extension, '其他')
            if not os.path.exists(folder):
                os.mkdir(folder)
            shutil.move(file_name, folder)
    print('檔案整理完成！')
else:
    print('目錄不存在。')
