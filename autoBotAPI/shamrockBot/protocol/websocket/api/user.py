###############################################################################
#   File name:   user.py
#   Description: 用户相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
import asyncio
###############################################################################
# Function:     delete_friend
# Input:        @user_id 用户ID    
# Notice:       
###############################################################################
async def delete_friend(self, user_id: int):
    '''shamrockAPI, 删除好友'''
    raise TypeError("shamrock暂未实现该API")
    pld = payload(self.websocket, self.accessToken, "/delete_friend")
    pld.argAdd("user_id", user_id)

    return await pld.post()

###############################################################################
# Function:     delete_unidirectional_friend
# Input:        @user_id 用户ID    
# Notice:       
###############################################################################
async def delete_unidirectional_friend(self, user_id: int):
    '''shamrockAPI, 删除单向好友'''
    raise TypeError("shamrock暂未实现该API")
    pld = payload(self.websocket, self.accessToken, "/delete_unidirectional_friend")
    pld.argAdd("user_id", user_id)

    return await pld.post()

###############################################################################
# Function:     send_like
# Input:        @user_id 用户ID
#               @times 点赞次数    
# Notice:       
###############################################################################
async def send_like(self, user_id: int, times: int):
    '''shamrockAPI, 点赞资料卡'''
    pld = payload(self.websocket, self.accessToken, "/send_like")
    pld.argAdd("user_id", user_id)
    pld.argAdd("times", times)

    return await pld.post()