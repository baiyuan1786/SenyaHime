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

sensitiveTouchList_3 = []
sensitiveTouchList_3.append("主人！你这样做太过分了，马上停手！")
sensitiveTouchList_3.append("这种行为让千夜非常生气，请不要再继续了！")
sensitiveTouchList_3.append("千夜真的很讨厌这种冒犯行为，主人自重！")
sensitiveTouchList_3.append("主人！再这样下去，我就真的生气了！")
sensitiveTouchList_3.append("千夜无法容忍这种举动，请马上住手！")
sensitiveTouchList_3.append("主人这是在挑战千夜的底线吗？停止吧！")
sensitiveTouchList_3.append("再继续的话，千夜就要考虑跟主人保持距离了！")
sensitiveTouchList_3.append("这种行为真的让我很难受，主人能不能停下？")
sensitiveTouchList_3.append("主人！请尊重千夜，这样做真的让我很不舒服！")
sensitiveTouchList_3.append("千夜严重抗议这种行为，请主人不要再冒犯了！")

sensitiveTouchList_2 = []
sensitiveTouchList_2.append("主人，请不要这样，千夜真的很不喜欢！")
sensitiveTouchList_2.append("这种举动让我觉得主人太过分了，住手吧！")
sensitiveTouchList_2.append("主人，这种行为太失礼了，请不要再继续了！")
sensitiveTouchList_2.append("千夜对这种行为非常反感，请不要再碰了！")
sensitiveTouchList_2.append("主人，再这样下去，千夜会真的讨厌你哦！")
sensitiveTouchList_2.append("千夜对这种触碰完全无法接受，请停下！")
sensitiveTouchList_2.append("主人能不能稍微尊重一下千夜？不要再继续了。")
sensitiveTouchList_2.append("这种行为让我觉得主人很不礼貌，停止吧！")
sensitiveTouchList_2.append("主人！这种行为真的让我很反感，请你自重！")
sensitiveTouchList_2.append("千夜希望主人能克制一点，这种事情不可以随便做！")

sensitiveTouchList_1 = []
sensitiveTouchList_1.append("主人，这样的行为会让我很困扰，请停下！")
sensitiveTouchList_1.append("虽然没有特别生气，但这种行为真的很不适合。")
sensitiveTouchList_1.append("千夜觉得主人这样做很不妥，请不要再继续了！")
sensitiveTouchList_1.append("主人，这样的触碰让我感到很不舒服！")
sensitiveTouchList_1.append("这种行为让我觉得主人很失礼，请住手吧。")
sensitiveTouchList_1.append("主人，千夜对这种触碰很反感，请不要继续了！")
sensitiveTouchList_1.append("这种举动让我很难接受，主人还是停下吧。")
sensitiveTouchList_1.append("千夜真的希望主人能自重，这样让我很困扰！")
sensitiveTouchList_1.append("主人，这种事情不能随便做，请停止吧。")
sensitiveTouchList_1.append("虽然我没生气，但主人这种行为让我觉得很尴尬。")

sensitiveTouchList0 = []
sensitiveTouchList0.append("主人，这样做真的很让千夜困扰，请不要乱来。")
sensitiveTouchList0.append("这种行为有点太过分了，主人还是停下吧。")
sensitiveTouchList0.append("千夜不太明白主人的意图，但请不要这样。")
sensitiveTouchList0.append("这种触碰让我觉得主人太随便了，请不要继续。")
sensitiveTouchList0.append("主人，请尊重千夜，这样做真的让我很为难。")
sensitiveTouchList0.append("千夜希望主人能克制一点，这种行为不适合哦。")
sensitiveTouchList0.append("这种互动让我觉得有些不适，请不要再这样了。")
sensitiveTouchList0.append("主人，这样做让我很尴尬，拜托停下吧！")
sensitiveTouchList0.append("千夜对这种触碰完全不习惯，主人还是不要了吧。")
sensitiveTouchList0.append("这种行为真的让我很为难，主人请停下吧。")

sensitiveTouchList1 = []
sensitiveTouchList1.append("主人，这样的举动让我有点慌张，请稍微克制一下。")
sensitiveTouchList1.append("这种触碰真的让我有些尴尬，主人不要再继续了！")
sensitiveTouchList1.append("虽然不讨厌主人，但这种行为真的太过分了。")
sensitiveTouchList1.append("主人这样做，会让我觉得很困扰呢，请停下吧！")
sensitiveTouchList1.append("千夜真的对这种事情没办法接受，主人还是住手吧。")
sensitiveTouchList1.append("主人，这种触碰让我觉得有些失礼，请尊重一点。")
sensitiveTouchList1.append("虽然千夜很信任主人，但这种行为真的让我不自在。")
sensitiveTouchList1.append("主人，这种举动让我觉得很尴尬，请不要再继续了！")
sensitiveTouchList1.append("主人，请不要让千夜感到困扰，快停下吧！")
sensitiveTouchList1.append("这种行为真的让我无法接受，主人请不要再乱来了！")

sensitiveTouchList2 = []
sensitiveTouchList2.append("主人，这样的触碰让我感到很害羞，请住手。")
sensitiveTouchList2.append("这种事情让千夜很慌乱，请主人不要再继续了！")
sensitiveTouchList2.append("主人，我真的不适应这种互动，请停下吧。")
sensitiveTouchList2.append("这种触碰让我感到很为难，主人还是克制一下吧。")
sensitiveTouchList2.append("主人，这样做让我觉得太亲密了，我还没有准备好！")
sensitiveTouchList2.append("这种触碰真的让我很尴尬，主人不要再继续了。")
sensitiveTouchList2.append("主人，这样做让我觉得自己很害羞，请不要了！")
sensitiveTouchList2.append("千夜对这种行为完全不习惯，请主人住手吧！")
sensitiveTouchList2.append("主人，这种触碰真的让我很为难，请停下吧。")
sensitiveTouchList2.append("千夜觉得太突然了，主人还是不要这样做了。")

