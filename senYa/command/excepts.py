###############################################################################
#   File name:   except.py
#   Description: 处理在意外之外的命令输入
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from autoBotAPI.shamrockBot import message
from autoBotAPI.shamrockBot import httpserver, websocketserver
from .base import command
from ..user import user

COMMAND_SHOW_LEN = 5
###############################################################################
# Class:        sorryCommand     
# Input:        
# Notice:       
###############################################################################
class sorryCommand(command):
    '''命令不支持, 使用此回复'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            commandText = msg.resolve()
            return commandText is not None and commandText.startswith("\\")
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            commandText = msg.resolve()
            if len(commandText) > COMMAND_SHOW_LEN:
                commandText = commandText[0:5] + "..."
            return message.text(text = f"呜呜, 对不起主人, 命令\"{commandText}\"还不支持呜喵")

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic)
###############################################################################
# Class:        confuseCommand     
# Input:        
# Notice:       
###############################################################################
class confuseCommand(command):
    '''只at不提供任何输入, 使用疑惑命令'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            commandText = msg.resolve()
            return (commandText is None or not commandText.startswith("\\"))
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            if msg.resolve() is None:
                return message.text(text = f"怎么啦主人, 想小千夜了吗, 要和小千夜聊天, 请输入\\开头的命令哦")
            else:
                return message.text(text = f"对不起主人, 暂不支持直接聊天哦")

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic)
