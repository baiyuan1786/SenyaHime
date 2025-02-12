###############################################################################
#   File name:   touch.py
#   Description: 触摸服务
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from typing import Literal
import random

from .base import TriggerFunction
from ..memory.user import userInfo
from ..physics import message, httpserver, websocketserver
from control import json2dict, GRoot

replyPath = GRoot / "senYa" / "memory" / "reply" / "touch"
touchReply = json2dict(replyPath / "touch.json")
touchBellyReply = json2dict(replyPath / "touchBelly.json")
touchEarReply = json2dict(replyPath / "touchEar.json")
touchFaceReply = json2dict(replyPath / "touchFace.json")
touchFootReply = json2dict(replyPath / "touchFoot.json")
touchHairReply = json2dict(replyPath / "touchHair.json")
touchHandReply = json2dict(replyPath / "touchHand.json")
touchHeadReply = json2dict(replyPath / "touchHead.json")
touchLegReply = json2dict(replyPath / "touchLeg.json")
touchSensitiveReply = json2dict(replyPath / "touchSensitive.json")
touchEyesReply = json2dict(replyPath / "touchEyes.json")
touchUnknownReply = json2dict(replyPath / "touchUnknown.json")
touchWordLessReply = json2dict(replyPath / "touchWordLess.json")

FAVOR_DECREASE_FORBIDDEN_TOUCH = -100       # 禁止触摸减少好感度
FAVOR_ADD_LEAST = 30                        # 单次行为好感增加下限
FAVOR_ADD_MAX = 40                          # 单次行为好感增加上限
TOUCH_COMMAND_LEN_MAX = 10                  # 触摸命令支持长度上限

############################################################################################################################
# Class:        Touch
# Notice:       触摸命令
############################################################################################################################
class Touch(TriggerFunction[userInfo, httpserver|websocketserver, message.callbackmsg, message.messageSegment]):
    '''触摸命令, 提供各个部位的触摸返回和好感度增减服务'''
    def __init__(self):
        super().__init__(isNeedAt = True, isReply = False, isAt = True,\
                          skillName = "触摸" , autoEscape = None, recallDuration = None)

    ###############################################################################
    # Function:     realize  
    # Notice:       
    ###############################################################################
    def realize(self, user, server, backMsg):
        ###############################################################################
        # Function:     __touchFavorHandle  
        # Notice:       
        ###############################################################################
        def __touchFavorHandle(sensitive: Literal[0, 1, 2], touchReply: dict):
            '''触摸的好感度处理逻辑'''
            favorStage = user.readFavor(key = "stage")

            # 获取回复
            if sensitive <= 1:
                
                # 普通触摸
                if sensitive == 0:
                    addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
                    favorMsgAdd = user.favorAdd(addedFavor)

                # 敏感触摸
                else:
                    addedFavor = random.randint(2 * FAVOR_ADD_LEAST, 2 * FAVOR_ADD_MAX)
                    decreaseFavor = random.randint(-5 * FAVOR_ADD_MAX, -5 * FAVOR_ADD_LEAST)
                    if favorStage <= 2:
                        favorMsgAdd = user.favorAdd(decreaseFavor)
                    else:
                        favorMsgAdd = user.favorAdd(addedFavor)

                if favorStage == -3:
                    favorMsg = message.text(text = random.choice(touchReply["List_3"]))
                elif favorStage == -2:
                    favorMsg = message.text(text = random.choice(touchReply["List_2"]))
                elif favorStage == -1:
                    favorMsg = message.text(text = random.choice(touchReply["List_1"]))
                elif favorStage == 0:
                    favorMsg = message.text(text = random.choice(touchReply["List0"]))
                elif favorStage == 1:
                    favorMsg = message.text(text = random.choice(touchReply["List1"]))
                elif favorStage == 2:
                    favorMsg = message.text(text = random.choice(touchReply["List2"]))
                elif favorStage == 3:
                    favorMsg = message.text(text = random.choice(touchReply["List3"]))
                elif favorStage == 4:
                    favorMsg = message.text(text = random.choice(touchReply["List4"]))
                else:
                    favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")
            
            # 禁止触摸
            else:
                favorMsgAdd = user.favorAdd(FAVOR_DECREASE_FORBIDDEN_TOUCH)
                favorMsg = message.text(text = random.choice(touchReply["List"]))

            # 添加历史记录
            #user.recordAdd(role = "user", msg = commandText)
            #user.recordAdd(role = "assistant", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd

        commandText = backMsg.resolve()
        
        # 戳戳命令
        if commandText == "\\戳戳":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchReply)
        elif commandText == "摸头发":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchHairReply)
        elif commandText == "摸头":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchHeadReply)
        elif commandText == "摸耳朵":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchEarReply)
        elif commandText == "摸脸":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchFaceReply)
        elif commandText == "摸肚子":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchBellyReply)
        elif commandText == "摸手":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchHandReply)
        elif commandText == "摸腿":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchLegReply)
        elif commandText == "摸脚":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchFootReply)
        elif commandText == "摸肚脐":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchSensitiveReply)
        elif commandText == "摸小穴":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchSensitiveReply)
        elif commandText == "摸屁股":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchSensitiveReply)
        elif commandText == "摸鼻子" or commandText == "摸小嘴" or commandText == "摸嘴":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchWordLessReply)
        elif commandText == "摸尾巴":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchSensitiveReply)
        elif commandText == "摸眼睛":
            allMsg = __touchFavorHandle(sensitive = 2, touchReply = touchEyesReply)
        elif commandText is not None and (commandText.startswith("摸") and len(commandText) < TOUCH_COMMAND_LEN_MAX):
            allMsg = message.text(text = random.choice(touchUnknownReply["List"]))
            #user.recordAdd(role = "user", msg = commandText)
            #user.recordAdd(role = "assistant", msg = allMsg.data["text"])
        else:
            raise NameError("not me")

        return allMsg