import os

searchPath = input('搜索路径：')
searchKey = input('搜索关键词：')
# 父层、当前层目录、当前层文件
for directoryPath, directoryPath_, files in os.walk(searchPath):
    for file in files:
        try:
            with open(fr'{directoryPath}\{file}', 'rb') as f:
                fileOpen = f.read()
            f.close()
            if searchKey in str(fileOpen):
                print(fr'在这个文件中找到：{directoryPath}\{file}')
        except Exception:
            print(fr'无法打开并读取该文件：{directoryPath}\{file}')
