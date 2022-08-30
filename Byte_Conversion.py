def Byte_Conversion(size: int or float):
    """
    1、字节数转换为占用空间大小

    :param size: 字节数
    :return:
    """

    # 单位
    unitList = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    for index in range(len(unitList)):
        if size / 1024.0 < 1:
            # 保留2位小数点
            return f'{round(size, 2)}:{unitList[index]}'
        size /= 1024.0
