###############################################################################
#   File name:   tarot.py
#   Description: 塔罗牌功能
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .base import TriggerFunction
from ..physics import message, httpserver, websocketserver
from ..memory.tarot import tarotPool2233
from ..memory.user import userInfo

FAVOR_DRAW_TAROT = 10

############################################################################################################################
# Class:        DrawTarot
# Notice:       千夜姬抽塔罗牌命令
############################################################################################################################
class DrawTarot(TriggerFunction[userInfo, httpserver|websocketserver, message.callbackmsg, message.messageSegment]):
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
        if commandText == "\\塔罗牌" or commandText == "\\抽塔罗牌":

            explainMsg, imaMsg, name = tarotPool2233.draw()
            favorMsgAdd = user.favorAdd(FAVOR_DRAW_TAROT)
            helloMsg = message.text(f"\n主人~你抽到了【{name}】哦\n")

            allMsg = helloMsg + imaMsg + explainMsg + favorMsgAdd

        else:
            raise NameError("not me")
        
        return allMsg