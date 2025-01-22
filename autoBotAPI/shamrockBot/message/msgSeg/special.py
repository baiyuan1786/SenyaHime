###############################################################################
#   File name:   special.py
#   Description: 特殊类型消息
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .base import messageSegment
from typing import Literal

###############################################################################
# Class:        basketball     
# Input:        @id
# Notice:       5 没中, 4 擦边没中, 3 卡框, 2 擦边中, 1 正中
###############################################################################
class basketball(messageSegment):
    '''投篮表情'''
    def __init__(self, id: Literal[5, 4, 3, 2, 1]):
        """投篮表情

        :param id: 5 没中, 4 擦边没中, 3 卡框, 2 擦边中, 1 正中
        """        
        super().__init__(type = "basketball", data = {"id": id}, msgType = "basketball")

###############################################################################
# Class:        new_rps     
# Input:        @id
# Notice:       锤 3 剪 2 布 1
###############################################################################
class new_rps(messageSegment):
    '''猜拳表情'''
    def __init__(self, id: Literal[3, 2, 1]):
        """猜拳表情

        :param id: 锤 3 剪 2 布 1
        """        
        super().__init__(type = "new_rps", data = {"id": id}, msgType = "new_rps")

###############################################################################
# Class:        new_dice     
# Input:        @id
# Notice:       点数ID
###############################################################################
class new_dice(messageSegment):
    '''新骰子'''
    def __init__(self, id: Literal[6, 5, 4, 3, 2, 1]):
        super().__init__(type = "new_dice", data = {"id": id}, msgType = "new_dice")

###############################################################################
# Class:        poke     
# Input:        @type
#               @id
#               @strength
# Notice:       
###############################################################################
class poke(messageSegment):
    '''戳一戳(动画版本)'''
    def __init__(self, type: int, id: int, strength: int):
        super().__init__(type = "poke", data = {"type": type, "id": id, "strength": strength}, msgType = "poke")

###############################################################################
# Class:        touch     
# Input:        @id
# Notice:       
###############################################################################
class touch(messageSegment):
    '''戳一戳(双击头像),id=qq'''
    def __init__(self, id: int):
        super().__init__(type = "touch", data = {"id": id}, msgType = "touch")

###############################################################################
# Class:        music     
# Input:        @type   音乐类型(qq/163)
#               @id     音乐 ID
# Notice:       
###############################################################################
class music(messageSegment):
    '''音乐消息'''
    def __init__(self, type: str, id: int):
        super().__init__(type = "music", data = {"type": type, "id": id}, msgType = "music")

###############################################################################
# Class:        weather     
# Input:        @city   城市
#               @code   城市代码
# Notice:       
###############################################################################
class weather(messageSegment):
    '''天气'''
    def __init__(self, city: str, code: str):
        super().__init__(type = "weather", data = {"city": city, "code": code}, msgType = "weather")

###############################################################################
# Class:        gift     
# Input:        @qq   QQ号
#               @id   礼物ID
# Notice:       
###############################################################################
class gift(messageSegment):
    '''礼物'''
    def __init__(self, qq: int, id: int):
        super().__init__(type = "gift", data = {"qq": qq, "id": id}, msgType = "gift")