###############################################################################
#   File name:   shamrock.py
#   Description: shamrock相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
import asyncio
###############################################################################
# Function:     switch_account
# Input:        @user_id   
# Notice:       返回是是否正常执行切换账号请求的响应。
###############################################################################
async def switch_account(self, user_id: int):
    '''shamrockAPI, 切换当前shamrockQQ号'''
    pld = payload(self.websocket, self.accessToken, "/switch_account")
    pld.argAdd("user_id", user_id)

    return await pld.post()

###############################################################################
# Function:     upload_file
# Input:        @user_id   
# Notice:       
###############################################################################
async def upload_file(self, filePath: str):
    '''shamrockAPI, 上传文件到缓存目录,输入的file是文件路径'''
    pld = payload(self.websocket, self.accessToken, "/upload_file")
    pld.argAdd("file", filePath)

    return await pld.post()

###############################################################################
# Function:     download_file
# Input:        @pld    下载地址
#               @name   文件名称
#               @root   保存文件的根目录
#               @base64 文件base64内容
#               @thread_cnt 下载的线程数量
#               @headers    请求头
# Notice:       "headers": "User-Agent=YOUR_UA[\r\n]Referer=https://www.baidu.com"
###############################################################################
async def download_file(self, pld: str, name: str, root: str, base64: str, thread_cnt: int, headers: str, ):
    '''shamrockAPI, Shamrock下载文件到缓存目录'''
    pld = payload(self.websocket, self.accessToken, "/download_file")
    pld.argAdd("pld", pld)
    pld.argAdd("name", name)
    pld.argAdd("root", root)
    pld.argAdd("base64", base64)
    pld.argAdd("thread_cnt", thread_cnt)
    pld.argAdd("headers", headers)

    return await pld.post()

###############################################################################
# Function:     clean_cache
# Input:        void  
# Notice:       
###############################################################################
async def clean_cache(self):
    '''shamrockAPI, 清除当前shamrock缓存'''
    pld = payload(self.websocket, self.accessToken, "/clean_cache")

    return await pld.post()

###############################################################################
# Function:     get_device_battery
# Input:        void   
# Notice:       
###############################################################################
async def get_device_battery(self, file: str):
    '''shamrockAPI, 获取手机电池信息'''
    pld = payload(self.websocket, self.accessToken, "/get_device_battery")

    return await pld.post()

###############################################################################
# Function:     get_start_time
# Input:        void   
# Notice:       
###############################################################################
async def get_start_time(self, file: str):
    '''shamrockAPI, 获取Shamerock启动时间'''
    pld = payload(self.websocket, self.accessToken, "/get_start_time")

    return await pld.post()

###############################################################################
# Function:     log
# Input:        @start    开始的行	
#               @recent   是否只显示最近的日志	 
# Notice:       
###############################################################################
async def log(self, start: int, recent: bool):
    '''shamrockAPI, 获取Shamrock日志'''
    pld = payload(self.websocket, self.accessToken, "/log")
    pld.argAdd("start", start)
    pld.argAdd("recent", recent)

    return await pld.post()

###############################################################################
# Function:     shut
# Input:        void 
# Notice:       
###############################################################################
async def shut(self):
    '''shamrockAPI, 关闭Shamrock'''
    pld = payload(self.websocket, self.accessToken, "/shut")

    return await pld.post()

###############################################################################
# Function:     get_supported_actions
# Input:        void 
# Notice:       
###############################################################################
async def get_supported_actions(self):
    '''shamrockAPI, 获取所有支持的动作'''
    pld = payload(self.websocket, self.accessToken, "/get_supported_actions")

    return await pld.post()