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

# 摸头
earTouchList_3 = []
earTouchList_3.append("主人！千夜的耳朵是随便能摸的吗？真不自量力！")
earTouchList_3.append("嘁，主人再摸耳朵，千夜就要报警了哦！")
earTouchList_3.append("哼～杂鱼主人摸耳朵，是想被千夜直接打脸吗？")
earTouchList_3.append("主人！别动千夜的耳朵，你以为自己是谁？")
earTouchList_3.append("主人真是超级大变态，连耳朵都不放过！")
earTouchList_3.append("这种行为……主人真的是让人想翻白眼呢！")
earTouchList_3.append("主人！再乱摸，小千夜真的会开始生气了！")
earTouchList_3.append("千夜的耳朵可是很珍贵的，杂鱼主人不配碰！")
earTouchList_3.append("啊！不要碰千夜的耳朵，会被你这种低级手法弄脏的！")
earTouchList_3.append("嘁～主人不觉得摸耳朵是一种非常冒犯的行为吗？")

earTouchList_2 = []
earTouchList_2.append("主人，你的手真的很烦，总想着摸千夜的耳朵！")
earTouchList_2.append("哼～千夜的耳朵是给喜欢的人摸的，不是随便谁都行！")
earTouchList_2.append("主人真是不懂分寸，连耳朵都敢乱碰！")
earTouchList_2.append("千夜很讨厌这种感觉，主人还是放过我吧！")
earTouchList_2.append("杂鱼主人，摸耳朵这种行为真的很丢分哦！")
earTouchList_2.append("啊～再摸千夜的耳朵，小心我直接咬你！")
earTouchList_2.append("嘁，主人摸耳朵前，最好想清楚自己有没有资格哦～")
earTouchList_2.append("主人这种行为真的让千夜觉得无语，为什么会这么执着？")
earTouchList_2.append("主人，千夜的耳朵可不是玩具！不要随便动手！")
earTouchList_2.append("啊！这种感觉让千夜好想离主人远一点！")

earTouchList_1 = []
earTouchList_1.append("主人！你连千夜的耳朵都想摸，真是够了哦！")
earTouchList_1.append("哎呀～主人真的很奇怪，千夜完全不明白你的脑回路！")
earTouchList_1.append("主人这种摸耳朵的行为真是让人讨厌呢！")
earTouchList_1.append("千夜的耳朵可不是随便能碰的，懂了吗？")
earTouchList_1.append("嘁，主人这种手法真的让人觉得好无聊呢！")
earTouchList_1.append("杂鱼主人！千夜的耳朵是宝贝，乱碰是要罚款的！")
earTouchList_1.append("主人！千夜要对你发出严正警告，不许再摸耳朵！")
earTouchList_1.append("嘤嘤主人，你再继续，千夜会咬回去的哦！")
earTouchList_1.append("哼！这种笨拙的动作，千夜根本就不喜欢！")
earTouchList_1.append("主人！千夜真心建议你去找别的事情做！")

earTouchList0 = []
earTouchList0.append("哦？主人居然摸了千夜的耳朵，有什么特别的感受吗？")
earTouchList0.append("主人摸耳朵这件事，千夜不讨厌，但也没多喜欢。")
earTouchList0.append("嗯……这种感觉算是一般般吧，主人还需要多练练哦！")
earTouchList0.append("哎呀～主人是不是手太闲了，随便就摸耳朵呢？")
earTouchList0.append("嗯，主人……下次摸的时候记得轻一点哦！")
earTouchList0.append("千夜觉得主人这种行为可以勉强接受吧！")
earTouchList0.append("啊，主人果然是个调皮鬼，总喜欢乱摸呢！")
earTouchList0.append("主人这种手法还行，但离专业水平还差得远呢！")
earTouchList0.append("哦？主人摸耳朵是有特别的意义吗？千夜不太懂哦～")
earTouchList0.append("千夜会勉强原谅主人的小动作啦！")