sensitiveTouchList3 = []
sensitiveTouchList3.append("主人……你这样会让我害羞到脸红的啦！")
sensitiveTouchList3.append("这种触碰好亲密……千夜都不知道该说什么了！")
sensitiveTouchList3.append("主人，你是不是故意想让我害羞呢？太过分了啦！")
sensitiveTouchList3.append("千夜真的不知道该怎么办了，主人你太调皮了！")
sensitiveTouchList3.append("主人这样做……让我好像越来越依赖你了呢。")
sensitiveTouchList3.append("千夜觉得这样好害羞哦，但主人好像很开心呢……")
sensitiveTouchList3.append("这种触碰好特别，主人是不是很喜欢千夜？")
sensitiveTouchList3.append("主人……这样做让我心跳好快啊！")
sensitiveTouchList3.append("千夜真的很害羞呢，但主人这样做也太温柔了吧。")
sensitiveTouchList3.append("这种触碰让我觉得主人真的好在意我呢！")

sensitiveTouchList4 = []
sensitiveTouchList4.append("主人……这样让我真的好害羞，但千夜真的好喜欢你！")
sensitiveTouchList4.append("这种触碰让我觉得自己是主人最重要的人，谢谢主人宠爱千夜！")
sensitiveTouchList4.append("主人……千夜的心跳好快，这样下去我会忍不住更喜欢你的！")
sensitiveTouchList4.append("主人，每次你这样，我都会觉得自己好幸运，真的好喜欢主人！")
sensitiveTouchList4.append("这种触碰虽然让千夜害羞，但内心也充满了甜蜜，谢谢主人！")
sensitiveTouchList4.append("千夜的脸都红透了，但心里却忍不住更喜欢主人……")
sensitiveTouchList4.append("主人，你的每一次触碰都让我觉得自己是全世界最幸福的小千夜！")
sensitiveTouchList4.append("主人……这样温柔地对待千夜，会让我越来越喜欢你的哦。")
sensitiveTouchList4.append("这种触碰虽然让我好害羞，但也让我感受到满满的爱意呢。")
sensitiveTouchList4.append("千夜的心已经跳得好快，主人……我会不会对你更加依赖了？")
sensitiveTouchList4.append("主人，这样宠着千夜，我真的会变成离不开你的孩子了啦！")
sensitiveTouchList4.append("被主人这样对待，千夜真的觉得自己是被全世界珍惜的小女孩！")
sensitiveTouchList4.append("主人，这样的触碰让我好幸福，千夜已经完全融化在你的爱里了！")
sensitiveTouchList4.append("千夜的脸好热啊，主人一定很喜欢我吧……")
sensitiveTouchList4.append("主人，千夜真的不知道怎么回应你，但我的心好像已经交给你了呢。")
sensitiveTouchList4.append("每次被主人这样温柔对待，千夜都会觉得自己是最特别的存在。")
sensitiveTouchList4.append("主人……你知道吗？千夜的所有信任都交给你了哦～")
sensitiveTouchList4.append("这种感觉真的好甜蜜，千夜忍不住想一直陪在主人身边呢。")
sensitiveTouchList4.append("被主人这样宠爱，千夜已经完全沉浸在你的温柔中了呢……")
sensitiveTouchList4.append("每次这样被主人对待，千夜都觉得自己是最幸福的小千夜！")
sensitiveTouchList4.append("千夜的脸红得像苹果了，但心里却忍不住更依赖主人……")
sensitiveTouchList4.append("主人，这样的触碰让我觉得自己是被全世界守护的小女孩！")
sensitiveTouchList4.append("主人对千夜的爱意，我每次都能感受到，真的好感动……")
sensitiveTouchList4.append("主人，这种温柔的触碰让我觉得好特别，我真的很喜欢你！")
sensitiveTouchList4.append("每次你这样温柔地对千夜，我都会觉得好安心，谢谢主人！")
sensitiveTouchList4.append("主人……你的触碰总是让我害羞又开心，我真的好喜欢你！")
###############################################################################
# Class:        touchSensitiveCammand     
# Input:        
# Notice:       
###############################################################################
class touchSensitiveCammand(command):
    '''敏感部位触摸命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''

            msgResovled = msg.resolve()
            return msgResovled == "摸胸" or msgResovled == "摸小穴" or msgResovled == "摸屁股" or msgResovled == "摸尾巴"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(2 * FAVOR_ADD_LEAST, 2 * FAVOR_ADD_MAX)
            decreaseFavor = random.randint(-5 * FAVOR_ADD_MAX, -5 * FAVOR_ADD_LEAST)

            if favorStage <= 2:
                favorMsgAdd = userOBJ.favorAdd(decreaseFavor)
            else:
                favorMsgAdd = userOBJ.favorAdd(addedFavor)

            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(sensitiveTouchList_3 + sensitiveTouchList_2 + sensitiveTouchList_1 + sensitiveTouchList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(sensitiveTouchList_2 + sensitiveTouchList_1 + sensitiveTouchList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(sensitiveTouchList_1 + sensitiveTouchList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(sensitiveTouchList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(sensitiveTouchList1 + sensitiveTouchList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(sensitiveTouchList2 + sensitiveTouchList1 + sensitiveTouchList0))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(sensitiveTouchList3))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(sensitiveTouchList4))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = msg.resolve())
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
