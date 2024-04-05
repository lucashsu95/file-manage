import inquirer
import os

files = [f for f in os.listdir() if os.path.isfile(f)]

questions = [
    inquirer.Checkbox('options',
                      message="請選擇不要被分類的檔案:",
                      choices=files,
                  ),
]

answers = inquirer.prompt(questions)
ignore_files = answers['options']
print(ignore_files)