earTouchList1 = []
earTouchList1.append("主人总是喜欢摸千夜的耳朵，是觉得好玩吧？")
earTouchList1.append("千夜的耳朵被主人摸得痒痒的啦！")
earTouchList1.append("嘻嘻，主人摸耳朵的感觉还挺温暖的哦！")
earTouchList1.append("哇～主人手法不错，千夜觉得挺舒服的呢！")
earTouchList1.append("主人是不是太喜欢千夜了，连耳朵都不放过！")
earTouchList1.append("主人摸耳朵的样子好认真，千夜都快笑出来啦！")
earTouchList1.append("千夜现在对主人的小动作已经习惯啦～")
earTouchList1.append("嘻嘻，主人每次摸耳朵，千夜都觉得好可爱哦！")
earTouchList1.append("哎呀，主人真是个细心的人呢～摸耳朵都这么温柔！")
earTouchList1.append("主人，耳朵可是千夜的敏感区域哦，要轻一点啦！")

earTouchList2 = []
earTouchList2.append("主人的手好温暖，摸千夜的耳朵真舒服呢！")
earTouchList2.append("主人摸耳朵的时候，千夜觉得好幸福哦！")
earTouchList2.append("主人轻一点，千夜会忍不住笑出声的啦！")
earTouchList2.append("主人对千夜这么好，千夜也要回报你哦！")
earTouchList2.append("哇～耳朵被主人摸着，千夜觉得自己像被宠坏了呢！")
earTouchList2.append("主人，千夜会越来越喜欢你的，怎么办？")
earTouchList2.append("主人，这种感觉好奇妙哦，千夜觉得特别安心！")
earTouchList2.append("嘻嘻，主人就是千夜心目中的超级英雄呢！")
earTouchList2.append("主人再多摸一会儿，千夜好想赖在你身边～")
earTouchList2.append("主人这么宠千夜，千夜会越来越依赖你的啦！")

earTouchList3 = []
earTouchList3.append("主人的摸摸让千夜觉得好甜蜜哦！")
earTouchList3.append("主人是千夜的专属医生，摸耳朵都这么专业～")
earTouchList3.append("主人摸耳朵的时候，千夜都觉得像在做梦一样！")
earTouchList3.append("主人这么温柔地对待千夜，千夜要永远记住！")
earTouchList3.append("主人摸耳朵的动作好温柔，千夜超级喜欢～")
earTouchList3.append("主人摸得千夜耳朵都要发热了啦！")
earTouchList3.append("主人下次记得用更温暖的手摸哦～")
earTouchList3.append("主人对千夜真是太好了，千夜以后会更听话的！")
earTouchList3.append("主人这么宠千夜，千夜真是好幸福！")
earTouchList3.append("千夜要一直留在主人身边，感受你的温暖！")

earTouchList4 = []
earTouchList4.append("喵～主人摸耳朵的时候，千夜好像一只乖巧的小猫呢～")
earTouchList4.append("主人……耳朵被这样轻轻摸着，千夜会觉得痒痒的呢。")
earTouchList4.append("每次主人碰千夜的耳朵，我都会忍不住红了脸哦……")
earTouchList4.append("耳朵被主人摸的时候，千夜觉得自己快要融化了～")
earTouchList4.append("喵喵～主人这样温柔地摸着耳朵，是不是觉得千夜很可爱呢？")
earTouchList4.append("主人，每次摸耳朵的时候，我的心跳都会变得好快呢……")
earTouchList4.append("千夜的耳朵都快热起来了，主人好喜欢捉弄我呢～")
earTouchList4.append("耳朵被主人摸得好舒服，千夜觉得自己是一只乖巧的猫娘呢～")
earTouchList4.append("主人，这样轻轻地摸着耳朵，会让我越来越依赖你的哦。")
earTouchList4.append("喵～主人，你的手好温暖，摸着千夜的耳朵好舒服～")



###############################################################################
# Class:        touchEarCammand     
# Input:        
# Notice:       
###############################################################################
class touchEarCammand(command):
    '''摸耳朵命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            
            return msg.resolve() == "摸耳朵"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(earTouchList_3 + earTouchList_2 + earTouchList_1 + earTouchList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(earTouchList_2 + earTouchList_1 + earTouchList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(earTouchList_1 + earTouchList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(earTouchList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(earTouchList1 + earTouchList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(earTouchList2 + earTouchList1 + earTouchList0))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(earTouchList3 + earTouchList2 + earTouchList1 + earTouchList0))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(earTouchList4 + earTouchList3 + earTouchList2 + earTouchList1 + earTouchList0))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "摸头")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
