# file-manage

這一個用python做的簡單的檔案分類器
## after.py

這個檔會依照**檔案名稱**生成資料夾，再把檔案放進資料夾

## before.py

這個檔會依照**檔案的副檔名**生成資料夾，再把檔案放進資料夾

## 使用pyinstaller

```sh
pip install pyinstaller
```

```sh
pyinstaller -F --name=檔案分類器 main.py
```


## 常用參數介紹
1. pyinstaller -h 來查看參數
2. -F 打包成一個exe文件
3. –icon=圖標路徑
4. -w 使用視窗，無控制台
5. -c 使用控制台，無視窗
6. -D 創建一個目錄，包含exe以及其他一些依賴性文件