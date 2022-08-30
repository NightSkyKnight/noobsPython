import zipfile, os, subprocess


def Compression_File(filePath: str, saveFilePath: str):
    """
    1、压缩路径下的所有文件与目录

    2、zipfile包无法加密压缩包

    :param filePath: 需要压缩的路径
    :param saveFilePath: 保存路径
    :return: 压缩好的路径
    """

    # 压缩路径是否是目录
    directoryBool = True
    # 被压缩文件是目录
    if os.path.isdir(filePath):
        # 名称
        newName = os.path.split(filePath)[1]
        directoryBool = True
    else:
        # 去掉后缀并获取名称
        newName = os.path.split(os.path.splitext(filePath)[0])[1]
        directoryBool = False

    # 保存位置为目录
    if os.path.isdir(saveFilePath):
        # 目录
        newSaveZipPath = saveFilePath
    else:
        # 文件所处目录
        newSaveZipPath = os.path.split(saveFilePath)[0]

    # 创建压缩文件
    zipFile = zipfile.ZipFile(fr'{newSaveZipPath}\{newName}.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)

    # 写入
    if directoryBool:
        os.chdir(filePath)
        # 遍历所有目录 父层、当前层目录、当前层文件
        for directoryPath, directoryPath_, files in os.walk('.'):
            # 当前目录下的文件
            for file in files:
                # 不压缩自己
                if fr'{newName}.zip' == file:
                    continue
                # 系统文件跳过
                if '.db' in str(file) or '.ini' in str(file):
                    continue
                else:
                    # 压缩
                    zipFile.write(fr'{directoryPath}\{file}')
    else:
        os.chdir(os.path.split(filePath)[0])
        zipFile.write(fr'.\{os.path.split(filePath)[1]}')
    # 关闭
    zipFile.close()

    return fr'{newSaveZipPath}\{newName}.zip'


def Compression_File_(filePathList: list, saveFileName: str, saveFilePath: str):
    """
    1、单文件循环压缩

    :param filePathList: 需要压缩的文件路径列表
    :param saveFileName: 压缩包名称
    :param saveFilePath: 压缩包保存路径
    :return:
    """

    # 保存位置为目录
    if os.path.isdir(saveFilePath):
        # 目录
        newSaveZipPath = saveFilePath
    else:
        # 文件所处目录
        newSaveZipPath = os.path.split(saveFilePath)[0]

    # 创建压缩文件
    zipFile = zipfile.ZipFile(fr'{newSaveZipPath}\{saveFileName}.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9)

    for file in filePathList:
        if os.path.isfile(file):
            # 文件路径，文件全称
            filePath, fileName = os.path.split(file)
            os.chdir(filePath)
            zipFile.write(fr'.\{fileName}')

    return fr'{newSaveZipPath}\{saveFileName}.zip'


def Compression_File_Password(filePathList: list, saveFileName: str, saveFilePath: str, filePassword: str):
    """
    1、使用winRAR命令行压缩并加密

    :param filePathList: 需要压缩的文件或者文件目录路径列表
    :param saveFileName: 压缩包名称
    :param saveFilePath: 压缩包保存路径
    :param filePassword: 压缩包密码
    :return: 压缩包完整路径
    """

    # 新文件路径列表
    filePathNewList = []
    for filePath in filePathList:
        if os.path.isdir(filePath):
            # 文件夹目录则添加斜杆
            filePathNewList.append(f'{filePath}\\')
        else:
            filePathNewList.append(filePath)
    # 每个路径用双引号和空格隔开
    filePathListStr = '" "'.join(filePathNewList)

    # -r 递归子文件夹
    # -ep1 从名称中排除基本目录
    # -ibck 后台运行
    # -m2 快速压缩方法
    cmd = fr'winRAR a -r -ep1 -ibck "{saveFilePath}\{saveFileName}.zip" "{filePathListStr}" -hp{filePassword} -m2'
    (subprocess.Popen(cmd, executable=r'C:\Program Files\WinRAR\WinRAR.exe')).wait()

    return fr'{saveFilePath}\{saveFileName}.zip'


if __name__ == '__main__':
    # Compression_File_Password(
    #     filePathList=[
    #         r'G:\BaiduNetdiskDownload\A\新建文件夹\新建文件夹',
    #         r'C:\Users\Adminitrator03\Desktop\百家号.xlsx',
    #     ],
    #     saveFilePath=r'\\hwindows\公用2', filePassword=123, saveFileName='新建文件夹'
    # )
    pass
