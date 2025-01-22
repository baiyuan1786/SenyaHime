###############################################################################
#   File name:   momo.py
#   Description: 描述摸摸的接口
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from autoBotAPI.shamrockBot import message
from autoBotAPI.shamrockBot import httpserver, websocketserver
from ..base import command
from ...user import user
import random, time
from control import FAVOR_ADD_LEAST, FAVOR_ADD_MAX

unknownTouchList = []
unknownTouchList.append("诶？主人想摸什么？千夜完全听不懂啦～")
unknownTouchList.append("嗯？主人刚刚说的是什么？千夜从来没听说过呢！")
unknownTouchList.append("主人，千夜好像没有那个地方哦，你是不是搞错啦？")
unknownTouchList.append("千夜……好像并没有这种东西吧？")
unknownTouchList.append("诶？主人，千夜刚刚好像听错了，你想摸什么？")
unknownTouchList.append("主人真是奇怪，总想着一些千夜也不明白的事情～")
unknownTouchList.append("主人，～别胡思乱想啦！")
unknownTouchList.append("主人是不是看错小说了呀")
unknownTouchList.append("主人，千夜不懂你说的是什么，不过你很可爱呢！")
unknownTouchList.append("千夜歪着头想了半天……主人在说什么呢？")
unknownTouchList.append("好像挺帅的，主人是不是想象力太丰富了？")
unknownTouchList.append("诶呀，千夜对主人说的话完全没概念，难道主人看错了设定？")
unknownTouchList.append("主人总是想到一些奇怪的地方，这次又是从哪里冒出来的呢？")
unknownTouchList.append("千夜也很想要啦，不过现在没有呢～")
unknownTouchList.append("主人刚刚说的，是在千夜的梦里才会有的东西吧？")
unknownTouchList.append("啊？主人，你说的那个地方，千夜从来没听过呢～")
unknownTouchList.append("千夜歪着头仔细想了想，主人好像在开玩笑吧？")
unknownTouchList.append("千夜觉得主人是不是睡迷糊了，快醒醒吧！")
unknownTouchList.append("主人，千夜的身体很正常哦，别乱想啦～")
###############################################################################
# Class:        touchUnknownCammand     
# Input:        
# Notice:       
###############################################################################
class touchUnknownCammand(command):
    '''未知触摸命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''

            msgResovled = msg.resolve()
            return msgResovled is not None and msgResovled.startswith("摸") and len(msgResovled) < 10
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''

            # 获取回复
            favorMsg = message.text(text = random.choice(unknownTouchList))

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = msg.resolve())
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
