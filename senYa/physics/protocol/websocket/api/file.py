###############################################################################
#   File name:   file.py
#   Description: 文件相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
import asyncio
###############################################################################
# Function:     upload_private_file
# Input:        @user_id    目标
#               @file       本地文件路径 或 文件base64 或 文件url 
#               @name       文件名称
# Notice:       本地文件路径为绝对路径，文件base64为base64://开头，文件url则应该是正确的http请求地址
###############################################################################
async def upload_private_file(self, user_id: int, file: str, name: str):
    '''shamrockAPI, 上传私聊文件'''
    pld = payload(self.websocket, self.accessToken, "/upload_private_file")
    pld.argAdd("user_id", user_id)
    pld.argAdd("file", file)
    pld.argAdd("name", name)

    return await pld.post()

###############################################################################
# Function:     upload_group_file
# Input:        @group_id    目标
#               @file       本地文件路径 或 文件base64 或 文件url 
#               @name       文件名称
# Notice:       本地文件路径为绝对路径，文件base64为base64://开头，文件url则应该是正确的http请求地址
###############################################################################
async def upload_group_file(self, group_id: int, file: str, name: str):
    '''shamrockAPI, 上传群文件'''
    pld = payload(self.websocket, self.accessToken, "/upload_group_file")
    pld.argAdd("group_id", group_id)
    pld.argAdd("file", file)
    pld.argAdd("name", name)

    return await pld.post()

###############################################################################
# Function:     delete_group_file
# Input:        @group_id   群号
#               @file_id	文件ID 参考 File 对象   
#               @busid      文件类型 参考 File 对象
# Notice:       
###############################################################################
async def delete_group_file(self, group_id: int, file_id: str, busid: int):
    '''shamrockAPI, 删除群文件'''
    pld = payload(self.websocket, self.accessToken, "/delete_group_file")
    pld.argAdd("group_id", group_id)
    pld.argAdd("file_id", file_id)
    pld.argAdd("busid", busid)

    return await pld.post()

###############################################################################
# Function:     create_group_file_folder
# Input:        @group_id   群号
#               @name       群文件夹名字   
# Notice:       仅能在根目录创建文件夹
###############################################################################
async def create_group_file_folder(self, group_id: int, name: str):
    '''shamrockAPI, 创建群文件文件夹'''
    pld = payload(self.websocket, self.accessToken, "/create_group_file_folder")
    pld.argAdd("group_id", group_id)
    pld.argAdd("name", name)

    return await pld.post()

###############################################################################
# Function:     rename_group_folder
# Input:        @group_id   群号
#               @folder_id	群文件夹ID
#               @name      群文件夹名字
# Notice:       
###############################################################################
async def rename_group_folder(self, group_id: int, folder_id: str, name: str):
    '''shamrockAPI, 重命名群文件夹'''
    pld = payload(self.websocket, self.accessToken, "/rename_group_folder")
    pld.argAdd("group_id", group_id)
    pld.argAdd("folder_id", folder_id)
    pld.argAdd("name", name)

    return await pld.post()

###############################################################################
# Function:     delete_group_folder
# Input:        @group_id   群号
#               @folder_id	文件夹ID 参考 Folder 对象
# Notice:       
###############################################################################
async def delete_group_folder(self, group_id: int, folder_id: str):
    '''shamrockAPI, 删除群文件夹'''
    pld = payload(self.websocket, self.accessToken, "/delete_group_folder")
    pld.argAdd("group_id", group_id)
    pld.argAdd("folder_id", folder_id)

    return await pld.post()

###############################################################################
# Function:     get_group_file_system_info
# Input:        @group_id   群号 
# Notice:       
###############################################################################
async def get_group_file_system_info(self, group_id: int):
    '''shamrockAPI, 获取群文件系统信息,例如文件总数,已使用空间'''
    pld = payload(self.websocket, self.accessToken, "/get_group_file_system_info")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     get_group_root_files
# Input:        @group_id   群号 
# Notice:       
###############################################################################
async def get_group_root_files(self, group_id: int):
    '''shamrockAPI, 获取群根目录文件列表'''
    pld = payload(self.websocket, self.accessToken, "/get_group_root_files")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     get_group_files_by_folder
# Input:        @group_id   群号
#               @folder_id	文件夹ID 参考 Folder 对象
# Notice:       
###############################################################################
async def get_group_files_by_folder(self, group_id: int, folder_id: str):
    '''shamrockAPI, 获取群子目录文件列表'''
    pld = payload(self.websocket, self.accessToken, "/get_group_files_by_folder")
    pld.argAdd("group_id", group_id)
    pld.argAdd("folder_id", folder_id)

    return await pld.post()

###############################################################################
# Function:     get_group_file_url
# Input:        @group_id   群号
#               @file_id	文件ID 参考 File 对象
#               @busid      文件类型 参考 File 对象
# Notice:       
###############################################################################
async def get_group_file_url(self, group_id: int, file_id: str, busid: str):
    '''shamrockAPI, 获取群文件资源链接'''
    pld = payload(self.websocket, self.accessToken, "/get_group_file_url")
    pld.argAdd("group_id", group_id)
    pld.argAdd("file_id", file_id)
    pld.argAdd("busid", busid)

    return await pld.post()