###############################################################################
#   File name:   account.py
#   Description: 账户相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
import asyncio
###############################################################################
# Function:     get_login_info
# Input:        void    
# Notice:       回复是一个json字典
###############################################################################
async def get_login_info(self):
    '''shamrockAPI, 获取当前账号信息'''
    pld = payload(self.websocket, self.accessToken, "/get_login_info")
    return await pld.post()

###############################################################################
# Function:     set_qq_profile 
# Input:        @nickname 昵称
#               @company 公司
#               @email 邮箱
#               @college 大学
#               @personal_note 个人备注
#               @age 年龄
#               @birthday 生日（格式：YYYY-MM-DD      
# Notice:       
###############################################################################
async def set_qq_profile(self, nickname: str, company: str, email: str, college: str, personal_note: str, age: int, birthday: str):
    """shamrockAPI, 设置QQ基本信息"""    

    pld = payload(self.websocket, self.accessToken, "/set_qq_profile")
    pld.argAdd("nickname", nickname)
    pld.argAdd("company", company)
    pld.argAdd("email", email)
    pld.argAdd("college", college)
    pld.argAdd("personal_note", personal_note)
    pld.argAdd("age", age)
    pld.argAdd("birthday", birthday)

    return await pld.post()

###############################################################################
# Function:     get_model_show
# Input:        @model 手机机型    
# Notice:       
###############################################################################
async def get_model_show(self, model: str):
    '''shamrockAPI, 获取 QQ 在线机型(似乎没什么用)'''

    pld = payload(self.websocket, self.accessToken, "/_get_model_show")
    pld.argAdd("model", model)

    return await pld.post()

###############################################################################
# Function:     set_model_show
# Input:        @model 手机机型
#               @manu 厂商      
# Notice:       
###############################################################################
async def set_model_show(self, model: str, manu: str):
    '''
    shamrockAPI, 设置 QQ 在线机型
    :param model: 手机机型
    :param manu: 厂商
    '''
    pld = payload(self.websocket, self.accessToken, "/_set_model_show")
    pld.argAdd("model", model)
    pld.argAdd("manu", manu)

    return await pld.post()

###############################################################################
# Function:     get_online_clients
# Input:        @no_cache 是否无视缓存     
# Notice:       
###############################################################################
async def get_online_clients(self, no_cache: bool):
    '''shamrockAPI, 获取当前账号在线客户端列表'''
    raise TypeError("shamrock暂未实现该API")

    pld = payload(self.websocket, self.accessToken, "/get_online_clients")
    pld.argAdd("no_cache", no_cache)

    return await pld.post()