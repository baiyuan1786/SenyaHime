###############################################################################
#   File name:   resource.py
#   Description: 资源相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..url import shamrockURL
from typing import Literal
###############################################################################
# Function:     get_image
# Input:        @file 文件MD5     
# Notice:       只能获取已经缓存的图片
###############################################################################
def get_image(self, fileMD5: str):
    '''shamrockAPI, 获取图片,只能获取已经缓存的图片'''
    url = shamrockURL(self.baseURL, self.accessToken, "/get_image")
    url.argAdd("file", fileMD5)

    return url.get()

###############################################################################
# Function:     can_send_image
# Input:            
# Notice:       只能获取已经缓存的图片
###############################################################################
def can_send_image(self):
    '''shamrockAPI, 判断是否可以发送图片'''
    raise TypeError("shamrock暂未实现该API")
    url = shamrockURL(self.baseURL, self.accessToken, "/can_send_image")

    return url.get()

###############################################################################
# Function:     ocr_image
# Input:        @image     
# Notice:       只能获取已经缓存的图片
###############################################################################
def ocr_image(self, image: str):
    '''shamrockAPI, 图片 OCR'''
    raise TypeError("shamrock暂未实现该API")
    url = shamrockURL(self.baseURL, self.accessToken, "/ocr_image")
    url.argAdd("image", image)

    return url.get()

###############################################################################
# Function:     can_send_record
# Input:        @file 文件MD5     
# Notice:       只能获取已经缓存的图片
###############################################################################
def can_send_record(self):
    '''shamrockAPI, 检查是否可以发送语音'''
    raise TypeError("shamrock暂未实现该API")
    url = shamrockURL(self.baseURL, self.accessToken, "/can_send_record")

    return url.get()

###############################################################################
# Function:     get_record
# Input:        @file 文件MD5     
# Notice:       需要安装ffmpeg
###############################################################################
def get_record(self, file: str, out_format: str = Literal["mp3", "amr", "wma", "m4a", "spx", "ogg", "wav", "flac"]):
    '''shamrockAPI, 获取语音'''
    url = shamrockURL(self.baseURL, self.accessToken, "/get_record")
    url.argAdd("file", file)
    url.argAdd("out_format", out_format)

    return url.get()

###############################################################################
# Function:     get_file
# Input:        @file 文件MD5
#               @file_type 文件类型     
# Notice:       需要安装ffmpeg
###############################################################################
def get_file(self, file: str, file_type: str):
    '''shamrockAPI, 获取某文件'''
    url = shamrockURL(self.baseURL, self.accessToken, "/get_file")
    url.argAdd("file", file)
    url.argAdd("file_type", file_type)

    return url.get()