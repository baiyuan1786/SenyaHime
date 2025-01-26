###############################################################################
#   File name:   group.py
#   Description: 群组相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..payload import payload
import asyncio
###############################################################################
# Function:     set_group_name
# Input:        @group_id   群号
#               @group_name 新群名   
# Notice:       该 API 无响应数据
###############################################################################
async def set_group_name(self, group_id: int, group_name: str):
    '''shamrockAPI, 设置群名'''
    pld = payload(self.websocket, self.accessToken, "/set_group_name")
    pld.argAdd("group_id", group_id)
    pld.argAdd("group_name", group_name)

    return await pld.post()

###############################################################################
# Function:     set_group_portrait
# Input:        @group_id   群号
#               @file 图片文件名（使用在shamrock上的路径）
#               @cache 表示是否使用已缓存的文件   
# Notice:       该 API 无响应数据
###############################################################################
async def set_group_portrait(self, group_id: int, file: str, cache: int):
    '''shamrockAPI, 设置群头像'''
    raise TypeError("shamrock暂未实现该API")
    pld = payload(self.websocket, self.accessToken, "/set_group_portrait")
    pld.argAdd("group_id", group_id)
    pld.argAdd("file", file)
    pld.argAdd("cache", cache)

    return await pld.post()

###############################################################################
# Function:     set_group_admin
# Input:        @group_id   群号
#               @user_id 新群名
#               @enable	是否设置   
# Notice:       该 API 无响应数据
###############################################################################
async def set_group_admin(self, group_id: int, user_id: str, enable: bool):
    '''shamrockAPI, 设置管理员'''
    pld = payload(self.websocket, self.accessToken, "/set_group_admin")
    pld.argAdd("group_id", group_id)
    pld.argAdd("user_id", user_id)
    pld.argAdd("enable", enable)

    return await pld.post()

###############################################################################
# Function:     set_group_card
# Input:        @group_id   群号
#               @user_id    新群名
#               @card       群名片内容, 不填或空字符串表示删除群名片   
# Notice:       该 API 无响应数据
###############################################################################
async def set_group_card(self, group_id: int, user_id: str, card: str):
    '''shamrockAPI, 设置群成员名片'''
    pld = payload(self.websocket, self.accessToken, "/set_group_card")
    pld.argAdd("group_id", group_id)
    pld.argAdd("user_id", user_id)
    pld.argAdd("card", card)

    return await pld.post()

###############################################################################
# Function:     set_group_remark
# Input:        @group_id   群号
#               @remark     备注   
# Notice:       该 API 无响应数据
###############################################################################
async def set_group_remark(self, group_id: int, remark: str):
    '''shamrockAPI, 设置群备注'''
    pld = payload(self.websocket, self.accessToken, "/set_group_remark")
    pld.argAdd("group_id", group_id)
    pld.argAdd("remark", remark)

    return await pld.post()

###############################################################################
# Function:     set_group_special_title
# Input:        @group_id   群号
#               @user_id    
#               @special_title    
# Notice:       该 API 无响应数据
###############################################################################
async def set_group_special_title(self, group_id: int, user_id: str, special_title: str):
    '''shamrockAPI, 设置群组(成员)专属头衔'''
    pld = payload(self.websocket, self.accessToken, "/set_group_special_title")
    pld.argAdd("group_id", group_id)
    pld.argAdd("user_id", user_id)
    pld.argAdd("special_title", special_title)

    return await pld.post()

###############################################################################
# Function:     set_group_special_title
# Input:        @group_id   群号
#               @user_id    
#               @special_title    
# Notice:       该 API 无响应数据
###############################################################################
async def set_group_special_title(self, group_id: int, user_id: str, special_title: str):
    '''shamrockAPI, 设置群组专属头衔'''
    pld = payload(self.websocket, self.accessToken, "/set_group_special_title")
    pld.argAdd("group_id", group_id)
    pld.argAdd("user_id", user_id)
    pld.argAdd("special_title", special_title)

    return await pld.post()

###############################################################################
# Function:     set_group_ban
# Input:        @group_id   群号
#               @user_id    
#               @duration   持续时间，单位不明   
# Notice:       当 duration 为 0 时，将解除禁言。
###############################################################################
async def set_group_ban(self, group_id: int, user_id: str, duration: int):
    '''shamrockAPI, 禁言群组成员'''
    pld = payload(self.websocket, self.accessToken, "/set_group_ban")
    pld.argAdd("group_id", group_id)
    pld.argAdd("user_id", user_id)
    pld.argAdd("duration", duration)

    return await pld.post()

