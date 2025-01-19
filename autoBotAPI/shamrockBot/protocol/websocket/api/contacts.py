###############################################################################
#   File name:   contacts.py
#   Description: 联系人相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
import asyncio
###############################################################################
# Function:     get_stranger_info
# Description:  shamrockAPI, 获取陌生人的信息
# Input:        @user_id QQ号
# Return:       
# Notice:       
###############################################################################
async def get_stranger_info(self, user_id: int):
    '''获取陌生人的信息'''
    pld = payload(self.websocket, self.accessToken, "/get_stranger_info")
    pld.argAdd("user_id", user_id)

    return await pld.post()

###############################################################################
# Function:     get_friend_list
# Description:  shamrockAPI, 获取好友列表
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_friend_list(self):
    '''获取好友列表'''
    pld = payload(self.websocket, self.accessToken, "/get_friend_list")

    return await pld.post()

###############################################################################
# Function:     get_unidirectional_friend_list
# Description:  shamrockAPI, 获取单向好友列表
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_unidirectional_friend_list(self):
    '''获取单向好友列表'''
    pld = payload(self.websocket, self.accessToken, "/get_unidirectional_friend_list")

    return await pld.post()
    
###############################################################################
# Function:     get_group_list
# Description:  shamrockAPI, 获取群列表
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_group_list(self):
    '''获取群列表'''
    pld = payload(self.websocket, self.accessToken, "/get_group_list")

    return await pld.post()

###############################################################################
# Function:     get_group_member_info
# Description:  shamrockAPI, 获取群成员信息
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_group_member_info(self, group_id: int, user_id: int):
    '''获取群成员信息'''
    pld = payload(self.websocket, self.accessToken, "/get_group_member_info")
    pld.argAdd("group_id", group_id)
    pld.argAdd("user_id", user_id)

    return await pld.post()

###############################################################################
# Function:     get_group_member_list
# Description:  shamrockAPI, 获取群成员列表
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_group_member_list(self, group_id: int):
    '''获取群成员列表'''
    pld = payload(self.websocket, self.accessToken, "/get_group_member_list")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     get_group_honor_info
# Description:  shamrockAPI, 获取群荣誉信息
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_group_honor_info(self, group_id: int):
    '''获取群荣誉信息'''
    pld = payload(self.websocket, self.accessToken, "/get_group_honor_info")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     get_group_system_msg
# Description:  shamrockAPI, 获取群系统消息
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_group_system_msg(self):
    '''获取群系统消息'''
    pld = payload(self.websocket, self.accessToken, "/get_group_system_msg")

    return await pld.post()

###############################################################################
# Function:     get_friend_system_msg
# Description:  shamrockAPI, 获取好友系统消息
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_friend_system_msg(self):
    '''获取好友系统消息'''
    pld = payload(self.websocket, self.accessToken, "/get_friend_system_msg")

    return await pld.post()

###############################################################################
# Function:     get_essence_msg_list
# Description:  shamrockAPI, 获取精华消息列表
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def get_essence_msg_list(self, group_id: int):
    '''获取精华消息列表'''
    pld = payload(self.websocket, self.accessToken, "/get_essence_msg_list")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     is_blacklist_uin
# Description:  shamrockAPI, 判断是否在黑名单内
# Input:        void
# Return:       
# Notice:       
###############################################################################
async def is_blacklist_uin(self, user_id: int):
    '''判断是否在黑名单内'''
    pld = payload(self.websocket, self.accessToken, "/is_blacklist_uin")
    pld.argAdd("user_id", user_id)

    return await pld.post()
