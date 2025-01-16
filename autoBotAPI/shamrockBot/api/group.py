###############################################################################
#   File name:   group.py
#   Description: 群组相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..url import shamrockURL
###############################################################################
# Function:     set_group_name
# Input:        @group_id   群号
#               @group_name 新群名   
# Notice:       该 API 无响应数据
###############################################################################
def set_group_name(self, group_id: int, group_name: str):
    '''shamrockAPI, 设置群名'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_name")
    url.argAdd("group_id", group_id)
    url.argAdd("group_name", group_name)

    return url.get()

###############################################################################
# Function:     set_group_portrait
# Input:        @group_id   群号
#               @file 图片文件名（使用在shamrock上的路径）
#               @cache 表示是否使用已缓存的文件   
# Notice:       该 API 无响应数据
###############################################################################
def set_group_portrait(self, group_id: int, file: str, cache: int):
    '''shamrockAPI, 设置群头像'''
    raise TypeError("shamrock暂未实现该API")
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_portrait")
    url.argAdd("group_id", group_id)
    url.argAdd("file", file)
    url.argAdd("cache", cache)

    return url.get()

###############################################################################
# Function:     set_group_admin
# Input:        @group_id   群号
#               @user_id 新群名
#               @enable	是否设置   
# Notice:       该 API 无响应数据
###############################################################################
def set_group_admin(self, group_id: int, user_id: str, enable: bool):
    '''shamrockAPI, 设置管理员'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_admin")
    url.argAdd("group_id", group_id)
    url.argAdd("user_id", user_id)
    url.argAdd("enable", enable)

    return url.get()

###############################################################################
# Function:     set_group_card
# Input:        @group_id   群号
#               @user_id    新群名
#               @card       群名片内容, 不填或空字符串表示删除群名片   
# Notice:       该 API 无响应数据
###############################################################################
def set_group_card(self, group_id: int, user_id: str, card: str):
    '''shamrockAPI, 设置群成员名片'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_card")
    url.argAdd("group_id", group_id)
    url.argAdd("user_id", user_id)
    url.argAdd("card", card)

    return url.get()

###############################################################################
# Function:     set_group_remark
# Input:        @group_id   群号
#               @remark     备注   
# Notice:       该 API 无响应数据
###############################################################################
def set_group_remark(self, group_id: int, remark: str):
    '''shamrockAPI, 设置群备注'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_remark")
    url.argAdd("group_id", group_id)
    url.argAdd("remark", remark)

    return url.get()

###############################################################################
# Function:     set_group_special_title
# Input:        @group_id   群号
#               @user_id    
#               @special_title    
# Notice:       该 API 无响应数据
###############################################################################
def set_group_special_title(self, group_id: int, user_id: str, special_title: str):
    '''shamrockAPI, 设置群组(成员)专属头衔'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_special_title")
    url.argAdd("group_id", group_id)
    url.argAdd("user_id", user_id)
    url.argAdd("special_title", special_title)

    return url.get()

###############################################################################
# Function:     set_group_special_title
# Input:        @group_id   群号
#               @user_id    
#               @special_title    
# Notice:       该 API 无响应数据
###############################################################################
def set_group_special_title(self, group_id: int, user_id: str, special_title: str):
    '''shamrockAPI, 设置群组专属头衔'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_special_title")
    url.argAdd("group_id", group_id)
    url.argAdd("user_id", user_id)
    url.argAdd("special_title", special_title)

    return url.get()

###############################################################################
# Function:     set_group_ban
# Input:        @group_id   群号
#               @user_id    
#               @duration   持续时间，单位不明   
# Notice:       当 duration 为 0 时，将解除禁言。
###############################################################################
def set_group_ban(self, group_id: int, user_id: str, duration: int):
    '''shamrockAPI, 禁言群组成员'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_ban")
    url.argAdd("group_id", group_id)
    url.argAdd("user_id", user_id)
    url.argAdd("duration", duration)

    return url.get()

###############################################################################
# Function:     set_group_whole_ban
# Input:        @group_id   群号
#               @enable     False时表示取消禁言   
# Notice:       
###############################################################################
def set_group_whole_ban(self, group_id: int, enable: bool):
    '''shamrockAPI, 禁言全群'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_whole_ban")
    url.argAdd("group_id", group_id)
    url.argAdd("enable", enable)

    return url.get()

