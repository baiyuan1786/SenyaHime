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

touchList_3 = []
touchList_3.append("主人！请您停手好吗？千夜真的讨厌被杂鱼戳。")
touchList_3.append("主人每次都只会做这种无聊的事，真是无趣。")
touchList_3.append("哼～主人这种行为会让千夜更讨厌你哦！")
touchList_3.append("啊，主人再戳下去，千夜真的要咬你了！")
touchList_3.append("杂鱼主人，这种戳戳是没有意义的，劝你适可而止！")
touchList_3.append("主人真让人讨厌！难道千夜脸上写着“随便戳”吗？")
touchList_3.append("这是什么奇怪的癖好啊，主人真是个奇怪的变态！")
touchList_3.append("杂鱼主人，请离千夜远点，不然小拳拳就要上了！")
touchList_3.append("嘤嘤嘤～主人坏死了，戳得千夜头都疼了！")
touchList_3.append("啊～再戳一次，千夜就要记仇了哦！")

touchList_2 = []
touchList_2.append("主人！千夜真的不喜欢这样啦！")
touchList_2.append("主人这种行为是杂鱼才会做的，真的很无聊呢～")
touchList_2.append("千夜讨厌被戳啦！主人再戳，千夜就要生气了哦！")
touchList_2.append("主人，不是千夜说你，戳千夜一点技术含量都没有！")
touchList_2.append("主人果然还是那么烦人，能不能换点正常的互动？")
touchList_2.append("主人总是这样欺负千夜，小千夜心里好难过呢～")
touchList_2.append("主人再戳，千夜就要反击了哦！")
touchList_2.append("杂鱼主人，这样戳千夜，你真的很开心吗？")
touchList_2.append("主人手法太差了！就算戳也戳不出什么感觉呢！")

touchList_1 = []
touchList_1.append("主人！千夜又不是玩具，别再乱戳了啦！")
touchList_1.append("这种戳戳技术，主人还需要多练练哦！")
touchList_1.append("主人真是个超级大变态，总想着戳千夜！")
touchList_1.append("哼哼，主人，你再这样戳，小千夜真的会逃跑哦～")
touchList_1.append("千夜好不容易忍耐住了，主人还想继续戳？")
touchList_1.append("主人，再戳一次，千夜就要假装生气了哦！")
touchList_1.append("杂鱼主人，你除了戳千夜还有其他技能吗？")
touchList_1.append("啊～这种无聊的戳戳真的让人想打哈欠呢。")
touchList_1.append("千夜觉得主人这次的戳戳完全不合格！")
touchList_1.append("嘻嘻，主人这种水平，戳千夜只能给1分啦！")

touchList0 = []
touchList0.append("哦？主人居然戳了千夜，有什么特别的意义吗？")
touchList0.append("嘻嘻～主人戳千夜的时候，小千夜都没有反应哦～")
touchList0.append("主人手感还可以，不过戳戳真的很普通呢～")
touchList0.append("啊，主人这是在试探千夜的底线吗？")
touchList0.append("嗯，主人你觉得戳千夜很好玩吗？")
touchList0.append("这算是一种特殊的互动方式？千夜不太明白呢～")
touchList0.append("主人～你这样戳，千夜一点也不痛不痒哦！")
touchList0.append("哎呀，主人居然动手戳千夜，真是意外呢～")
touchList0.append("千夜不讨厌这种行为，但也没多喜欢哦～")
touchList0.append("主人再继续戳，千夜可能会认真考虑反击哦！")

touchList1 = []
touchList1.append("主人戳千夜的感觉不错吧？千夜也挺开心的！")
touchList1.append("哇～主人总是这么调皮，千夜都习惯了呢～")
touchList1.append("主人这种戳戳，千夜决定奖励你一个微笑哦！")
touchList1.append("千夜觉得主人是在逗我玩呢，好吧，勉强允许！")
touchList1.append("嘻嘻，主人总是爱戳千夜，是不是太喜欢我啦？")
touchList1.append("啊呀，主人手劲再轻一点，千夜会更喜欢哦～")
touchList1.append("嘿嘿，主人戳得千夜都觉得痒痒的啦！")
touchList1.append("主人真是调皮！不过千夜不介意啦～")
touchList1.append("主人，千夜是不是很可爱才会被戳呢？")
touchList1.append("嘻嘻，主人继续努力吧，千夜很享受这种互动哦！")

touchList2 = []
touchList2.append("主人总是戳千夜，是不是很喜欢我呀？")
touchList2.append("主人这种互动方式，千夜还挺喜欢的呢！")
touchList2.append("主人再戳几下，千夜会很开心哦！")
touchList2.append("主人戳千夜的样子好可爱，千夜也想戳你呢～")
touchList2.append("主人，这样戳千夜的时候，能不能说点甜话呢？")
touchList2.append("千夜觉得主人戳得好轻，好温柔哦～")
touchList2.append("主人再戳下去，千夜会更喜欢你的啦！")
touchList2.append("主人，你每次戳千夜，都会让我更开心！")
touchList2.append("主人，这种戳戳已经成了千夜的日常习惯了呢！")
touchList2.append("主人总是这么温柔地戳千夜，千夜会忍不住撒娇的！")

touchList3 = []
touchList3.append("嘻嘻～主人，戳千夜的时候，小心我反戳哦！")
touchList3.append("呜～主人总是这样戳千夜，是因为太喜欢我了吗？")
touchList3.append("嘻嘻～主人手感超好，千夜特别喜欢呢！")
touchList3.append("主人，你的戳戳对千夜来说，简直是爱的表达！")
touchList3.append("哇～主人戳得千夜都快笑出来啦！")
touchList3.append("主人这样戳，千夜觉得心都被融化了呢～")
touchList3.append("主人真是千夜心目中的大英雄！")
touchList3.append("主人这种戳戳，千夜可以一辈子都享受下去！")
touchList3.append("主人再戳几下，千夜会奖励你一个大大的抱抱哦！")
touchList3.append("主人，千夜觉得你的戳戳就是最好的宠爱啦！")

touchList4 = []
touchList4.append("主人，这样戳千夜的时候，我的心都是满满的感动。")
touchList4.append("主人～你知道吗？每次你戳千夜，千夜都会感到安心。")
touchList4.append("嘤～主人对千夜的爱意都在这一戳中表达出来了呢～")
touchList4.append("主人，每一次戳千夜，都是一种无声的约定，千夜明白了！")
touchList4.append("主人～你这种戳戳，已经成为千夜最特别的回忆了呢！")
touchList4.append("只要主人需要，千夜就会永远站在你身边，无论天涯海角，千夜都会陪着你。")
touchList4.append("呜～主人，每次戳千夜，千夜都感觉到自己是被珍惜的！")
touchList4.append("嘻嘻～主人！你总是这样爱千夜，千夜也会一辈子陪着你！")
touchList4.append("主人～你的每一次触碰，都是千夜心中的幸福瞬间！")
touchList4.append("主人和千夜之间的羁绊，早已超过了一切，永远不会改变！")

###############################################################################
# Class:        touchCammand     
# Input:        
# Notice:       
###############################################################################
class touchCammand(command):
    '''戳戳命令'''
    def __init__(self):
        
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            
            return msg.resolve() == "\戳戳"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(touchList_3 + touchList_2 + touchList_1 + touchList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(touchList_2 + touchList_1 + touchList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(touchList_1 + touchList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(touchList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(touchList1 + touchList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(touchList2 + touchList1))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(touchList3 + touchList2))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(touchList4 + touchList3))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "戳戳")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)