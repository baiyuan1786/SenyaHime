###############################################################################
#   File name:   url.py
#   Description: shamrock的url访问文件
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
import requests
from ...message.msgSeg.base import messageSegment
from plugin.log import logInfo

###############################################################################
# Class:        shamrockURL     
# Input:        @baseURL：基本URL
#               @command: 命令
#               @accessToken：密钥
# Notice:       
###############################################################################
class shamrockURL:
    '''shamrock的URL类'''
    def __init__(self, baseURL: str, accessToken: str | None, command: str) -> None:
        '''初始化url,该初始化不携带参数,需要使用argAdd为命令添加参数'''

        self.url = fr"{baseURL}{command}"
        self.payLoad = {}
        self.argAdd("access_token", accessToken)

    ###############################################################################
    # Function:     argAdd
    # Input:        @argName
    #               @argValue     
    # Notice:       
    ###############################################################################
    def argAdd(self, argName: str, argValue: str | int | messageSegment | None):
        '''为命令添加额外的参数'''
        if argValue is None:
            return
        elif isinstance(argValue, messageSegment):
            self.payLoad[argName] = argValue.toList()
        else:
            self.payLoad[argName] = argValue

    ###############################################################################
    # Function:     post 
    # Input:        void   
    # Notice:
    ###############################################################################    
    def post(self):
        '''使用post方法获取响应'''
        return requests.post(self.url, json = self.payLoad).json()

    ###############################################################################
    # Function:     get 
    # Input:        void
    # Notice:
    ###############################################################################    
    def get(self):
        '''使用get方法获取响应'''

        payloadURL = self.url
        for key, value in self.payLoad.items():
            if isinstance(value, list):
                raise TypeError("列表无法转换为URL格式, 无法使用get")

            if "?" in payloadURL:
                payloadURL += f"&{key}={value}" # 已经有参数
            else:
                payloadURL += f"?{key}={value}" # 没有参数

        return requests.get(payloadURL).json()