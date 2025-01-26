###############################################################################
#   File name:   handle.py
#   Description: 处理相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..url import shamrockURL
###############################################################################
# Function:     set_friend_add_request
# Input:        @flag 好友申请标记
#               @approve 是否同意申请
#               @remark 好友备注      
# Notice:       
###############################################################################
def set_friend_add_request(self, flag: str, approve: bool, remark: str):
    '''shamrockAPI, 处理加好友请求'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/set_friend_add_request")
    url.argAdd("flag", flag)
    url.argAdd("approve", approve)
    url.argAdd("remark", remark)

    return url.get()

###############################################################################
# Function:     set_group_add_request
# Input:        @flag 加群申请标记
#               @type（sub_type） add 或 invite, 请求类型（需要和上报消息中的 sub_type 字段相符）
#               @approve 是否同意请求／邀请
#               @reason 拒绝理由（仅在拒绝时有效）      
# Notice:       该功能可能存在bug
###############################################################################
def set_group_add_request(self, flag: str, type: str, approve: bool, reason: str):
    '''shamrockAPI, 处理加群请求'''
    url = shamrockURL(self.baseURL(), self.accessToken, "/set_group_add_request")
    url.argAdd("flag", flag)
    url.argAdd("type", type)
    url.argAdd("approve", approve)
    url.argAdd("reason", reason)

    return url.get()