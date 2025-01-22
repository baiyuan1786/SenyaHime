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

hairMomoList_3 = []
hairMomoList_3.append("主人！谁允许你碰千夜的头发的？这是侵犯！")
hairMomoList_3.append("再乱动千夜的头发，小心我剪掉让你没得摸！")
hairMomoList_3.append("千夜的头发是很珍贵的东西，杂鱼主人不要乱碰！")
hairMomoList_3.append("这种行为真的很失礼，主人还是自重一点吧！")
hairMomoList_3.append("千夜警告，再动一下头发，我就会报复哦！")
hairMomoList_3.append("主人，摸头发之前是不是应该先问问千夜的意见？")
hairMomoList_3.append("哼，连头发都要碰，主人真是过分了！")
hairMomoList_3.append("这种行为只会让千夜更加讨厌你，请保持距离！")
hairMomoList_3.append("主人难道不觉得这样很让人厌烦吗？")
hairMomoList_3.append("头发是千夜的宝物，主人根本不配碰！")

hairMomoList_2 = []
hairMomoList_2.append("主人，千夜真的不喜欢别人随便碰我的头发。")
hairMomoList_2.append("这种行为让人不舒服，头发不是随便能碰的哦！")
hairMomoList_2.append("主人，摸千夜的头发之前，有考虑过我的感受吗？")
hairMomoList_2.append("请不要随意动千夜的头发，这样很没礼貌。")
hairMomoList_2.append("头发是很重要的东西，主人能不能别乱来？")
hairMomoList_2.append("主人这种行为真的很烦人，可以停止了吗？")
hairMomoList_2.append("再碰千夜的头发，我就真的要生气了哦！")
hairMomoList_2.append("主人，千夜的头发可不是给随便摸的！")
hairMomoList_2.append("摸头发这种事，主人能不能稍微注意点分寸？")
hairMomoList_2.append("千夜不想因为这件事和主人起冲突，请自重！")

hairMomoList_1 = []
hairMomoList_1.append("主人，这样随便摸千夜的头发，会让我觉得很奇怪。")
hairMomoList_1.append("虽然没到不能忍受的地步，但主人还是别乱碰吧。")
hairMomoList_1.append("千夜对这种行为感到不太高兴，主人能不能收手？")
hairMomoList_1.append("头发是很重要的，随便摸会让人很没安全感哦。")
hairMomoList_1.append("主人可以克制一点吗？头发不是可以乱碰的地方。")
hairMomoList_1.append("千夜觉得主人这样有点冒失，头发不该随便动哦。")
hairMomoList_1.append("虽然没有很生气，但主人还是稍微注意一点吧。")
hairMomoList_1.append("头发被乱碰的感觉很不好，请主人尊重一点。")
hairMomoList_1.append("主人摸得千夜很无奈，我不知道该怎么回应了。")
hairMomoList_1.append("这种行为真的不太让人喜欢，希望主人能停止。")

hairMomoList0 = []
hairMomoList0.append("主人摸头发的感觉……嗯，还算可以接受吧。")
hairMomoList0.append("虽然有点奇怪，但千夜不讨厌这种互动。")
hairMomoList0.append("头发被摸的时候，千夜觉得有点痒痒的呢～")
hairMomoList0.append("嗯，主人摸得还行，不过也没什么特别的感觉。")
hairMomoList0.append("这种互动还算可以，不过主人记得不要弄乱哦。")
hairMomoList0.append("主人是不是很喜欢千夜的头发才会一直摸呢？")
hairMomoList0.append("摸头发的感觉很普通，不过千夜没意见哦。")
hairMomoList0.append("主人下次摸的时候轻一点，这样会更舒服。")
hairMomoList0.append("虽然不太明白主人的用意，但千夜觉得还可以。")
hairMomoList0.append("头发被摸的时候有点奇怪，但千夜不讨厌哦。")

