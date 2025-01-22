###############################################################################
#   File name:   Touch.py
#   Description: 描述摸摸的接口
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from autoBotAPI.shamrockBot import message
from autoBotAPI.shamrockBot import httpserver, websocketserver
from ..base import command
from ...user import user
import random, time
from control import FAVOR_ADD_LEAST, FAVOR_ADD_MAX

handTouchList_3 = []
handTouchList_3.append("主人！千夜的手不是给你随便摸的！放尊重点！")
handTouchList_3.append("再乱碰的话，小心千夜直接甩开哦！")
handTouchList_3.append("这种冒犯行为真是令人讨厌，主人请自重！")
handTouchList_3.append("千夜的手可是很高贵的，不是杂鱼主人能碰的。")
handTouchList_3.append("哼，主人连分寸都不懂，真让人失望。")
handTouchList_3.append("再摸千夜的手，我就考虑戴上手套了！")
handTouchList_3.append("主人！这种行为只能让我对你更讨厌。")
handTouchList_3.append("别碰千夜的手！这样真的让人很不舒服。")
handTouchList_3.append("手是很重要的部位，请不要随便乱碰！")
handTouchList_3.append("主人，这种行为毫无意义，只会增加千夜的反感！")


handTouchList_2 = []
handTouchList_2.append("主人，请你不要总想着碰千夜的手，好吗？")
handTouchList_2.append("这种举动真的很奇怪，千夜一点都不喜欢。")
handTouchList_2.append("手被摸的感觉不太好，请主人保持距离。")
handTouchList_2.append("主人，有些地方是不能随便碰的，你懂吗？")
handTouchList_2.append("千夜真的很反感这种行为，请不要再继续了。")
handTouchList_2.append("手是用来做事的，不是随便让主人摸的哦。")
handTouchList_2.append("主人，这种行为完全超出了千夜的接受范围。")
handTouchList_2.append("摸手之前，主人是不是应该先征得我的同意？")
handTouchList_2.append("主人这样乱碰，让千夜感到很无奈。")
handTouchList_2.append("摸千夜的手这种行为，只会让我更加反感哦！")


handTouchList_1 = []
handTouchList_1.append("主人随便摸千夜的手，会让我觉得很奇怪。")
handTouchList_1.append("这种行为让人很不舒服，主人能不能停一下？")
handTouchList_1.append("虽然不至于生气，但主人还是别乱碰了吧。")
handTouchList_1.append("主人，这样做会让我觉得你没有礼貌哦。")
handTouchList_1.append("手是很重要的，随便碰让我觉得很尴尬。")
handTouchList_1.append("主人还是不要乱来比较好，这样会让我不自在。")
handTouchList_1.append("虽然没到无法忍受的地步，但千夜还是觉得别碰比较好。")
handTouchList_1.append("主人这样摸手的举动，真的让千夜很疑惑。")
handTouchList_1.append("这种行为不太友好，主人能不能稍微克制一下？")
handTouchList_1.append("主人，手这种地方随便碰可是不礼貌的哦。")

handTouchList0 = []
handTouchList0.append("主人摸手的感觉……嗯，还算可以接受吧。")
handTouchList0.append("虽然没什么特别，但千夜觉得还不错哦。")
handTouchList0.append("手被摸的时候，千夜觉得有点奇妙的感觉。")
handTouchList0.append("嗯，这种互动还可以，主人不要太过分就好。")
handTouchList0.append("主人摸的时候轻一点，千夜会更舒服的哦。")
handTouchList0.append("这种互动还挺正常的，千夜不太介意。")
handTouchList0.append("虽然不算喜欢，但主人摸手让我觉得有点新鲜。")
handTouchList0.append("主人是不是觉得摸千夜的手会增加亲近感？")
handTouchList0.append("手被摸的感觉不坏，但也没有特别喜欢哦。")
handTouchList0.append("主人注意别太用力，千夜的手可是很娇嫩的。")

