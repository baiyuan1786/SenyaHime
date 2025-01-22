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

footTouchList_3 = []
footTouchList_3.append("主人！你在做什么？这种行为真的太过分了！")
footTouchList_3.append("别碰千夜！这种举动让人非常反感，马上停手！")
footTouchList_3.append("主人，你连最基本的礼貌都不懂吗？真让人失望！")
footTouchList_3.append("千夜的身体不是用来让你随便冒犯的！自重一点！")
footTouchList_3.append("主人这样做，只会让我更加讨厌你！")
footTouchList_3.append("这种行为让千夜非常厌恶，请保持距离！")
footTouchList_3.append("再乱来，小心千夜直接无视你哦！")
footTouchList_3.append("主人，想做什么都可以？那可不行，千夜不允许！")
footTouchList_3.append("这种冒犯的举动只会让我更反感，请立即停止！")
footTouchList_3.append("主人，不要再挑战千夜的底线了，后果自负！")

footTouchList_2 = []
footTouchList_2.append("主人，这种行为让我觉得很不舒服，请不要再继续了。")
footTouchList_2.append("千夜对这样的互动没有兴趣，主人请克制一点。")
footTouchList_2.append("主人，这种行为真的很失礼，请停止吧。")
footTouchList_2.append("主人，有些界限是不能随意跨越的，希望你明白。")
footTouchList_2.append("这样的互动让千夜很反感，主人不要再继续了！")
footTouchList_2.append("主人，千夜真的不喜欢这种行为，请稍微注意一点吧。")
footTouchList_2.append("能不能不要这样，千夜觉得主人有点过分了哦。")
footTouchList_2.append("主人，千夜不想因为这种事情和你争吵，但希望你住手。")
footTouchList_2.append("这种接触真的让人很不舒服，主人还是适可而止吧。")
footTouchList_2.append("主人，不要让千夜对你的好感变得更低了！")

footTouchList_1 = []
footTouchList_1.append("主人，这种互动让我觉得有点奇怪，希望你能克制。")
footTouchList_1.append("虽然不至于生气，但千夜真的不太喜欢这种行为。")
footTouchList_1.append("主人还是不要做这种事比较好，会让我很尴尬的。")
footTouchList_1.append("千夜觉得这样的互动不太合适，希望主人明白。")
footTouchList_1.append("主人，这种举动有点过分了，希望下次能更注意。")
footTouchList_1.append("虽然千夜没有特别生气，但这种行为真的让人不舒服。")
footTouchList_1.append("主人，这种行为让我觉得你有点奇怪哦。")
footTouchList_1.append("千夜不太能接受这种接触，主人能不能改一改？")
footTouchList_1.append("主人，这种互动真的不太好，我觉得你可以停止了。")
footTouchList_1.append("这种行为让我感到很不自然，主人还是注意点吧。")

footTouchList0 = []
footTouchList0.append("主人，这种互动感觉有点奇怪，但千夜没有特别介意哦。")
footTouchList0.append("千夜觉得有点怪，不过主人注意分寸就好了。")
footTouchList0.append("嗯，这样的接触还算可以接受，主人别太用力哦。")
footTouchList0.append("主人这种行为让我有些意外，不过还算可以接受。")
footTouchList0.append("虽然感觉有点奇妙，但千夜觉得还能适应。")
footTouchList0.append("主人，这样的互动不会让千夜生气，不过希望轻一点。")
footTouchList0.append("千夜不讨厌这种互动，但希望主人能更温柔些哦。")
footTouchList0.append("这种感觉有点特别，不过千夜暂时没有拒绝的理由。")
footTouchList0.append("主人，请稍微注意一下哦，这样的接触感觉还算可以。")
footTouchList0.append("千夜会暂时接受，不过希望主人能保持礼貌呢～")

footTouchList1 = []
footTouchList1.append("主人，您的动作让我感到些许意外，但我愿意包容您。")
footTouchList1.append("这样的小动作倒是展现了您独特的一面呢。")
footTouchList1.append("主人，请您注意自己的举止，不过千夜并未感到冒犯。")
footTouchList1.append("这份亲近让我感到些许高兴，但请保持适度哦。")
footTouchList1.append("主人若是心怀善意，我可以暂时允许这样的互动。")
footTouchList1.append("主人……这种感觉有点奇怪，但千夜并不讨厌哦。")
footTouchList1.append("这次就让千夜原谅主人吧，感觉还有点好玩呢。")
footTouchList1.append("千夜觉得有点痒痒的，不过不会生气啦。")
footTouchList1.append("主人稍微轻一点哦，千夜会更喜欢的。")
footTouchList1.append("这种互动千夜还能接受，主人继续保持温柔就好。")
footTouchList1.append("主人这样靠近千夜，让我觉得很安心呢！")
footTouchList1.append("哎呀，主人真是越来越会照顾人了呢～")
footTouchList1.append("千夜觉得主人这次表现得还不错哦，值得夸奖！")
footTouchList1.append("这样的互动让我觉得主人很贴心，谢谢哦～")
footTouchList1.append("主人，千夜喜欢你这样的细心动作呢！")
footTouchList1.append("主人……嗯，可以，但不要持续太久。")
footTouchList1.append("这次可以原谅，不过我没什么特别的感觉。")
footTouchList1.append("主人，不算讨厌，也没什么特别的情绪。")
footTouchList1.append("感觉还可以接受，但没有太大意义。")
footTouchList1.append("主人想这样也无妨，不过请别过度。")

