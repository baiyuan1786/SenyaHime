###############################################################################
#   File name:   media.py
#   Description: 媒体类型消息, 包括图片, 语音和视频消息
#                对于下述消息类型, 涉及 文件地址 的参数规则如下:
#                可以是本地文件路径, 以 file:// 开头。
#                可以是 http(s) 链接, 以 http:// 或 https:// 开头。
#                可以是 base64 编码的数据, 但是必须以 base64:// 开头。
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .messageSegment import messageSegment
import os
import base64

###############################################################################
# Function:    imageToBase64
# Input:       @image_path (str) - 图片文件的路径
# Notice:      支持常见的图片格式，如 JPG、PNG 等
###############################################################################
def imageToBase64(image_path: str) -> str:
    '''将本地的一张图片转换为base64格式'''

    with open(image_path, "rb") as image_file:
        # 读取图片文件并进行 Base64 编码
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return r"base64://" + encoded_string

###############################################################################
# Class:        image     
# Input:        @file       图片文件地址
#               @url        图片链接地址
#               @type       图片类型, 分为show, flash, original
#               @subType    图片子类型
# Notice:       当 qq 字段为 "0"或"all" 时, 表示 image 全体成员
#               value	图片子类型说明
#               0	正常图片
#               1	表情包, 在客户端会被分类到表情包图片并缩放显示
#               2	热图
#               3	斗图
#               4	智图?
#               7	贴图
#               8	自拍
#               9	贴图广告?
#               10	有待测试
#               13	热搜图
###############################################################################
class image(messageSegment):
    '''图片类型消息'''
    def __init__(self, file: str | None, url: str | None = None, type: str | None = None, subType: str | None = None):
        """图片类型消息

        :param file: 图片文件地址,可以是本地文件路径,http(s) 链接,base64 编码的数据
        :param url: 图片链接地址
        :param type: 图片类型, 分为show, flash, original
        :param subType: 推荐0正常图片, 1表情包
        """

        # 如果使用本地路径, 转换为base64
        if os.path.exists(file):
            file = imageToBase64(image_path = file)
        super().__init__(type = "image", data = {"file": file, "url": url, "type": type, "subType": subType }, msgType = "image")    

###############################################################################
# Class:        record     
# Input:        @file       语音文件地址
#               @url        语音链接地址
#               @magic      是否为魔法语音
# Notice:       发送语音消息需要安装语音引擎，可以在 这里 查看。
###############################################################################
class record(messageSegment):
    '''语音类型消息'''
    def __init__(self, file: str, url: str | None = None, magic: str | None = None):
        """语音类型消息

        :param file: 语音文件地址
        :param url: 语音链接地址, defaults to None
        :param magic: 是否为魔法语音, defaults to None
        """        
        super().__init__(type = "record", data = {"file": file, "url": url, "magic": magic}, msgType = "record")

###############################################################################
# Class:        video     
# Input:        @file       视频文件地址
# Notice:
###############################################################################
class video(messageSegment):
    '''视频类型消息'''
    def __init__(self, file: str):
        super().__init__(type = "video", data = {"file": file}, msgType = "video")