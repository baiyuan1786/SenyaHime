###############################################################################
#   File name:   test.py
#   Description: 测试功能
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .base import TriggerFunction
from ..physics import message, httpserver, websocketserver
from ..memory.tarot import tarotPool2233
from ..memory.user import userInfo
from .dialogue_siliconFlow import dialogue

############################################################################################################################
# Class:        DrawTarot
# Notice:       千夜姬测试命令
############################################################################################################################
class Test(TriggerFunction[userInfo, httpserver|websocketserver, message.callbackmsg, message.messageSegment]):
    '''抽取塔罗牌'''
    def __init__(self):
        super().__init__(isNeedAt = True, isReply = False, isAt = True,\
                          skillName = "测试" , autoEscape = None, recallDuration = None)

    ###############################################################################
    # Function:     realize  
    # Notice:       抽塔罗牌实现
    ###############################################################################
    def realize(self, user, server, backMsg):

        # 命令解析
        commandText = backMsg.resolve()
        if commandText == "\\测试":
            allMsg = dialogue().execute(self, user, server, backMsg)

        else:
            raise NameError("not me")
        
        return allMsg