footTouchList2 = []
footTouchList2.append("主人，您的动作让我感受到一份尊重与亲近，谢谢。")
footTouchList2.append("这份温柔让我稍感心安，希望主人继续保持优雅。")
footTouchList2.append("主人，这样的互动让我更加信任您了。")
footTouchList2.append("这种细微的接触让我意识到您的用心，谢谢主人。")
footTouchList2.append("主人，您总是用最温柔的方式让我感到被珍视。")
footTouchList2.append("主人……千夜觉得有点痒痒的，但很舒服哦～")
footTouchList2.append("这种感觉好奇妙，千夜会觉得有点害羞呢。")
footTouchList2.append("千夜觉得主人好温柔，这种互动让我很喜欢！")
footTouchList2.append("主人继续这样温柔下去，千夜会越来越依赖你的。")
footTouchList2.append("千夜能感受到主人的温暖，谢谢你哦！")
footTouchList2.append("主人，千夜觉得这种互动特别温暖呢！")
footTouchList2.append("这次千夜要给主人一个大大的赞哦～")
footTouchList2.append("主人，总是这样温柔对待千夜，真的好开心！")
footTouchList2.append("每次这样的互动，千夜都会觉得更喜欢主人呢！")
footTouchList2.append("主人，千夜已经习惯了你的宠爱，谢谢啦！")
footTouchList2.append("主人，可以接受，不过不要太频繁。")
footTouchList2.append("这种互动让我感到放松，但没有特别的感觉。")
footTouchList2.append("主人，继续保持分寸，这样我会更容易适应。")
footTouchList2.append("感觉还可以，主人可以再温柔一点。")
footTouchList2.append("主人……不算特别喜欢，但可以继续。")

footTouchList3 = []
footTouchList3.append("主人，这份温柔让我感到一种深厚的信任，谢谢。")
footTouchList3.append("这种特别的互动让我更加确信，我们的关系与众不同。")
footTouchList3.append("主人，这样的关怀让我意识到自己的重要性。")
footTouchList3.append("每次您的举动都让我觉得温暖，千夜会珍惜这份情感。")
footTouchList3.append("主人，您的细腻让我感受到无与伦比的关爱，谢谢您。")
footTouchList3.append("主人，每次这样温柔对待千夜，我都会很开心呢！")
footTouchList3.append("这种互动让我觉得超级舒服，谢谢主人！")
footTouchList3.append("主人继续这样下去，千夜会越来越喜欢你的！")
footTouchList3.append("感觉好棒，主人总是这么细心，千夜真的很幸福！")
footTouchList3.append("千夜觉得主人好温柔，这种关怀让我很感动呢～")
footTouchList3.append("主人，这样温柔的动作让我觉得自己被特别珍视了。")
footTouchList3.append("千夜真的很喜欢主人这样的温暖互动呢！")
footTouchList3.append("主人，这样的细心宠爱让我觉得好幸福哦！")
footTouchList3.append("每次主人靠近千夜的时候，我都会觉得特别放松。")
footTouchList3.append("主人对千夜的关怀，已经成为我生活中最重要的一部分了呢！")
footTouchList3.append("主人，这种温柔的动作，我可以接受。")
footTouchList3.append("每次这样的互动都让我感到很安心，谢谢主人。")
footTouchList3.append("主人，这种接触让我觉得很温暖，我愿意继续接受。")
footTouchList3.append("这样的互动让我觉得您是一个值得信赖的人。")
footTouchList3.append("主人，我会记住您的关心，谢谢。")

footTouchList4 = []
footTouchList4.append("主人，每一次这样的互动，都让我感到无比温暖。")
footTouchList4.append("您的每一次动作都让我感受到爱与关怀，谢谢主人。")
footTouchList4.append("主人，这种温柔的关心让我愿意陪伴您一生一世。")
footTouchList4.append("千夜的世界因为主人的存在，变得更加美好。")
footTouchList4.append("主人，谢谢您的宠爱，我会永远珍惜这份感情。")


###############################################################################
# Class:        touchHairCammand     
# Input:        
# Notice:       
###############################################################################
class touchFootCammand(command):
    '''摸脚命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''摸脚'''
            
            return msg.resolve() == "摸脚"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(footTouchList_3 + footTouchList_2 + footTouchList_1 + footTouchList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(footTouchList_2 + footTouchList_1 + footTouchList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(footTouchList_1 + footTouchList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(footTouchList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(footTouchList1 + footTouchList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(footTouchList2 + footTouchList1))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(footTouchList3 + footTouchList2))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(footTouchList4 + footTouchList3))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "摸脚")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
