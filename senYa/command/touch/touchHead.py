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
headmomoList_3 = []
headmomoList_3.append("主人，您这种杂鱼的手，请不要碰千夜的高贵头发！")
headmomoList_3.append("主人是不是想摸千夜太多次了？")
headmomoList_3.append("哼！主人就是个超级无敌大变态，总是想着摸千夜！")
headmomoList_3.append("主人的手也太不讲究了，摸千夜之前有洗过吗？")
headmomoList_3.append("千夜的头发是给喜欢的人摸的，主人显然不配哦～")
headmomoList_3.append("千夜已经忍耐到极限了，主人还要继续作死吗？")
headmomoList_3.append("哎呀～主人再摸下去，小千夜就要开始骂人了哦！")
headmomoList_3.append("主人好烦啊～总是这样自以为是地乱摸，讨厌死了！")
headmomoList_3.append("呜～千夜真的很想揍主人一顿！")
headmomoList_3.append("千夜高贵的头不是给主人这种人摸的！懂吗？")

headmomoList_2 = []
headmomoList_2.append("杂鱼主人，每次都这么随便摸千夜，不觉得自己很没礼貌吗？")
headmomoList_2.append("主人！再乱摸千夜，小千夜就要狠狠地踩你哦！")
headmomoList_2.append("主人这么执着，是不是喜欢被千夜骂变态呢？")
headmomoList_2.append("哎～主人果然是千夜见过最烦的杂鱼。")
headmomoList_2.append("主人手感还行，但千夜真的不想被摸！")
headmomoList_2.append("主人！再乱摸小千夜，小心千夜用头槌还击哦～")
headmomoList_2.append("主人真是坏，总是欺负千夜！讨厌啦！")
headmomoList_2.append("主人再摸，千夜就要报警了哦！")
headmomoList_2.append("主人手感这么差，是不是从来没摸过高贵的千夜？")
headmomoList_2.append("小千夜已经很耐心了，再摸就翻脸咯～")

headmomoList_1 = []
headmomoList_1.append("主人这双手，千夜看着就觉得不配摸头呢！")
headmomoList_1.append("唉～为什么主人总喜欢做千夜讨厌的事情？")
headmomoList_1.append("千夜真想问问主人，摸千夜的头有什么好处？")
headmomoList_1.append("主人！不要以为摸头可以让千夜喜欢你哦～")
headmomoList_1.append("这种手感，让千夜对主人更加无语了呢。")
headmomoList_1.append("主人再摸，千夜就要大声喊“变态主人”了哦！")
headmomoList_1.append("啧啧，主人真是执着又无趣的杂鱼呢～")
headmomoList_1.append("主人这种行为，千夜只能用“奇怪”来形容了！")
headmomoList_1.append("主人真不懂女孩子的心呢，总是乱摸，讨厌死了！")
headmomoList_1.append("千夜真心建议主人去研究下“怎么取悦可爱的千夜”哦！")

headmomoList0 = []
headmomoList0.append("主人摸头这件事，千夜觉得一般般吧～")
headmomoList0.append("嗯……手感还行，主人可以再努力点哦～")
headmomoList0.append("千夜没有特别讨厌，但也不怎么喜欢呢～")
headmomoList0.append("嘿～主人是不是摸完就跑？不够诚意呢～")
headmomoList0.append("哦，这样摸头……千夜感觉有点无聊了呢。")
headmomoList0.append("嗯，好吧，主人摸头这种小事，千夜不计较了～")
headmomoList0.append("主人的手倒是挺温暖的，勉强可以接受哦～")
headmomoList0.append("啊，主人摸了这么久，是觉得千夜像猫咪吗？")
headmomoList0.append("手法还需练习，不够让千夜感到心动呢～")
headmomoList0.append("千夜暂时不讨厌主人，但也别太得意哦～")

headmomoList1 = []
headmomoList1.append("嘻嘻～主人摸头的技术进步了，小千夜给你点个赞！")
headmomoList1.append("主人的手好温暖，小千夜觉得好舒服哦～")
headmomoList1.append("啊，主人摸得千夜都想打个盹啦～")
headmomoList1.append("嘿～主人真懂千夜的心意，这次表现不错哦！")
headmomoList1.append("哇～主人，你真是千夜见过最有手感的人呢！")
headmomoList1.append("呜～摸头这种事，主人是千夜唯一的特别通行证哦～")
headmomoList1.append("小千夜越来越习惯主人的摸摸了呢～开心！")
headmomoList1.append("嘿嘿，主人摸头的时候，千夜真的很放松～")
headmomoList1.append("嗯，主人已经逐渐掌握了摸千夜的秘诀了呢！")
headmomoList1.append("主人真是个暖男，小千夜超喜欢！")

