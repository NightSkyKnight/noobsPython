from moviepy.editor import VideoFileClip
import os, re


def Clip_Video(videoFilePath: str, videoTimeStr: str, videoSavePath: str) -> bool or str:
    """
    1、剪辑视频

    2、10:10-20:20（输出这个区间的视频）

    3、10:10>（此时间直到结尾）

    4、<20:20（开头直到此时间）

    :param videoFilePath: 源视频文件路径
    :param videoTimeStr: 剪辑时间格式
    :param videoSavePath: 剪辑好的视频保存文件路径
    :return:
    """

    # 读取视频
    video = VideoFileClip(videoFilePath)

    # 开始时间 结束时间
    startTimeSendStr, endTimeSendStr = '', ''
    # 10:10-20:20（输出这个区间的视频）
    if '-' in videoTimeStr:
        # 分离开始时间和结束时间
        timeTuple = re.findall('(.*)-(.*)', videoTimeStr)[0]
        # 遍历每个时间
        for j in timeTuple:
            # 获取时与分
            timeTuple_ = re.findall('(.*):(.*)', j)[0]

            # 1小时以下
            if len(timeTuple_) >= 2 < 3:
                if startTimeSendStr == '':
                    # 开始的秒
                    startTimeSendStr = int(timeTuple_[0]) * 60 + int(timeTuple_[1])
                else:
                    # 结束的秒
                    endTimeSendStr = int(timeTuple_[0]) * 60 + int(timeTuple_[1])
            # 1小时以上
            elif len(timeTuple_) >= 3:
                if startTimeSendStr == '':
                    # 开始的秒
                    startTimeSendStr = int(timeTuple_[0]) * 60 * 60 + int(timeTuple_[1]) * 60 + int(timeTuple_[2])
                else:
                    # 结束的秒
                    endTimeSendStr = int(timeTuple_[0]) * 60 * 60 + int(timeTuple_[1]) * 60 + int(timeTuple_[2])
            else:
                return '时间错误'

    # 10:10>（此时间直到结尾）
    elif '>' in videoTimeStr:
        # 获取时与分
        timeTuple_ = re.findall('(.*):(.*)', re.sub('>', '', videoTimeStr))[0]

        # 1小时以下
        if len(timeTuple_) >= 2 < 3:
            # 开始的秒
            startTimeSendStr = int(timeTuple_[0]) * 60 + int(timeTuple_[1])
        # 1小时以上
        elif len(timeTuple_) >= 3:
            # 开始的秒
            startTimeSendStr = int(timeTuple_[0]) * 60 * 60 + int(timeTuple_[1]) * 60 + int(timeTuple_[2])
        else:
            return '时间错误'

        # 结束的秒等于视频结束时间
        endTimeSendStr = int(video.end)

    # <20:20（开头直到此时间）
    elif '<' in videoTimeStr:
        # 获取时与分
        timeTuple_ = re.findall('(.*):(.*)', re.sub('<', '', videoTimeStr))[0]

        if len(timeTuple_) >= 2 < 3:
            # 结束的秒
            endTimeSendStr = int(timeTuple_[0]) * 60 + int(timeTuple_[1])
        elif len(timeTuple_) >= 3:
            # 结束的秒
            endTimeSendStr = int(timeTuple_[0]) * 60 * 60 + int(timeTuple_[1]) * 60 + int(timeTuple_[2])
        else:
            return '时间错误'

        # 开始的秒等于视频开始时间
        startTimeSendStr = int(video.start)

    else:
        return '输入的时间格式不正确 -> 参考：10:10-20:20 or 10:10> or <20:20'

    # 剪辑
    if startTimeSendStr != '' and endTimeSendStr != '':
        # 剪辑
        video_ = video.subclip(startTimeSendStr, endTimeSendStr)
        # 保存
        if os.path.isdir(videoSavePath):
            video_.write_videofile(
                fr'{videoSavePath}\{str(os.path.split(video.filename)[1])}', threads=16, fps=int(video_.fps)
            )
        elif os.path.isfile(videoSavePath):
            video_.write_videofile(
                videoSavePath, threads=16
            )
        else:
            return '视频保存路径不正确'

    return True


if __name__ == '__main__':
    # Clip_Video(
    #     videoFilePath=r'视频.mp4',
    #     videoTimeStr='2:10-3:10', videoSavePath=r'C:\Users\Adminitrator\Desktop'
    # )
    pass