###############################################################################
# Function:     set_essence_msg
# Input:        @message_id   消息ID   
# Notice:       该 API 没有响应数据
###############################################################################
def set_essence_msg(self, message_id: int):
    '''shamrockAPI, 设置精华消息'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_essence_msg")
    url.argAdd("message_id", message_id)

    return url.get()

###############################################################################
# Function:     send_group_sign
# Input:        @group_id   群号
#               @enable     False时表示取消禁言   
# Notice:       
###############################################################################
def send_group_sign(self, group_id: int):
    '''shamrockAPI, 群打卡'''
    url = shamrockURL(self.baseURL, self.accessToken, "/send_group_sign")
    url.argAdd("group_id", group_id)

    return url.get()

###############################################################################
# Function:     send_group_notice
# Input:        @group_id   群号
#               @content    公告内容
#               @image      图片   
# Notice:       
###############################################################################
def send_group_notice(self, group_id: int, content: str, image: str = None):
    '''shamrockAPI, 发送群公告'''
    url = shamrockURL(self.baseURL, self.accessToken, "/_send_group_notice")
    url.argAdd("group_id", group_id)
    url.argAdd("content", content)
    url.argAdd("image", image)

    return url.get()

###############################################################################
# Function:     get_group_notice
# Input:        @group_id   群号   
# Notice:       
###############################################################################
def get_group_notice(self, group_id: int):
    '''shamrockAPI, 获取群公告'''
    url = shamrockURL(self.baseURL, self.accessToken, "/_get_group_notice")
    url.argAdd("group_id", group_id)

    return url.get()

###############################################################################
# Function:     set_group_kick
# Input:        @group_id   群号
#               @user_id    用户号
#               @reject_add_request    是否拒绝再次加群   
# Notice:       
###############################################################################
def set_group_kick(self, group_id: int, user_id: int, reject_add_request: bool):
    '''shamrockAPI, 群组踢人'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_kick")
    url.argAdd("group_id", group_id)
    url.argAdd("user_id", user_id)
    url.argAdd("reject_add_request", reject_add_request)

    return url.get()

###############################################################################
# Function:     set_group_leave
# Input:        @group_id   群号   
# Notice:       
###############################################################################
def set_group_leave(self, group_id: int):
    '''shamrockAPI, 退出群组'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_leave")
    url.argAdd("group_id", group_id)

    return url.get()

###############################################################################
# Function:     group_touch 
# Input:        @group_id   群号
#               @user_id    用户号   
# Notice:       
###############################################################################
def group_touch (self, group_id: int, user_id: int):
    '''shamrockAPI, 群内戳一戳'''
    url = shamrockURL(self.baseURL, self.accessToken, "/group_touch ")
    url.argAdd("group_id", group_id)
    url.argAdd("user_id", user_id)

    return url.get()

###############################################################################
# Function:     get_prohibited_member_list
# Input:        @group_id   群号   
# Notice:       
###############################################################################
def get_prohibited_member_list(self, group_id: int):
    '''shamrockAPI, 获取被禁言成员列表'''
    url = shamrockURL(self.baseURL, self.accessToken, "/get_prohibited_member_list")
    url.argAdd("group_id", group_id)

    return url.get()

###############################################################################
# Function:     get_group_at_all_remain
# Input:        @group_id   群号   
# Notice:       当机器人是管理员时可用
###############################################################################
def get_group_at_all_remain(self, group_id: int):
    '''shamrockAPI, 获取群 @全体成员 剩余次数'''
    url = shamrockURL(self.baseURL, self.accessToken, "/get_group_at_all_remain")
    url.argAdd("group_id", group_id)

    return url.get()

###############################################################################
# Function:     set_group_comment_face
# Input:        @group_id   群号
#               @msg_id     消息ID
#               @face_id    表情ID
#               @is_set     是否设置或取消评论   
# Notice:       可能有bug
###############################################################################
def set_group_comment_face(self, group_id: int, msg_id: int, face_id: int, is_set: bool):
    '''shamrockAPI, 设置消息底部评论小表情(可能无效)'''
    url = shamrockURL(self.baseURL, self.accessToken, "/set_group_comment_face")
    url.argAdd("group_id", group_id)
    url.argAdd("msg_id", msg_id)
    url.argAdd("face_id", face_id)
    url.argAdd("is_set", is_set)

    return url.get()