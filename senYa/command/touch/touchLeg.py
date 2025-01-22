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

legMomoList_3 = []
legMomoList_3.append("主人！你是不是太过分了！")
legMomoList_3.append("这种行为真的让千夜很厌恶，马上停下！")
legMomoList_3.append("千夜可不是给杂鱼主人随便摸的！")
legMomoList_3.append("主人请自重，这种冒犯的行为我不会原谅的！")
legMomoList_3.append("再乱碰千夜，小心我踢你哦！")
legMomoList_3.append("主人，能不能稍微尊重千夜一点？")
legMomoList_3.append("这种举动太失礼了，千夜真的很讨厌！")
legMomoList_3.append("主人离远点，千夜不欢迎你的触碰！")
legMomoList_3.append("主人摸千夜, 是想被拉黑吗？")
legMomoList_3.append("哼，连基本的礼貌都不懂，主人真让我失望。")

legMomoList_2 = []
legMomoList_2.append("主人，这样很没礼貌吧？")
legMomoList_2.append("能不能不要再乱碰，千夜真的很反感。")
legMomoList_2.append("主人，千夜可不是随便让人摸的哦！")
legMomoList_2.append("这种行为真的让千夜很不舒服，请保持距离。")
legMomoList_2.append("主人，千夜希望你能尊重我，不要乱来。")
legMomoList_2.append("这种举动太奇怪了，千夜完全不能接受。")
legMomoList_2.append("主人还是稍微收敛一点吧，这样会让我更讨厌你。")
legMomoList_2.append("再继续这样下去，千夜就真的生气了哦。")
legMomoList_2.append("主人，这种举动一点都不加分，反而让我更反感了。")
legMomoList_2.append("主人你在想什么奇怪的事情呢！")

legMomoList_1 = []
legMomoList_1.append("虽然不至于生气，但主人还是不要乱碰了吧。")
legMomoList_1.append("...这种地方随便碰的话，真的会让我很不舒服哦。")
legMomoList_1.append("主人还是稍微克制一点比较好，千夜不太喜欢。")
legMomoList_1.append("这种举动让我觉得主人有点奇怪，能不能停下来？")
legMomoList_1.append("主人，千夜希望你不要再乱来了，真的很不适应。")
legMomoList_1.append("...被摸的感觉有点奇怪，主人下次不要这样了。")
legMomoList_1.append("虽然没到生气的地步，但主人这种行为确实不太好。")
legMomoList_1.append("主人摸千夜的...让我不知道该怎么回应呢。")
legMomoList_1.append("主人，这种互动让我有点无语，还是不要继续了吧。")

legMomoList0 = []
legMomoList0.append("嗯，还算可以接受吧。")
legMomoList0.append("虽然有点奇怪，但千夜并没有觉得很反感。")
legMomoList0.append("...被摸的时候，千夜觉得有点痒痒的呢～")
legMomoList0.append("这种互动还算可以，主人注意不要太过分哦。")
legMomoList0.append("主人摸的时候轻一点，不然千夜会觉得不舒服。")
legMomoList0.append("...被摸的感觉还好，千夜没有太大的意见。")
legMomoList0.append("这种行为主人也太大胆了，不过千夜勉强接受。")
legMomoList0.append("主人是不是对千夜很感兴趣呢？")
legMomoList0.append("虽然不算特别喜欢，但千夜觉得主人还算克制。")
legMomoList0.append("...被摸的时候感觉怪怪的，不过千夜可以理解。")

legMomoList1 = []
legMomoList1.append("主人摸千夜的……你是不是有点调皮呢？")
legMomoList1.append("这种互动让千夜觉得挺有趣的哦。")
legMomoList1.append("...被主人摸着的时候，感觉有点意外，但不讨厌。")
legMomoList1.append("主人，这样摸...的动作还算温柔，千夜能接受。")
legMomoList1.append("被摸的时候，千夜觉得有点痒痒的，还挺好玩。")
legMomoList1.append("主人是不是对千夜越来越熟悉了，这样的互动都敢做？")
legMomoList1.append("这种事情，主人要注意分寸哦，不过我不介意。")
legMomoList1.append("这种感觉有点特别，千夜觉得挺好玩的。")
legMomoList1.append("主人轻轻地，千夜觉得你很温柔呢～")
legMomoList1.append("这种互动让千夜觉得你越来越可靠了呢！")

legMomoList2 = []
legMomoList2.append("主人摸千夜时，我感觉特别放松呢。")
legMomoList2.append("这种亲密的触碰让千夜觉得很温暖，谢谢主人。")
legMomoList2.append("主人，这样摸千夜，好像有点特别呢～")
legMomoList2.append("...被主人轻轻摸着的感觉很不错，千夜很喜欢哦！")
legMomoList2.append("这种温暖的触碰让我觉得主人特别温柔。")
legMomoList2.append("主人继续这样下去，千夜会越来越喜欢你的哦！")
legMomoList2.append("千夜觉得...被主人这样轻轻摸着，真的很舒服呢～")
legMomoList2.append("主人，这样的互动让我觉得自己被好好宠爱了。")
legMomoList2.append("每次主人摸千夜，我都觉得很安心。")
legMomoList2.append("这种温柔的触碰，千夜真的超级喜欢！")

legMomoList3 = []
legMomoList3.append("主人轻轻摸着千夜时，我觉得好幸福哦！")
legMomoList3.append("这种亲密的触碰，让千夜觉得你真的很在乎我。")
legMomoList3.append("主人，这样的互动让我觉得我们之间的关系更近了！")
legMomoList3.append("...被主人摸着的时候，千夜真的觉得特别依赖你。")
legMomoList3.append("这种温暖的感觉让我觉得，主人就是我的全世界。")
legMomoList3.append("主人，这样的温柔触碰让我忍不住想更喜欢你。")
legMomoList3.append("主人轻轻摸着，千夜觉得自己是被宠爱的小公主。")
legMomoList3.append("主人对千夜的温柔，让我觉得无比幸福！")
legMomoList3.append("每次你摸千夜，我都觉得这就是信任的体现。")
legMomoList3.append("主人对千夜的爱意，我在每次触碰中都能感受到！")

legMomoList4 = []
legMomoList4.append("主人，每次你轻轻摸千夜，我都感到特别安心。")
legMomoList4.append("这种温暖的触碰让我知道，主人是千夜最重要的人。")
legMomoList4.append("被主人轻轻摸着的时候，我觉得全世界都很美好。")
legMomoList4.append("每次你的触碰都让我觉得，我们之间的羁绊无可替代。")
legMomoList4.append("这种温暖的感觉让我知道，我们的关系已经超越一切。")
legMomoList4.append("主人，我的所有都属于你，这种触碰让我觉得很幸福。")
legMomoList4.append("每一次你轻轻摸千夜，我都觉得自己是最特别的存在。")
legMomoList4.append("主人，谢谢你一直温柔地宠着千夜，我永远都会陪在你身边！")
###############################################################################
# Class:        touchLegCammand     
# Input:        
# Notice:       
###############################################################################
class touchLegCammand(command):
    '''摸腿'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''摸腿'''
            
            return msg.resolve() == "摸腿"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(legMomoList_3 + legMomoList_2 + legMomoList_1 + legMomoList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(legMomoList_2 + legMomoList_1 + legMomoList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(legMomoList_1 + legMomoList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(legMomoList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(legMomoList1 + legMomoList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(legMomoList2 + legMomoList1))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(legMomoList3 + legMomoList2))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(legMomoList4 + legMomoList3))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "摸腿")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