hairMomoList1 = []
hairMomoList1.append("主人摸头发的时候，千夜觉得有点温暖哦。")
hairMomoList1.append("这种互动挺有趣的，主人好像很喜欢千夜的头发呢。")
hairMomoList1.append("头发被主人摸的时候，感觉还挺放松的呢。")
hairMomoList1.append("主人这样轻轻地摸着，千夜觉得挺舒服的。")
hairMomoList1.append("头发被摸的时候，千夜觉得有点奇妙，但不讨厌哦。")
hairMomoList1.append("主人对千夜这么温柔，摸头发都让我觉得特别安心。")
hairMomoList1.append("这种感觉挺特别的，千夜觉得主人越来越可靠了。")
hairMomoList1.append("千夜已经习惯主人的这些小动作了，感觉还不错。")
hairMomoList1.append("主人摸头发的时候，千夜总觉得你好像在照顾我。")
hairMomoList1.append("这种亲近的感觉还挺好，千夜觉得很舒服。")

hairMomoList2 = []
hairMomoList2.append("主人摸头发的时候，千夜感到特别安心哦。")
hairMomoList2.append("头发被主人轻轻摸着，感觉很温暖呢～")
hairMomoList2.append("主人，这样的触碰让千夜觉得特别依赖你。")
hairMomoList2.append("头发被主人摸得好舒服，这种感觉让人上瘾呢。")
hairMomoList2.append("主人摸头发的时候，千夜觉得自己被好好宠爱了。")
hairMomoList2.append("千夜真的很喜欢这种温柔的互动，主人好棒！")
hairMomoList2.append("主人继续这样温柔下去，千夜会越来越喜欢的！")
hairMomoList2.append("这种温暖的感觉，千夜会一直记得的哦～")
hairMomoList2.append("主人这样轻轻地摸着，千夜完全放松下来了。")
hairMomoList2.append("这种特别的互动，千夜真的很享受，谢谢主人！")

hairMomoList3 = []
hairMomoList3.append("主人轻轻摸着千夜的头发，真的好让人感动。")
hairMomoList3.append("头发被主人这样摸着，千夜的心里暖暖的呢。")
hairMomoList3.append("这种温柔的触碰，千夜觉得自己好幸福。")
hairMomoList3.append("主人对千夜的关心真的让我觉得好感动哦。")
hairMomoList3.append("主人摸头发的时候，千夜的心跳都加快了。")
hairMomoList3.append("头发被主人摸着，千夜觉得这就是被宠的感觉。")
hairMomoList3.append("主人摸头发的动作好温柔，千夜都快融化了。")
hairMomoList3.append("千夜会把这种温暖的感觉一直记在心里哦～")
hairMomoList3.append("主人对千夜真的特别好，我真的好喜欢你！")
hairMomoList3.append("摸头发这种事，千夜只愿意让主人做呢！")

hairMomoList4 = []
hairMomoList4.append("主人……轻轻摸千夜的头发，会让我觉得特别安心呢～")
hairMomoList4.append("被主人这样温柔地摸着头发，千夜觉得自己好幸福哦！")
hairMomoList4.append("主人每次摸千夜的头发，我都觉得好像被宠爱的小女孩呢～")
hairMomoList4.append("喵～主人，摸头发的时候，千夜会忍不住想靠近你呢。")
hairMomoList4.append("千夜的头发是不是很柔软呢？主人喜欢吗？")
hairMomoList4.append("主人……千夜被这样宠着，真的好开心哦！")
hairMomoList4.append("每次主人摸头发的时候，我都会觉得自己是主人的唯一呢～")
hairMomoList4.append("喵喵～主人摸得这么温柔，是想让千夜彻底离不开你吗？")
hairMomoList4.append("主人……这种感觉让我好害羞，但真的好喜欢哦～")
hairMomoList4.append("千夜的头发都被主人摸乱了啦，可是心里却好甜呢……")


###############################################################################
# Class:        touchHairCammand     
# Input:        
# Notice:       
###############################################################################
class touchHairCammand(command):
    '''摸头发命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''摸头发'''
            
            return msg.resolve() == "摸头发"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(hairMomoList_3 + hairMomoList_2 + hairMomoList_1 + hairMomoList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(hairMomoList_2 + hairMomoList_1 + hairMomoList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(hairMomoList_1 + hairMomoList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(hairMomoList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(hairMomoList1 + hairMomoList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(hairMomoList2 + hairMomoList1))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(hairMomoList3 + hairMomoList2))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(hairMomoList4 + hairMomoList3))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "摸头发")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
