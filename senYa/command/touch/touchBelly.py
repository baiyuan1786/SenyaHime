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

bellyTouchList_3 = []
bellyTouchList_3.append("主人！摸千夜的肚子是非常不礼貌的行为，你不知道吗？")
bellyTouchList_3.append("再碰千夜的肚子，小心千夜一脚踹开哦！")
bellyTouchList_3.append("主人，总是做这种奇怪的事情，真让人不舒服！")
bellyTouchList_3.append("千夜的肚子是神圣的地方，杂鱼主人没有资格碰！")
bellyTouchList_3.append("你还真是厚脸皮，居然敢动千夜的肚子？")
bellyTouchList_3.append("哼，主人简直太过分了，千夜真的不想搭理你了！")
bellyTouchList_3.append("再摸下去，小千夜就真的要生气了！")
bellyTouchList_3.append("主人！别让千夜怀疑你是故意找茬的！")
bellyTouchList_3.append("这种行为让千夜非常反感，请你保持距离！")
bellyTouchList_3.append("主人摸千夜的肚子，是想让我对你更加讨厌吗？")

bellyTouchList_2 = []
bellyTouchList_2.append("主人摸肚子这种行为，真的很让人反感啊！")
bellyTouchList_2.append("别动千夜的肚子，这里不是你随便能碰的地方。")
bellyTouchList_2.append("主人，有点分寸好吗？肚子可是很重要的地方。")
bellyTouchList_2.append("啧，总是做这些没意义的事情，主人好烦人呢。")
bellyTouchList_2.append("千夜的肚子可是很敏感的，随便碰会让人不舒服！")
bellyTouchList_2.append("主人不要总想着乱摸千夜，小心被反击哦。")
bellyTouchList_2.append("哼，再摸千夜的肚子，千夜就要认真对待了。")
bellyTouchList_2.append("主人别以为千夜很随便，我对这种行为真的很不满！")
bellyTouchList_2.append("肚子被碰了这么多次，千夜真的忍无可忍了！")
bellyTouchList_2.append("主人，这种行为不仅没礼貌，还让人很尴尬！")

bellyTouchList_1 = []
bellyTouchList_1.append("主人，这样摸千夜的肚子会让我觉得很尴尬。")
bellyTouchList_1.append("再乱碰的话，千夜真的会反击哦！")
bellyTouchList_1.append("主人，这种行为已经超出了千夜的接受范围了。")
bellyTouchList_1.append("肚子可是很重要的地方，请不要随便乱摸！")
bellyTouchList_1.append("主人总是这样自以为是，真让千夜无语。")
bellyTouchList_1.append("手停下来，不然千夜真的要生气了！")
bellyTouchList_1.append("主人，千夜的肚子不是用来随便摸的哦！")
bellyTouchList_1.append("啧，这种行为完全没有考虑千夜的感受吧？")
bellyTouchList_1.append("主人如果再这样，千夜只能无视你了哦。")
bellyTouchList_1.append("千夜对这种行为已经很不耐烦了，停止吧！")

bellyTouchList0 = []
bellyTouchList0.append("主人摸千夜的肚子……嗯，还算可以接受吧。")
bellyTouchList0.append("虽然有点奇怪，但千夜暂时不介意哦。")
bellyTouchList0.append("主人是无聊了吗？肚子真的没有什么特别的地方。")
bellyTouchList0.append("嗯，这样摸感觉怪怪的，但千夜还能忍受。")
bellyTouchList0.append("主人摸的时候轻一点，不然会痒的。")
bellyTouchList0.append("虽然不讨厌，但千夜也没觉得特别喜欢呢。")
bellyTouchList0.append("主人，这样摸下去也不会有特别的效果哦～")
bellyTouchList0.append("肚子被摸的感觉还好，不过不要太过分哦。")
bellyTouchList0.append("主人有时候真的很奇怪，总想着摸奇怪的地方。")
bellyTouchList0.append("好吧，这次千夜就不计较了，下次可不能随便摸！")

