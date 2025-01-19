###############################################################################
#   File name:   file.py
#   Description: 文件相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..url import shamrockURL
###############################################################################
# Function:     upload_private_file
# Input:        @user_id    目标
#               @file       本地文件路径 或 文件base64 或 文件url 
#               @name       文件名称
# Notice:       本地文件路径为绝对路径，文件base64为base64://开头，文件url则应该是正确的http请求地址
###############################################################################
def upload_private_file(self, user_id: int, file: str, name: str):
    '''shamrockAPI, 上传私聊文件'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/upload_private_file")
    url.argAdd("user_id", user_id)
    url.argAdd("file", file)
    url.argAdd("name", name)

    return url.get()

###############################################################################
# Function:     upload_group_file
# Input:        @group_id    目标
#               @file       本地文件路径 或 文件base64 或 文件url 
#               @name       文件名称
# Notice:       本地文件路径为绝对路径，文件base64为base64://开头，文件url则应该是正确的http请求地址
###############################################################################
def upload_group_file(self, group_id: int, file: str, name: str):
    '''shamrockAPI, 上传群文件'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/upload_group_file")
    url.argAdd("group_id", group_id)
    url.argAdd("file", file)
    url.argAdd("name", name)

    return url.get()

###############################################################################
# Function:     delete_group_file
# Input:        @group_id   群号
#               @file_id	文件ID 参考 File 对象   
#               @busid      文件类型 参考 File 对象
# Notice:       
###############################################################################
def delete_group_file(self, group_id: int, file_id: str, busid: int):
    '''shamrockAPI, 删除群文件'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/delete_group_file")
    url.argAdd("group_id", group_id)
    url.argAdd("file_id", file_id)
    url.argAdd("busid", busid)

    return url.get()

###############################################################################
# Function:     create_group_file_folder
# Input:        @group_id   群号
#               @name       群文件夹名字   
# Notice:       仅能在根目录创建文件夹
###############################################################################
def create_group_file_folder(self, group_id: int, name: str):
    '''shamrockAPI, 创建群文件文件夹'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/create_group_file_folder")
    url.argAdd("group_id", group_id)
    url.argAdd("name", name)

    return url.get()

###############################################################################
# Function:     rename_group_folder
# Input:        @group_id   群号
#               @folder_id	群文件夹ID
#               @name      群文件夹名字
# Notice:       
###############################################################################
def rename_group_folder(self, group_id: int, folder_id: str, name: str):
    '''shamrockAPI, 重命名群文件夹'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/rename_group_folder")
    url.argAdd("group_id", group_id)
    url.argAdd("folder_id", folder_id)
    url.argAdd("name", name)

    return url.get()

###############################################################################
# Function:     delete_group_folder
# Input:        @group_id   群号
#               @folder_id	文件夹ID 参考 Folder 对象
# Notice:       
###############################################################################
def delete_group_folder(self, group_id: int, folder_id: str):
    '''shamrockAPI, 删除群文件夹'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/delete_group_folder")
    url.argAdd("group_id", group_id)
    url.argAdd("folder_id", folder_id)

    return url.get()

###############################################################################
# Function:     get_group_file_system_info
# Input:        @group_id   群号 
# Notice:       
###############################################################################
def get_group_file_system_info(self, group_id: int):
    '''shamrockAPI, 获取群文件系统信息,例如文件总数,已使用空间'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_group_file_system_info")
    url.argAdd("group_id", group_id)

    return url.get()

###############################################################################
# Function:     get_group_root_files
# Input:        @group_id   群号 
# Notice:       
###############################################################################
def get_group_root_files(self, group_id: int):
    '''shamrockAPI, 获取群根目录文件列表'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_group_root_files")
    url.argAdd("group_id", group_id)

    return url.get()

###############################################################################
# Function:     get_group_files_by_folder
# Input:        @group_id   群号
#               @folder_id	文件夹ID 参考 Folder 对象
# Notice:       
###############################################################################
def get_group_files_by_folder(self, group_id: int, folder_id: str):
    '''shamrockAPI, 获取群子目录文件列表'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_group_files_by_folder")
    url.argAdd("group_id", group_id)
    url.argAdd("folder_id", folder_id)

    return url.get()

###############################################################################
# Function:     get_group_file_url
# Input:        @group_id   群号
#               @file_id	文件ID 参考 File 对象
#               @busid      文件类型 参考 File 对象
# Notice:       
###############################################################################
def get_group_file_url(self, group_id: int, file_id: str, busid: str):
    '''shamrockAPI, 获取群文件资源链接'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_group_file_url")
    url.argAdd("group_id", group_id)
    url.argAdd("file_id", file_id)
    url.argAdd("busid", busid)

    return url.get()