###############################################################################
#   File name:   favor.py
#   Description: 好感度相关功能
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .base import TriggerFunction
from ..physics import message, httpserver, websocketserver
from ..memory.tarot import tarotPool2233
from ..memory.user import userInfo

FAVOR_DRAW_TAROT = 10

############################################################################################################################
# Class:        ShowFavor
# Notice:       千夜姬展示用户好感度
############################################################################################################################
class ShowFavor(TriggerFunction[userInfo, httpserver|websocketserver, message.callbackmsg, message.messageSegment]):
    '''抽取塔罗牌'''
    def __init__(self):
        super().__init__(isNeedAt = True, isReply = False, isAt = True,\
                          skillName = "抽塔罗牌" , autoEscape = None, recallDuration = None)

    ###############################################################################
    # Function:     realize  
    # Notice:       抽塔罗牌实现
    ###############################################################################
    def realize(self, user, server, backMsg):

        # 命令解析
        commandText = backMsg.resolve()
        if commandText == "\\好感度" or commandText == "\\查询好感度":
            allMsg = message.text("主人, 您的好感度信息如下哦\n") + user.readFavor(key = 'seg')
        else:
            raise NameError("not me")
            
        return allMsg
