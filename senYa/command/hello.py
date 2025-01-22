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
# Class:        wananCommand     
# Input:        
# Notice:       
###############################################################################
class wananCommand(command):
    '''查看卡池状态'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            return msg.resolve() == "晚安"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            return message.text(text = "晚安主人, 祝您好梦哦")

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic)