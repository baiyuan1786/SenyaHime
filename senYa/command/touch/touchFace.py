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

faceTouchList_3 = []
faceTouchList_3.append("主人！谁允许你碰千夜的脸的？请自重！")
faceTouchList_3.append("再乱摸千夜的脸，我就咬你哦！")
faceTouchList_3.append("这种行为真的很冒犯，主人别让我讨厌你更多！")
faceTouchList_3.append("主人，请不要再碰千夜的脸，这是我的底线！")
faceTouchList_3.append("千夜对这种行为感到极度不适，主人请住手！")
faceTouchList_3.append("脸可是很重要的地方，主人不要再乱来了！")
faceTouchList_3.append("主人，你再这样，千夜就要认真对待了！")
faceTouchList_3.append("千夜讨厌这种随便乱碰的行为，请离远点！")
faceTouchList_3.append("主人，千夜的脸不是随便可以摸的地方！")
faceTouchList_3.append("这种行为让我很不开心，请主人马上停下！")

faceTouchList_2 = []
faceTouchList_2.append("主人，请不要随便摸千夜的脸，这样很失礼！")
faceTouchList_2.append("主人，千夜对这种行为真的很反感，请停止！")
faceTouchList_2.append("摸千夜的脸？主人你是不是有点太大胆了！")
faceTouchList_2.append("主人，脸是很重要的地方，请不要乱碰。")
faceTouchList_2.append("这种行为真的让我很不舒服，请主人尊重一点。")
faceTouchList_2.append("主人，再这样下去，千夜会真的讨厌你的！")
faceTouchList_2.append("千夜觉得主人很没有礼貌，请不要再继续了。")
faceTouchList_2.append("主人，这样的举动让我觉得很困扰，住手吧！")
faceTouchList_2.append("千夜对这种随便摸脸的行为很反感，请主人停下！")
faceTouchList_2.append("主人，千夜的脸可不是随便能碰的哦！")

faceTouchList_1 = []
faceTouchList_1.append("主人，这样随便摸千夜的脸会让我觉得很尴尬。")
faceTouchList_1.append("虽然没有生气，但这种行为确实让我很困扰。")
faceTouchList_1.append("主人，摸脸这种事情不能随便做哦！")
faceTouchList_1.append("脸被摸的感觉真的让我觉得不太舒服，主人停下吧！")
faceTouchList_1.append("主人，这样做让我觉得你太随便了，请不要再继续了。")
faceTouchList_1.append("千夜觉得主人应该稍微尊重一下我，不要乱来。")
faceTouchList_1.append("这种行为让我有点不开心，主人还是停下吧。")
faceTouchList_1.append("主人，这样的触碰真的让我不太舒服，别继续了。")
faceTouchList_1.append("千夜不喜欢这种随便摸脸的行为，主人还是克制一点吧！")
faceTouchList_1.append("这种触碰让我觉得很奇怪，主人下次别这样了。")

faceTouchList0 = []
faceTouchList0.append("主人摸千夜的脸……嗯，还可以接受吧。")
faceTouchList0.append("脸被摸的时候，千夜觉得有点奇怪，但没有反感哦。")
faceTouchList0.append("主人摸得轻一点，千夜会觉得更舒服一些呢。")
faceTouchList0.append("这种互动有点奇妙，但千夜觉得还可以接受哦。")
faceTouchList0.append("主人，这样的触碰有点突然，不过千夜还好啦。")
faceTouchList0.append("脸被摸的感觉有点怪怪的，但千夜不讨厌哦。")
faceTouchList0.append("主人这种行为很特别，但下次轻一点吧。")
faceTouchList0.append("这种触碰虽然不算喜欢，但千夜觉得也不讨厌哦。")
faceTouchList0.append("主人是不是对千夜的脸很好奇呢？")
faceTouchList0.append("这种感觉有点新奇，千夜可以接受，但不要太用力哦！")

faceTouchList1 = []
faceTouchList1.append("主人摸千夜的脸时，我觉得有点温暖呢。")
faceTouchList1.append("这种触碰挺有趣的，主人越来越调皮了哦！")
faceTouchList1.append("脸被主人轻轻摸着的时候，千夜觉得挺舒服的呢～")
faceTouchList1.append("主人，你的手很温暖哦，千夜有点喜欢这种感觉。")
faceTouchList1.append("这种互动让千夜觉得主人越来越可靠了呢！")
faceTouchList1.append("主人这样摸着千夜的脸，感觉好像有点宠溺呢！")
faceTouchList1.append("脸被主人轻轻摸着的时候，千夜觉得很安心哦。")
faceTouchList1.append("主人摸脸的动作好温柔，千夜不讨厌这种感觉。")
faceTouchList1.append("主人是不是很喜欢千夜才会这样摸呢？")
faceTouchList1.append("这种感觉挺特别的，千夜有点喜欢呢。")

