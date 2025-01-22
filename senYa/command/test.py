###############################################################################
#   File name:   card.py
#   Description: 描述关于抽卡的接口
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from autoBotAPI.shamrockBot import message
from autoBotAPI.shamrockBot import httpserver, websocketserver
from .base import command
from ..user import user

###############################################################################
# Class:        testCommand     
# Input:        
# Notice:       
###############################################################################
class testCommand(command):
    '''测试命令'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            return msg.resolve() == "\测试"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            mainMsg1 = message.text("主人, 这是你的测试消息")
            mainMsg2 = message.image(file = r"D:\Tool\Admin\SenyaHime\doc\image\test.png", subType = 1)
            return mainMsg1 + mainMsg2

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic, auto_escape = True, recall_duration = 10000)