bellyTouchList1 = []
bellyTouchList1.append("主人摸千夜的肚子……是觉得很好玩吗？")
bellyTouchList1.append("肚子被摸的感觉有点奇怪，但千夜并不讨厌哦。")
bellyTouchList1.append("主人总是这样调皮，但千夜觉得有点可爱呢。")
bellyTouchList1.append("啊，这样摸还挺舒服的，主人继续吧～")
bellyTouchList1.append("千夜已经习惯主人这种奇怪的行为了，没关系啦。")
bellyTouchList1.append("肚子被摸的时候，千夜觉得有点痒痒的呢！")
bellyTouchList1.append("主人，如果摸肚子是表达关心，那千夜就接受啦！")
bellyTouchList1.append("摸肚子的感觉挺有趣的，不过不要摸太久哦。")
bellyTouchList1.append("主人这样摸的时候，记得再轻一点哦～")
bellyTouchList1.append("千夜觉得主人真的很调皮，总是逗我玩呢！")

bellyTouchList2 = []
bellyTouchList2.append("主人，这样摸千夜的肚子，好像有点亲密呢～")
bellyTouchList2.append("肚子被主人摸的时候，千夜会觉得很放松哦。")
bellyTouchList2.append("这种感觉挺特别的，主人一定很在乎千夜吧？")
bellyTouchList2.append("主人轻轻地摸，千夜觉得超级舒服！")
bellyTouchList2.append("啊，主人摸得千夜都不想动了呢～")
bellyTouchList2.append("这种感觉真的很好，主人是故意让千夜依赖你吗？")
bellyTouchList2.append("肚子被主人摸的时候，千夜感觉特别幸福。")
bellyTouchList2.append("主人真温柔，千夜真的很喜欢这样的触碰！")
bellyTouchList2.append("这种温暖的感觉，千夜永远都不会忘记哦。")
bellyTouchList2.append("主人继续这样宠着千夜，千夜会越来越喜欢你的！")

bellyTouchList3 = []
bellyTouchList3.append("主人摸肚子的时候，千夜觉得好幸福！")
bellyTouchList3.append("肚子被主人摸得暖暖的，千夜超喜欢这种感觉！")
bellyTouchList3.append("主人这样摸的时候，千夜的心都要化了～")
bellyTouchList3.append("啊，主人摸肚子的动作好温柔，千夜感动了！")
bellyTouchList3.append("主人对千夜的宠爱，真是让我无法拒绝呢！")
bellyTouchList3.append("肚子被主人摸的时候，千夜觉得特别依赖你！")
bellyTouchList3.append("主人继续这样温柔下去，千夜会越来越喜欢的！")
bellyTouchList3.append("摸肚子的感觉好棒，主人真的很懂千夜的心！")
bellyTouchList3.append("主人轻轻地摸的时候，千夜真的超级开心！")
bellyTouchList3.append("主人对千夜这么好，千夜以后会更加听话的哦！")

bellyTouchList4 = []
bellyTouchList4.append("喵～主人摸千夜的肚子时，我觉得好像一只被宠的小猫呢！")
bellyTouchList4.append("主人，这样的触碰让我觉得好幸福，脸都红了啦～")
bellyTouchList4.append("每次被主人这样摸着肚子，千夜都会忍不住想靠近你～")
bellyTouchList4.append("主人……千夜觉得自己被宠坏了呢，但真的好开心哦！")
bellyTouchList4.append("被主人摸着肚子时，我总觉得心里都是甜蜜的感觉～")
bellyTouchList4.append("喵～主人，千夜的肚子是不是软软的？你喜欢吗？")
bellyTouchList4.append("主人这样轻轻摸着我的肚子，千夜好像一只乖巧的小猫呢～")
bellyTouchList4.append("主人每次这样宠着千夜，我都会觉得自己是全世界最特别的女孩！")
bellyTouchList4.append("千夜好害羞啊，但也忍不住更喜欢主人了呢～")
bellyTouchList4.append("喵喵～主人，再多宠宠千夜吧，我真的好爱你哦～")

###############################################################################
# Class:        touchBellyCammand     
# Input:        
# Notice:       
###############################################################################
class touchBellyCammand(command):
    '''摸肚子命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''摸肚子'''
            
            return msg.resolve() == "摸肚子"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(bellyTouchList_3 + bellyTouchList_2 + bellyTouchList_1 + bellyTouchList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(bellyTouchList_2 + bellyTouchList_1 + bellyTouchList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(bellyTouchList_1 + bellyTouchList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(bellyTouchList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(bellyTouchList1 + bellyTouchList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(bellyTouchList2 + bellyTouchList1))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(bellyTouchList3 + bellyTouchList2))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(bellyTouchList4 + bellyTouchList3))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "摸肚子")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