###############################################################################
# Function:     set_group_whole_ban
# Input:        @group_id   群号
#               @enable     False时表示取消禁言   
# Notice:       
###############################################################################
async def set_group_whole_ban(self, group_id: int, enable: bool):
    '''shamrockAPI, 禁言全群'''
    pld = payload(self.websocket, self.accessToken, "/set_group_whole_ban")
    pld.argAdd("group_id", group_id)
    pld.argAdd("enable", enable)

    return await pld.post()

###############################################################################
# Function:     set_essence_msg
# Input:        @message_id   消息ID   
# Notice:       该 API 没有响应数据
###############################################################################
async def set_essence_msg(self, message_id: int):
    '''shamrockAPI, 设置精华消息'''
    pld = payload(self.websocket, self.accessToken, "/set_essence_msg")
    pld.argAdd("message_id", message_id)

    return await pld.post()

###############################################################################
# Function:     send_group_sign
# Input:        @group_id   群号
#               @enable     False时表示取消禁言   
# Notice:       
###############################################################################
async def send_group_sign(self, group_id: int):
    '''shamrockAPI, 群打卡'''
    pld = payload(self.websocket, self.accessToken, "/send_group_sign")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     send_group_notice
# Input:        @group_id   群号
#               @content    公告内容
#               @image      图片   
# Notice:       
###############################################################################
async def send_group_notice(self, group_id: int, content: str, image: str = None):
    '''shamrockAPI, 发送群公告'''
    pld = payload(self.websocket, self.accessToken, "/_send_group_notice")
    pld.argAdd("group_id", group_id)
    pld.argAdd("content", content)
    pld.argAdd("image", image)

    return await pld.post()

###############################################################################
# Function:     get_group_notice
# Input:        @group_id   群号   
# Notice:       
###############################################################################
async def get_group_notice(self, group_id: int):
    '''shamrockAPI, 获取群公告'''
    pld = payload(self.websocket, self.accessToken, "/_get_group_notice")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     set_group_kick
# Input:        @group_id   群号
#               @user_id    用户号
#               @reject_add_request    是否拒绝再次加群   
# Notice:       
###############################################################################
async def set_group_kick(self, group_id: int, user_id: int, reject_add_request: bool):
    '''shamrockAPI, 群组踢人'''
    pld = payload(self.websocket, self.accessToken, "/set_group_kick")
    pld.argAdd("group_id", group_id)
    pld.argAdd("user_id", user_id)
    pld.argAdd("reject_add_request", reject_add_request)

    return await pld.post()

###############################################################################
# Function:     set_group_leave
# Input:        @group_id   群号   
# Notice:       
###############################################################################
async def set_group_leave(self, group_id: int):
    '''shamrockAPI, 退出群组'''
    pld = payload(self.websocket, self.accessToken, "/set_group_leave")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     group_touch 
# Input:        @group_id   群号
#               @user_id    用户号   
# Notice:       
###############################################################################
async def group_touch (self, group_id: int, user_id: int):
    '''shamrockAPI, 群内戳一戳'''
    pld = payload(self.websocket, self.accessToken, "/group_touch ")
    pld.argAdd("group_id", group_id)
    pld.argAdd("user_id", user_id)

    return await pld.post()

###############################################################################
# Function:     get_prohibited_member_list
# Input:        @group_id   群号   
# Notice:       
###############################################################################
async def get_prohibited_member_list(self, group_id: int):
    '''shamrockAPI, 获取被禁言成员列表'''
    pld = payload(self.websocket, self.accessToken, "/get_prohibited_member_list")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     get_group_at_all_remain
# Input:        @group_id   群号   
# Notice:       当机器人是管理员时可用
###############################################################################
async def get_group_at_all_remain(self, group_id: int):
    '''shamrockAPI, 获取群 @全体成员 剩余次数'''
    pld = payload(self.websocket, self.accessToken, "/get_group_at_all_remain")
    pld.argAdd("group_id", group_id)

    return await pld.post()

###############################################################################
# Function:     set_group_comment_face
# Input:        @group_id   群号
#               @msg_id     消息ID
#               @face_id    表情ID
#               @is_set     是否设置或取消评论   
# Notice:       可能有bug
###############################################################################
async def set_group_comment_face(self, group_id: int, msg_id: int, face_id: int, is_set: bool):
    '''shamrockAPI, 设置消息底部评论小表情(可能无效)'''
    pld = payload(self.websocket, self.accessToken, "/set_group_comment_face")
    pld.argAdd("group_id", group_id)
    pld.argAdd("msg_id", msg_id)
    pld.argAdd("face_id", face_id)
    pld.argAdd("is_set", is_set)

    return await pld.post()