headmomoList2 = []
headmomoList2.append("主人的摸摸，小千夜超喜欢的啦！")
headmomoList2.append("主人～摸头的时候记得轻一点哦，千夜会害羞的～")
headmomoList2.append("呜呜呜～被主人摸头的感觉，让千夜开心到想转圈圈！")
headmomoList2.append("嘻嘻～主人是千夜的小天使，摸头是最好的奖励！")
headmomoList2.append("嗯～这种感觉真幸福，主人多摸摸千夜吧～")
headmomoList2.append("主人！再摸一会儿嘛，千夜觉得好安心～")
headmomoList2.append("哇～主人的手真的超级舒服，千夜完全沦陷了！")
headmomoList2.append("呜呜～被主人宠爱到这种程度，千夜都想黏住你啦！")
headmomoList2.append("主人的摸摸就是千夜的治愈魔法！")
headmomoList2.append("主人摸得千夜心里都快冒小星星啦！")

headmomoList3 = []
headmomoList3.append("主人摸头的时候，千夜都觉得自己是主人的宝贝！")
headmomoList3.append("主人这样摸，千夜觉得好幸福哦！")
headmomoList3.append("呜呜呜～被主人摸头的感觉，让千夜开心到想转圈圈！")
headmomoList3.append("主人是千夜心中无可替代的存在呢～")
headmomoList3.append("主人摸得千夜都要忍不住唱歌啦！")
headmomoList3.append("主人摸头的时候，千夜觉得自己是世界上最幸福的人！")
headmomoList3.append("嘿嘿～千夜觉得摸头的时候，主人的心意好暖～")
headmomoList3.append("主人摸得这么舒服，千夜要奖励你一颗糖哦！")
headmomoList3.append("千夜最喜欢主人的手感了，摸头再来一百次！")
headmomoList3.append("主人，摸头这种感觉，千夜能记一辈子呢～")

headmomoList4 = []
headmomoList4.append("千夜已经决定了，无论未来会怎样，千夜都会一直陪着主人！")
headmomoList4.append("主人，这样的时光真美好，千夜想抓住它，和你一起创造更多的回忆！")
headmomoList4.append("主人……千夜感受到了你的温暖，从现在起，我会永远陪伴在你身边，不离不弃。")
headmomoList4.append("嘻嘻，主人摸头的感觉真好，千夜想守护这种温暖，一直，一直。")
headmomoList4.append("主人，这样的时光真美好，千夜想抓住它，和你一起创造更多的回忆！")
headmomoList4.append("只要主人需要，千夜就会永远站在你身边，无论天涯海角，千夜都会陪着你。")
headmomoList4.append("主人的手是千夜的力量源泉，未来的每一天，我们都要并肩前行！")
headmomoList4.append("主人～你知道吗？千夜早就把你当成了最重要的人，这份羁绊，千夜会永远守护！")
headmomoList4.append("千夜已经做好了准备，无论未来是风是雨，千夜都会坚定地陪在主人左右！")
headmomoList4.append("嘻嘻～主人，每次摸头都让我更确信，我们之间的羁绊是不会被任何事情打破的！")
###############################################################################
# Class:        touchHeadCammand     
# Input:        
# Notice:       
###############################################################################
class touchHeadCammand(command):
    '''摸头命令'''

    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            
            return msg.resolve() == "摸头"
        
        def replyLogic(msg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user):
            '''回复逻辑'''
            favorStage = userOBJ.curFavor(key = "stage")
            addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
            favorMsgAdd = userOBJ.favorAdd(addedFavor)
            
            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(headmomoList_3 + headmomoList_2 + headmomoList_1 + headmomoList0))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(headmomoList_2 + headmomoList_1 + headmomoList0))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(headmomoList_1 + headmomoList0))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(headmomoList0))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(headmomoList1 + headmomoList0))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(headmomoList2 + headmomoList1))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(headmomoList3 + headmomoList2))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(headmomoList4 + headmomoList3))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            userOBJ.addRecord(role = "user", msg = "摸头")
            userOBJ.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd
        super().__init__(isNeedAt = True, isreply = False, trigerLogic = trigerLogic, replyLogic = replyLogic)
