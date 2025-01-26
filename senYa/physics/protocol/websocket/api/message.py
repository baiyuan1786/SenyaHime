###############################################################################
#   File name:   message.py
#   Description: 消息相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
from ....message import messageSegment
import asyncio
###############################################################################
# Function:     send_private_msg
# Input:        @user_id        接收者QQ号
#               @message        message格式可为消息段object，或消息段组合array
#               @auto_escape    是否解析 CQ 码（true为不解析）Not must
#               @recall_duration 自动撤回时间间隔（毫秒） Not must     
# Notice:       http://192.168.0.108:5700/send_private_msg?access_token=guzhaoqiaoqiaoa1&user_id=395642104&message=你好
###############################################################################
async def send_private_msg(self, user_id: int, message: str | messageSegment, auto_escape: bool = None, recall_duration: int = None):
    '''shamrockAPI, 发送私聊消息'''
    pld = payload(self.websocket, self.accessToken, "/send_private_msg")
    pld.argAdd("user_id", user_id)
    pld.argAdd("message", message)
    pld.argAdd("auto_escape", auto_escape)
    pld.argAdd("recall_duration", recall_duration)

    return await pld.post()

###############################################################################
# Function:     send_group_msg
# Input:        @group_id
#               @message
#               @auto_escape    是否解析 CQ 码（true为不解析）Not must
#               @recall_duration 自动撤回时间间隔（毫秒） Not must     
# Notice:       这是千夜姬的类函数, 不可在其他类中使用
###############################################################################
async def send_group_msg(self, group_id: int, message: str | messageSegment, auto_escape: bool = None, recall_duration: int = None):
    '''shamrockAPI, 发送群聊消息'''
    pld = payload(self.websocket, self.accessToken, "/send_group_msg")
    pld.argAdd("group_id", group_id)
    pld.argAdd("message", message)
    pld.argAdd("auto_escape", auto_escape)
    pld.argAdd("recall_duration", recall_duration)

    return await pld.post()

###############################################################################
# Function:     send_msg
# Input:        @message_type
#               @user_id
#               @group_id
#               @discuss_id
#               @message
#               @auto_escape    是否解析 CQ 码（true为不解析）Not must
#               @recall_duration 自动撤回时间间隔（毫秒） Not must     
# Notice:       当前发送消息的 API 暂不支持发送讨论组消息
###############################################################################
async def send_msg(self, message_type: str, user_id: int, group_id: int, discuss_id: int, message: str | messageSegment,\
              auto_escape: bool = None, recall_duration: int = None):
    '''shamrockAPI, 发送群聊和私聊消息'''
    pld = payload(self.websocket, self.accessToken, "/send_msg")
    pld.argAdd("message_type", message_type)
    pld.argAdd("user_id", user_id)
    pld.argAdd("group_id", group_id)
    pld.argAdd("discuss_id", discuss_id)
    pld.argAdd("message", message)
    pld.argAdd("auto_escape", auto_escape)
    pld.argAdd("recall_duration", recall_duration)

    return await pld.post()

###############################################################################
# Function:     get_msg
# Input:        @message_id     
# Notice:       
###############################################################################
async def get_msg(self, message_id: int):
    '''shamrockAPI, 主动获取某消息'''
    pld = payload(self.websocket, self.accessToken, "/get_msg")
    pld.argAdd("message_id", message_id)

    return await pld.post()

###############################################################################
# Function:     delete_msg
# Input:        @message_id     
# Notice:       
###############################################################################
async def delete_msg(self, message_id: int):
    '''shamrockAPI, 撤回某消息'''
    pld = payload(self.websocket, self.accessToken, "/delete_msg")
    pld.argAdd("message_id", message_id)

    return await pld.post()

###############################################################################
# Function:     get_history_msg
# Input:        @message_type
#               @user_id    not must
#               @group_id   not must
#               @count      获取的消息数量 not must
#               @message_seq 起始消息的message_id（默认为0，表示从最后一条发言往前）not must     
# Notice:       
###############################################################################
async def get_history_msg(self, message_id: int, user_id: int = None, group_id: int = None, count: int = None, message_seq: int = None):
    '''shamrockAPI, 获取历史消息'''
    pld = payload(self.websocket, self.accessToken, "/get_history_msg")
    pld.argAdd("message_id", message_id)
    pld.argAdd("user_id", user_id)
    pld.argAdd("group_id", group_id)
    pld.argAdd("count", count)
    pld.argAdd("message_seq", message_seq)

    return await pld.post()

###############################################################################
# Function:     get_group_msg_history
# Input:        @group_id
#               @count      获取的消息数量 not must
#               @message_seq 起始消息的message_id（默认为0，表示从最后一条发言往前）not must     
# Notice:       
###############################################################################
async def get_group_msg_history(self, group_id: int, count: int = None, message_seq: int = None):
    '''shamrockAPI, 获取群聊历史消息'''
    pld = payload(self.websocket, self.accessToken, "/get_group_msg_history")
    pld.argAdd("group_id", group_id)
    pld.argAdd("count", count)
    pld.argAdd("message_seq", message_seq)

    return await pld.post()

###############################################################################
# Function:     clear_msgs
# Input:        @message_type
#               @user_id  not must
#               @group_id not must     
# Notice:       
###############################################################################
async def clear_msgs(self, message_type: str, user_id: str = None, group_id: str = None):
    '''shamrockAPI, 清除本地消息缓存'''
    pld = payload(self.websocket, self.accessToken, "/clear_msgs")
    pld.argAdd("message_type", message_type)
    pld.argAdd("user_id", user_id)
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     get_forward_msg
# Input:        @id 消息资源ID（卡片消息里面的resId）     
# Notice:       由于QQ内部错误，该接口可能导致闪退等问题的出现！
#               一般是闪退一次后再次重新启动便不再闪退，但是可能无法获取合并转发的内容
###############################################################################
async def get_forward_msg(self, id: str):
    '''shamrockAPI, 获取合并转发内容'''
    pld = payload(self.websocket, self.accessToken, "/get_forward_msg")
    pld.argAdd("id", id)

    return await pld.post()

###############################################################################
# Function:     send_group_forward_msg
# Input:        @group_id 发送到的目标群号
#               @messages 合并转发消息集合     
# Notice:       由于QQ限制，该接口的响应结果暂不具备意义，其中：message_id不匹配、forward_id为空。
###############################################################################
async def send_group_forward_msg(self, group_id: str, messages):
    '''shamrockAPI, 发送群聊合并转发'''
    pld = payload(self.websocket, self.accessToken, "/send_group_forward_msg")
    pld.argAdd("group_id", group_id)
    pld.argAdd("messages", messages)
    return await pld.post()

###############################################################################
# Function:     send_private_forward_msg
# Input:        @user_id 发送到的目标用户
#               @messages 合并转发消息集合     
# Notice:       
###############################################################################
async def send_private_forward_msg(self, user_id: str, messages):
    '''shamrockAPI, 发送私聊合并转发'''
    pld = payload(self.websocket, self.accessToken, "/send_private_forward_msg")
    pld.argAdd("user_id", user_id)
    pld.argAdd("messages", messages)
    return await pld.post()