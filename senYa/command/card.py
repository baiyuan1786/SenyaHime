###############################################################################
#   File name:   card.py
#   Description: 描述关于抽卡的接口
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from path import initCardPool, stateCardPool
from autoBotAPI.shamrockBot import message
from plugin.cardPool import cardPool
from .base import command

qianyePool = cardPool("千夜酱测试卡池", stateCardPool)
###############################################################################
# Class:        drawCardCommand     
# Input:        
# Notice:       
###############################################################################
class drawCardCommand(command):
    '''抽卡命令'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            return msg.resolve() == "\抽奖"
        
        def replyLogic(msg: message.callbackmsg):
            '''回复逻辑'''
            card = qianyePool.drawCard()
            return message.text(f"收到喵，恭喜你抽中了 \"{card}\" 一张")

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic)

###############################################################################
# Class:        reInitCardPoolCommand     
# Input:        
# Notice:       
###############################################################################
class reInitCardPoolCommand(command):
    '''千夜机器人的重置卡池API'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            return msg.resolve() == "\重置卡池"
        
        def replyLogic(msg: message.callbackmsg):
            '''回复逻辑'''
            qianyePool.reInit(initFile = initCardPool)
            return message.text(f"好的喵主人，重置卡池成功")

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic)
    
###############################################################################
# Class:        stateInfoCommand     
# Input:        
# Notice:       
###############################################################################
class stateInfoCommand(command):
    '''查看卡池状态'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            return msg.resolve() == "\查看卡池状态"
        
        def replyLogic(msg: message.callbackmsg):
            '''回复逻辑'''
            return message.text(text = qianyePool.stateInfo())

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic)