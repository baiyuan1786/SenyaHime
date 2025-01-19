###############################################################################
#   File name:   handle.py
#   Description: 处理相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
import asyncio
###############################################################################
# Function:     set_friend_add_request
# Input:        @flag 好友申请标记
#               @approve 是否同意申请
#               @remark 好友备注      
# Notice:       
###############################################################################
async def set_friend_add_request(self, flag: str, approve: bool, remark: str):
    '''shamrockAPI, 处理加好友请求'''
    pld = payload(self.websocket, self.accessToken, "/set_friend_add_request")
    pld.argAdd("flag", flag)
    pld.argAdd("approve", approve)
    pld.argAdd("remark", remark)

    return await pld.post()

###############################################################################
# Function:     set_group_add_request
# Input:        @flag 加群申请标记
#               @type（sub_type） add 或 invite, 请求类型（需要和上报消息中的 sub_type 字段相符）
#               @approve 是否同意请求／邀请
#               @reason 拒绝理由（仅在拒绝时有效）      
# Notice:       该功能可能存在bug
###############################################################################
async def set_group_add_request(self, flag: str, type: str, approve: bool, reason: str):
    '''shamrockAPI, 处理加群请求'''
    pld = payload(self.websocket, self.accessToken, "/set_group_add_request")
    pld.argAdd("flag", flag)
    pld.argAdd("type", type)
    pld.argAdd("approve", approve)
    pld.argAdd("reason", reason)

    return await pld.post()