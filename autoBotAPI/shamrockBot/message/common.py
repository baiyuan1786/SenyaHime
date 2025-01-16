###############################################################################
#   File name:   common.py
#   Description: 常规类型消息
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .messageSegment import messageSegment

###############################################################################
# Class:        at     
# Input:        @qq
# Notice:       当 qq 字段为 "0"或"all" 时, 表示 AT 全体成员
###############################################################################
class at(messageSegment):
    '''@类型消息, 可以在群内@某人, 当 qq 字段为 "0"或"all" 时, 表示 AT 全体成员'''
    def __init__(self, qq: int | str):
        super().__init__(type = "at", data = {"qq": qq}, msgType = "at")

###############################################################################
# Class:        text     
# Input:        @text
# Notice:       
###############################################################################
class text(messageSegment):
    '''普通文本消息'''
    def __init__(self, text: str): 
        super().__init__(type = "text", data = {"text": text}, msgType = "text")

###############################################################################
# Class:        markDown     
# Input:        @text
# Notice:       
###############################################################################
class markDown(messageSegment):
    '''markDown语言消息'''
    def __init__(self, content: str):
        raise TypeError("暂不支持markdown格式消息")
        super().__init__(type = "markdown", data = {"content": content}, msgType = "markdown")

###############################################################################
# Class:        face     
# Input:        @id
#               @big
# Notice:       
###############################################################################
class face(messageSegment):
    '''发送一个小表情, 只能从QQ自带的表情包里面选,不是自定义表情包'''
    def __init__(self, id: int, big: bool):
        super().__init__(type = "face", data = {"id": id, "big": big}, msgType = "face")

###############################################################################
# Class:        bubble_face     
# Input:        @id
#               @count
# Notice:       
###############################################################################
class bubble_face(messageSegment):
    '''发送一个弹射表情, 只能从QQ自带的表情包里面选,不是自定义表情包'''
    def __init__(self, id: int, count: bool):
        super().__init__(type = "bubble_face", data = {"id": id, "count": count}, msgType = "bubble_face")

###############################################################################
# Class:        reply     
# Input:        @id
# Notice:       
###############################################################################
class reply(messageSegment):
    '''回复某个已经存在的消息, 需要输入消息id'''
    def __init__(self, id: int):
        super().__init__(type = "reply", data = {"id": id}, msgType = "reply")