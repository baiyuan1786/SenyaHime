###############################################################################
#   File name:   greeting.py
#   Description: 安安服务
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .base import TriggerFunction
from ..memory.user import userInfo
from ..physics import message, httpserver, websocketserver
from control import json2dict, GRoot

from datetime import datetime
import random, time

# 安安服务
helloReplyPath = GRoot / "senYa" / "memory" / "reply" / "greeting"
goodMorningReply = json2dict(helloReplyPath / "morning.json")   # 早安
goodnoonReply = json2dict(helloReplyPath / "noon.json")         # 午安
goodEveningReply = json2dict(helloReplyPath / "evening.json")   # 晚安
reEveningReply = json2dict(helloReplyPath / "reEvening.json")   # 再晚安
lastNightReply = json2dict(helloReplyPath / "lastNight.json")   # 深夜
defendEveningReply = json2dict(helloReplyPath / "defendEvening.json")   # 对于千夜的晚安
###############################################################################
# Function:     timePeriod  
# Notice:       获取当前时间段
############################################################################### 
def timePeriod():
    '''获取当前时间段'''
    currentTime = datetime.now()
    currentHour = currentTime.hour # 获取当前小时（整数)

    if currentHour < 6:
        period = "深夜"
    elif currentHour < 12:
        period = "早上"
    elif currentHour < 18:
        period = "下午"
    else:
        period = "晚上"
    return period

############################################################################################################################
# Class:        GreetingMor
# Notice:       早安命令
############################################################################################################################
class GreetingMor(TriggerFunction[userInfo, httpserver|websocketserver, message.callbackmsg, message.messageSegment]):
    '''早安命令'''
    def __init__(self):
        super().__init__(isNeedAt = False, isReply = False, isAt = False,\
                          skillName = "早安" , autoEscape = None, recallDuration = None)

    ###############################################################################
    # Function:     realize  
    # Notice:       早安实现
    ###############################################################################
    def realize(self, user, server, backMsg):
        '''早安命令实现'''

        # 命令解析
        commandText = backMsg.resolve()
        if commandText == "早安":
            if timePeriod() != "早上":
                allMsg = message.text(text = "主人, 现在好像还不是早上哦")
            else:
                allMsg = message.text(text = random.choice(goodMorningReply["List"]))
        else:
            raise NameError("not me")
        
        return allMsg
        
############################################################################################################################
# Class:        GreetingNoon
# Notice:       午安命令
############################################################################################################################
class GreetingNoon(TriggerFunction[userInfo, httpserver|websocketserver, message.callbackmsg, message.messageSegment]):
    '''午安命令'''
    def __init__(self):
        super().__init__(isNeedAt = False, isReply = False, isAt = False,\
                          skillName = "午安" , autoEscape = None, recallDuration = None)

    ###############################################################################
    # Function:     realize  
    # Notice:       午安实现
    ###############################################################################
    def realize(self, user, server, backMsg):
        '''午安命令实现'''

        # 命令解析
        commandText = backMsg.resolve()
        if commandText == "午安":
            if timePeriod() != "下午":
                allMsg = message.text(text = "主人, 现在好像还不是午后哦")
            else:
                allMsg = message.text(text = random.choice(goodnoonReply["List"]))
        else:
            raise NameError("not me")
        
        return allMsg

############################################################################################################################
# Class:        GreetingNight
# Notice:       晚安命令
############################################################################################################################
class GreetingNight(TriggerFunction[userInfo, httpserver|websocketserver, message.callbackmsg, message.messageSegment]):
    '''晚安命令'''
    def __init__(self):
        super().__init__(isNeedAt = False, isReply = False, isAt = False,\
                          skillName = "晚安" , autoEscape = None, recallDuration = None)

    ###############################################################################
    # Function:     realize  
    # Notice:       晚安实现
    ###############################################################################
    def realize(self, user, server, backMsg):
        '''晚安命令实现'''

        # 命令解析
        commandText = backMsg.resolve()
        if commandText == "晚安" or commandText == "晚安安":

            if timePeriod() != "晚上" and timePeriod() != "深夜":
                allMsg = message.text(text = "主人, 现在好像还不是晚上哦")

            elif not backMsg.isRelAtme():

                if time.time() - user.readConf(configName = "commandUseLastTimestamp", commandName = self.skillName) < 3600 * 2:
                    allMsg = message.text(text = random.choice(reEveningReply["List"]))
                elif timePeriod() == "深夜":
                    allMsg = message.text(text = random.choice(lastNightReply["List"]))
                elif timePeriod() == "晚上":
                    allMsg = message.text(text = random.choice(goodEveningReply["List"]))

            else:
                allMsg = message.text(text = random.choice(defendEveningReply["List"]))
        
        return allMsg