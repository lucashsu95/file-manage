import os
import shutil

file_extensions = {
    'pdf': 'PDF',
    'png': '圖片',
    'jpg': '圖片',
    'jpeg': '圖片',
    'gif': '圖片',
    'doc': '文件',
    'docx': '文件',
    'csv': '文件',
    'xlsx': 'Excel',
    'pptx': 'PowerPoint',
    'ini': '設定檔',
    'txt': '文字檔',
    'srt': '文字檔',
    'zip': '壓縮檔',
    'rar': '壓縮檔',
    'exe': '執行檔',
    'wav': '音樂',
    'mp3': '音樂',
    'mp4': '影片',
    'avi': '影片',
    'flv': '影片',
    'wmv': '影片',
    'webm': '影片',
    'ai': 'Illustrator',
    'psd': 'Photoshop',
}

# 取得當前工作目錄
dir_path = os.getcwd()
if(os.path.isdir(dir_path)):

    files = os.listdir()
    print(files)
    
    fileNames = [value for value in files if os.path.isfile(value)]
    extensions = [value.split('.')[-1] for value in files if os.path.isfile(value)]

    for fileName,extension in zip(fileNames,extensions):
        
        try:
            folder = file_extensions[extension]
            if(folder not in files):
                os.mkdir(folder)
                files.append(folder)
            shutil.move(fileName,folder)
            
        except:
            continue

else:
    print('沒有檔案')
