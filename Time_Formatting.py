import time, datetime


def Timestamp(initialTimestamp: int) -> str:
    """
    1、时间戳转为日期时间格式
    :param initialTimestamp: 初始时间戳
    :return: 日期时间格式
    """

    if len(str(initialTimestamp)) > 10:
        return '输入时间长度不正确'
    # 时间元组
    timeArray = time.localtime(initialTimestamp)

    return time.strftime('%Y-%m-%d %H:%M:%S', timeArray)


def Strftime(initialTimeStr: str) -> int:
    """
    1、日期时间格式转换为时间戳

    :param initialTimeStr: 初始日期时间格式
    :return: 时间戳
    """

    # 时间元组
    try:
        timeArray = time.strptime(initialTimeStr, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        timeArray = time.strptime(initialTimeStr, '%Y-%m-%d')

    return int(time.mktime(timeArray))
