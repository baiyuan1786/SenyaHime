###############################################################################
#   File name:   other.py
#   Description: 其他相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..url import shamrockURL
###############################################################################
# Function:     get_weather_city_code
# Input:        @city   城市 
# Notice:       
###############################################################################
def get_weather_city_code(self, city: int):
    '''shamrockAPI, 获取城市ADCode'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_weather_city_code")
    url.argAdd("city", city)

    return url.get()

###############################################################################
# Function:     get_weather
# Input:        @code   ADCode
#               @city   城市   
# Notice:       
###############################################################################
def get_weather(self, code: int, city: str):
    '''shamrockAPI, 获取天气'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_weather")
    url.argAdd("code", code)
    url.argAdd("city", city)

    return url.get()

###############################################################################
# Function:     upload_group_image
# Input:        @pic            图片base64
#               @sender         QQ
#               @troop          图片发送到的群聊
# Notice:       该接口用于上传群聊图片, 注意该接口是上传群消息的图片，不是群文件，也不是群相册。
###############################################################################
def upload_group_image(self, pic: str, sender: int, troop: int):
    '''shamrockAPI, 上传群图片,注意该接口是上传群消息的图片，不是群文件，也不是群相册'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/upload_group_image")
    url.argAdd("pic", pic)
    url.argAdd("sender", sender)
    url.argAdd("troop", troop)

    return url.get()

###############################################################################
# Function:     get_cookies
# Input:        @domain   域名 
# Notice:       
###############################################################################
def get_cookies(self, domain: str):
    '''shamrockAPI, 获取 Cookie'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_cookies")
    url.argAdd("domain", domain)

    return url.get()

###############################################################################
# Function:     get_csrf_token
# Input:        @domain   域名 
# Notice:       
###############################################################################
def get_csrf_token(self, domain: str):
    '''shamrockAPI, 获取 CSRF 令牌'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_csrf_token")
    url.argAdd("domain", domain)

    return url.get()

###############################################################################
# Function:     get_credentials
# Input:        @domain   域名 
# Notice:       
###############################################################################
def get_credentials(self, domain: str):
    '''shamrockAPI, 获取 Cookie 与 CSRF 令牌'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/get_credentials")
    url.argAdd("domain", domain)

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