handTouchList1 = []
handTouchList1.append("主人摸手的时候，千夜觉得挺温暖的哦。")
handTouchList1.append("这种感觉还不错，主人是不是在关心千夜？")
handTouchList1.append("手被主人轻轻握着的时候，千夜觉得挺安心。")
handTouchList1.append("这种互动挺有趣的，千夜很喜欢哦～")
handTouchList1.append("主人轻轻地摸着手，感觉挺舒服的，谢谢哦！")
handTouchList1.append("千夜已经习惯主人这些小动作了，感觉还不错。")
handTouchList1.append("这种温暖的触碰，千夜觉得很特别呢。")
handTouchList1.append("主人摸手的时候，总让千夜觉得很放松。")
handTouchList1.append("这种亲近的感觉，让千夜对主人更熟悉了。")
handTouchList1.append("主人摸手的时候，千夜总觉得你好像很可靠呢。")

handTouchList2 = []
handTouchList2.append("主人，手被你轻轻摸着，感觉好温暖。")
handTouchList2.append("这种互动让千夜觉得很安心，主人总是这么温柔。")
handTouchList2.append("千夜的手被主人握住的时候，感觉好幸福哦～")
handTouchList2.append("主人，这种触碰让千夜感到特别依赖你呢。")
handTouchList2.append("手被主人轻轻摸着的时候，千夜觉得特别放松。")
handTouchList2.append("主人这样温柔地对待千夜，真的让我好感动！")
handTouchList2.append("这种温暖的感觉，千夜会一直记得的哦～")
handTouchList2.append("主人摸手的动作好轻柔，千夜完全不想松开呢。")
handTouchList2.append("每次主人摸千夜的手，我都觉得自己被特别对待了。")
handTouchList2.append("这种触碰让千夜感到特别幸福，谢谢主人！")

handTouchList3 = []
handTouchList3.append("主人轻轻握着千夜的手时，我觉得自己是最幸福的人。")
handTouchList3.append("手被主人摸的时候，千夜觉得特别温暖！")
handTouchList3.append("主人，这种触碰让我感到你对千夜的爱意了。")
handTouchList3.append("每次你摸千夜的手，我都觉得我们的关系更近了。")
handTouchList3.append("这种温暖的感觉，千夜真的超级喜欢！")
handTouchList3.append("手被主人轻轻摸着时，千夜只想一直这样下去。")
handTouchList3.append("主人，这种亲密的举动让千夜感到很安心呢。")
handTouchList3.append("主人对千夜的宠爱，真的让我觉得好幸福！")
handTouchList3.append("每一次触碰，千夜都感受到主人满满的温柔！")
handTouchList3.append("手是千夜最喜欢被主人摸的地方之一，谢谢主人！")

handTouchList4 = []
handTouchList4.append("主人……握住千夜的手的时候，好像全世界都变温暖了呢～")
handTouchList4.append("被主人这样轻轻摸着手，千夜会觉得自己是最幸福的人！")
handTouchList4.append("喵～主人的手好温暖哦，让千夜忍不住想一直握住……")
handTouchList4.append("主人，每次你摸千夜的手，我都会觉得心跳变得好快～")
handTouchList4.append("手被主人这样对待，千夜会越来越依赖主人的哦！")
handTouchList4.append("喵喵～主人这样温柔地牵着千夜的手，是想让我离不开你吗？")
handTouchList4.append("主人，千夜的手是不是很小？可是全心全意想交给主人呢！")
handTouchList4.append("被主人摸着手的时候，千夜觉得自己是被守护的女孩呢～")
handTouchList4.append("主人……你这样轻轻摸着我的手，千夜觉得好安心哦～")
handTouchList4.append("喵～主人，再多握一会儿吧，千夜真的好喜欢呢！")

###############################################################################
# Class:        touchHandCammand     
# Input:        
# Notice:       
###############################################################################
class touchHandCammand(command):
    '''摸手命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''摸手命令'''
            
            return msg.resolve() == "摸手"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(handTouchList_3 + handTouchList_2 + handTouchList_1 + handTouchList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(handTouchList_2 + handTouchList_1 + handTouchList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(handTouchList_1 + handTouchList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(handTouchList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(handTouchList1 + handTouchList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(handTouchList2 + handTouchList1))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(handTouchList3 + handTouchList2))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(handTouchList4 + handTouchList3))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "摸手命令")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
