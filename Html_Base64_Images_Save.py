import os, base64, re
from lxml import etree


def Html_Base64_Images_Save(htmlFilePath: str, imagesSavePath: str, imagesLetterName='', imageMinWidth=None, imageMinheight=None):
    """
    1、提取HTML图片

    :param htmlFilePath: HTML文件路径
    :param imagesSavePath: 图片保存路径
    :param imagesLetterName: 图片前缀命名
    :param imageMinWidth: 最小图片宽度
    :param imageMinheight: 最小图片高度
    :return:
    """

    if not os.path.isfile(htmlFilePath):
        return '非HTML文件路径'
    if not os.path.isdir(imagesSavePath):
        return '非目录路径'

    # 读取HTML文件
    try:
        html = etree.parse(htmlFilePath, parser=etree.HTMLParser(encoding='utf-8'))
    except Exception:
        return '读取失败'

    # 图片顺序
    imgIndexInt = 0
    # 文档中的所有图片路径
    imgList = html.xpath('//img')
    for i in imgList:
        # 低于最小尺寸的图片不保存
        if isinstance(imageMinWidth, int) and isinstance(imageMinheight, int):
            try:
                width = re.search('\d+', str(i.xpath('./@width'))).group()
                height = re.search('\d+', str(i.xpath('./@height'))).group()
                if int(width) <= imageMinWidth and int(height) <= imageMinheight:
                    continue
            except ArithmeticError:
                pass

        # 图片全称
        imgName = imagesLetterName + str(imgIndexInt) + '.' + (str(
            re.search('data:image/(.*?);', ((str(i.xpath('./@src'))).split(','))[0]).group()
        ).split('/'))[1]
        imgName = re.sub(';', '', imgName)
        # 图片 base64
        imgSrcBase = str(i.xpath('./@src')).split(',')[1]
        # 解码
        imgSrc = base64.b64decode(imgSrcBase)
        # 图片保存
        with open(fr'{imagesSavePath}\{imgName}', 'wb') as f:
            f.write(imgSrc)
        f.close()
        imgIndexInt += 1

    return True
