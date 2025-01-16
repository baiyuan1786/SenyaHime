###############################################################################
#   File name:   shamrock.py
#   Description: shamrock相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..url import shamrockURL
###############################################################################
# Function:     switch_account
# Input:        @user_id   
# Notice:       返回是是否正常执行切换账号请求的响应。
###############################################################################
def switch_account(self, user_id: int):
    '''shamrockAPI, 切换当前shamrockQQ号'''
    url = shamrockURL(self.baseURL, self.accessToken, "/switch_account")
    url.argAdd("user_id", user_id)

    return url.get()

###############################################################################
# Function:     upload_file
# Input:        @user_id   
# Notice:       
###############################################################################
def upload_file(self, filePath: str):
    '''shamrockAPI, 上传文件到缓存目录,输入的file是文件路径'''
    url = shamrockURL(self.baseURL, self.accessToken, "/upload_file")
    url.argAdd("file", filePath)

    return url.post()

###############################################################################
# Function:     download_file
# Input:        @url    下载地址
#               @name   文件名称
#               @root   保存文件的根目录
#               @base64 文件base64内容
#               @thread_cnt 下载的线程数量
#               @headers    请求头
# Notice:       "headers": "User-Agent=YOUR_UA[\r\n]Referer=https://www.baidu.com"
###############################################################################
def download_file(self, url: str, name: str, root: str, base64: str, thread_cnt: int, headers: str, ):
    '''shamrockAPI, Shamrock下载文件到缓存目录'''
    url = shamrockURL(self.baseURL, self.accessToken, "/download_file")
    url.argAdd("url", url)
    url.argAdd("name", name)
    url.argAdd("root", root)
    url.argAdd("base64", base64)
    url.argAdd("thread_cnt", thread_cnt)
    url.argAdd("headers", headers)

    return url.post()

###############################################################################
# Function:     clean_cache
# Input:        void  
# Notice:       
###############################################################################
def clean_cache(self):
    '''shamrockAPI, 清除当前shamrock缓存'''
    url = shamrockURL(self.baseURL, self.accessToken, "/clean_cache")

    return url.get()

###############################################################################
# Function:     get_device_battery
# Input:        void   
# Notice:       
###############################################################################
def get_device_battery(self, file: str):
    '''shamrockAPI, 获取手机电池信息'''
    url = shamrockURL(self.baseURL, self.accessToken, "/get_device_battery")

    return url.get()

###############################################################################
# Function:     get_start_time
# Input:        void   
# Notice:       
###############################################################################
def get_start_time(self, file: str):
    '''shamrockAPI, 获取Shamerock启动时间'''
    url = shamrockURL(self.baseURL, self.accessToken, "/get_start_time")

    return url.get()

###############################################################################
# Function:     log
# Input:        @start    开始的行	
#               @recent   是否只显示最近的日志	 
# Notice:       
###############################################################################
def log(self, start: int, recent: bool):
    '''shamrockAPI, 获取Shamrock日志'''
    url = shamrockURL(self.baseURL, self.accessToken, "/log")
    url.argAdd("start", start)
    url.argAdd("recent", recent)

    return url.get()

###############################################################################
# Function:     shut
# Input:        void 
# Notice:       
###############################################################################
def shut(self):
    '''shamrockAPI, 关闭Shamrock'''
    url = shamrockURL(self.baseURL, self.accessToken, "/shut")

    return url.get()

###############################################################################
# Function:     get_supported_actions
# Input:        void 
# Notice:       
###############################################################################
def get_supported_actions(self):
    '''shamrockAPI, 获取所有支持的动作'''
    url = shamrockURL(self.baseURL, self.accessToken, "/get_supported_actions")

    return url.get()