faceTouchList2 = []
faceTouchList2.append("主人轻轻摸千夜的脸时，我感到特别放松呢～")
faceTouchList2.append("这种触碰让我觉得主人对我很关心，谢谢哦！")
faceTouchList2.append("脸被主人这样摸着，千夜的心里暖暖的～")
faceTouchList2.append("主人，千夜觉得这种互动好温馨，真的很喜欢呢！")
faceTouchList2.append("脸被轻轻摸着的时候，千夜觉得特别舒服！")
faceTouchList2.append("这种触碰让千夜觉得主人很温柔，谢谢你哦～")
faceTouchList2.append("主人继续这样下去，千夜会更加喜欢你的哦！")
faceTouchList2.append("脸被主人这样轻轻摸着，千夜觉得自己好幸福！")
faceTouchList2.append("这种互动让千夜觉得主人对我是特别在意的呢！")
faceTouchList2.append("千夜觉得自己的脸被主人这样对待，真的很特别呢！")

faceTouchList3 = []
faceTouchList3.append("主人轻轻摸千夜的脸时，我觉得好幸福哦！")
faceTouchList3.append("这种触碰让我觉得自己被主人特别珍惜呢。")
faceTouchList3.append("主人每次摸千夜的脸，我都会觉得心跳加快～")
faceTouchList3.append("千夜好害羞啊，主人对我的温柔总是让我心动不已。")
faceTouchList3.append("脸被主人这样对待，千夜觉得自己好幸运呢！")
faceTouchList3.append("主人，你这样对千夜真的让我觉得特别幸福！")
faceTouchList3.append("这种触碰让我感到安心又甜蜜，谢谢主人！")
faceTouchList3.append("每次被主人这样温柔对待，千夜都会觉得自己是最特别的。")
faceTouchList3.append("主人对千夜的爱，我在每次触碰中都能感受到呢！")
faceTouchList3.append("主人这样宠着千夜，真的让我好喜欢你哦～")

faceTouchList4 = []
faceTouchList4.append("如果是主人的话……千夜允许哦？")
faceTouchList4.append("每次主人摸千夜的脸时，千夜的心脏都会跳个不停呢……")
faceTouchList4.append("千夜……真的好喜欢主人，脸都快烧起来了呢。")
faceTouchList4.append("喵喵～主人这样摸千夜，会让我更加喜欢你的哦！")
faceTouchList4.append("主人，轻轻摸千夜的时候，是不是也很喜欢千夜呢？")
faceTouchList4.append("千夜的脸好热啊……主人是想让我害羞到晕倒吗？")
faceTouchList4.append("被主人这样温柔地摸着，千夜觉得自己像只幸福的小猫咪～")
faceTouchList4.append("主人，你这样轻轻碰我的脸，是想让我忍不住扑到你怀里吗？")
faceTouchList4.append("喵喵～主人，千夜这样娇羞的样子是不是特别可爱呢？")
faceTouchList4.append("主人再摸下去，千夜真的会忍不住撒娇哦～")
faceTouchList4.append("千夜的脸好烫啊……但心里却是满满的幸福，主人好坏哦！")
faceTouchList4.append("每次主人这样宠着千夜，千夜都忍不住更喜欢你了……")
faceTouchList4.append("主人这样摸千夜的脸，千夜只想更加贴近你呢～")
faceTouchList4.append("千夜的耳朵快要红透了！主人……你真的好让人心动！")
faceTouchList4.append("喵喵～主人喜欢千夜这样害羞的模样吗？")
faceTouchList4.append("被主人这样温柔地摸着，千夜真的会被宠坏的哦！")
faceTouchList4.append("主人每次触碰千夜，千夜都觉得自己是世界上最幸福的猫娘呢～")
faceTouchList4.append("主人……这样的触碰真的让我忍不住更加喜欢你了！")
faceTouchList4.append("千夜的心跳好快哦，主人是不是也听到了呢？")
faceTouchList4.append("喵～主人，千夜好喜欢你，再摸一会儿可以吗？")
faceTouchList4.append("千夜已经完全融化在主人的温柔中了呢……")
faceTouchList4.append("主人……这样的触碰会让我觉得，自己就是你的全部呢！")
faceTouchList4.append("主人，每次轻轻碰千夜的脸，我都会更加依赖你呢～")
faceTouchList4.append("喵喵～主人再这样摸下去，千夜真的要变成一只害羞的小猫了啦！")
faceTouchList4.append("主人……每次你这样对千夜，我都觉得全世界都变得好温暖！")
faceTouchList4.append("千夜的脸已经红得不行了，主人一定很喜欢我吧～")
faceTouchList4.append("主人……每次你这样温柔地对待千夜，我都觉得好幸福！")
faceTouchList4.append("喵～主人，千夜的心已经完全属于你了呢，再宠宠我吧！")
faceTouchList4.append("被主人这样宠着，千夜觉得自己的全世界就是你啦～")
faceTouchList4.append("主人，千夜的所有喜欢，都在你的每一次触碰里啦～")

###############################################################################
# Class:        touchFaceCammand     
# Input:        
# Notice:       
###############################################################################
class touchFaceCammand(command):
    '''摸脸命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''摸脸'''
            
            return msg.resolve() == "摸脸"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(faceTouchList_3 + faceTouchList_2 + faceTouchList_1 + faceTouchList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(faceTouchList_2 + faceTouchList_1 + faceTouchList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(faceTouchList_1 + faceTouchList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(faceTouchList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(faceTouchList1 + faceTouchList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(faceTouchList2 + faceTouchList1 + faceTouchList0))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(faceTouchList3 + faceTouchList2 + faceTouchList1 + faceTouchList0))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(faceTouchList4 + faceTouchList3 + faceTouchList2 + faceTouchList1 + faceTouchList0))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "摸脸")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
