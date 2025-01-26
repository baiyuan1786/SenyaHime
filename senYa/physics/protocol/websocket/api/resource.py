###############################################################################
#   File name:   resource.py
#   Description: 资源相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
import asyncio
from typing import Literal
###############################################################################
# Function:     get_image
# Input:        @file 文件MD5     
# Notice:       只能获取已经缓存的图片
###############################################################################
async def get_image(self, fileMD5: str):
    '''shamrockAPI, 获取图片,只能获取已经缓存的图片'''
    pld = payload(self.websocket, self.accessToken, "/get_image")
    pld.argAdd("file", fileMD5)

    return await pld.post()

###############################################################################
# Function:     can_send_image
# Input:            
# Notice:       只能获取已经缓存的图片
###############################################################################
async def can_send_image(self):
    '''shamrockAPI, 判断是否可以发送图片'''
    raise TypeError("shamrock暂未实现该API")
    pld = payload(self.websocket, self.accessToken, "/can_send_image")

    return await pld.post()

###############################################################################
# Function:     ocr_image
# Input:        @image     
# Notice:       只能获取已经缓存的图片
###############################################################################
async def ocr_image(self, image: str):
    '''shamrockAPI, 图片 OCR'''
    raise TypeError("shamrock暂未实现该API")
    pld = payload(self.websocket, self.accessToken, "/ocr_image")
    pld.argAdd("image", image)

    return await pld.post()

###############################################################################
# Function:     can_send_record
# Input:        @file 文件MD5     
# Notice:       只能获取已经缓存的图片
###############################################################################
async def can_send_record(self):
    '''shamrockAPI, 检查是否可以发送语音'''
    raise TypeError("shamrock暂未实现该API")
    pld = payload(self.websocket, self.accessToken, "/can_send_record")

    return await pld.post()

###############################################################################
# Function:     get_record
# Input:        @file 文件MD5     
# Notice:       需要安装ffmpeg
###############################################################################
async def get_record(self, file: str, out_format: Literal["mp3", "amr", "wma", "m4a", "spx", "ogg", "wav", "flac"]):
    '''shamrockAPI, 获取语音'''
    pld = payload(self.websocket, self.accessToken, "/get_record")
    pld.argAdd("file", file)
    pld.argAdd("out_format", out_format)

    return await pld.post()

###############################################################################
# Function:     get_file
# Input:        @file 文件MD5
#               @file_type 文件类型     
# Notice:       需要安装ffmpeg
###############################################################################
async def get_file(self, file: str, file_type: str):
    '''shamrockAPI, 获取某文件'''
    pld = payload(self.websocket, self.accessToken, "/get_file")
    pld.argAdd("file", file)
    pld.argAdd("file_type", file_type)

    return await pld.post()