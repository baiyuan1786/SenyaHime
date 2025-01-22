###############################################################################
#   File name:   favor.py
#   Description: 处理好感度
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from autoBotAPI.shamrockBot import message
from autoBotAPI.shamrockBot import httpserver, websocketserver
from .base import command
from ..user import user

###############################################################################
# Class:        showFavor     
# Input:        
# Notice:       
###############################################################################
class showFavor(command):
    '''查看当前好感度'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            return msg.resolve() == "\好感度" or msg.resolve() == "\查询好感度" or msg.resolve() == "\我的好感度"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            
            mainMsg = message.at(qq = userOBJ.user_id) + message.text("主人, 您的好感度信息如下哦\n")
            favorMsg = userOBJ.curFavor(key = 'seg')

            return mainMsg + favorMsg

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic)