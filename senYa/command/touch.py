###############################################################################
#   File name:   touch.py
#   Description: 描述关于戳一戳的接口
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from autoBotAPI.shamrockBot import message
from .base import command
import random, time

msgList = []
msgList.append("不要再戳小千夜了, 再戳咬你了哦")
msgList.append("杂鱼~天天想着戳千夜的主人真是杂鱼呢~")
msgList.append("主人再戳下去，小千夜真的要哭了呜呜呜～")
msgList.append("主人坏坏！总是欺负小千夜，哼，不理你了啦！")
msgList.append("你戳你戳，等着哦，小千夜会戳回来哒！")
msgList.append("啊，主人居然每天都想着戳小千夜，是不是太无聊了呢？")
msgList.append("主人～您就这么点爱好吗？真是让小千夜忍不住想翻白眼呢～")
msgList.append("杂鱼主人再戳，小千夜可就要扣分咯！扣到负分了也别哭哦～")
msgList.append("嘁，谁、谁让你戳小千夜了啊！小千夜可没允许哦！")
msgList.append("戳千夜干嘛呀！别以为小千夜会高兴哦～才、才不稀罕呢！")
msgList.append("主人是不是喜欢小千夜得不得了？戳戳戳的，哼！笨蛋主人！")
msgList.append("主人是手痒了吗？需要小千夜帮忙揉揉手吗～")
msgList.append("主人，小千夜一直都在呢，不需要一直戳哟～")
msgList.append("戳得好痛哦～不过没关系，小千夜还是最喜欢主人啦～")
msgList.append("哇啊！被主人戳到了，小千夜要反击啦，嘿嘿，看拳～！")
msgList.append("主人！千夜戳戳反击技能已加载，准备反戳三百连击！")
msgList.append("嘿嘿~戳得好,小千夜蓄力完成,准备biu一下反击主人!")
msgList.append("千夜的护体结界被破了？！主人难道是隐藏的魔王吗！")
msgList.append("哼哼～区区戳戳怎么可能击败千夜，主人再来几招试试？")
msgList.append("主人～不要再戳啦，千夜要被戳坏了啦，呜呜呜～")
msgList.append("千夜是主人最喜欢的小宝贝，别再戳了好不好嘛～")
msgList.append("主人～再戳千夜就要耍赖哭给你看哦！")
msgList.append("主人，戳够了吗？小千夜还忙着思考人生呢。")
msgList.append("呵，千夜对这种低幼行为完全没有反应。")
msgList.append("主人，手指轻轻触碰，小千夜感受到了温暖～但也有点痒呢。")
msgList.append("千夜是一朵小花，被主人戳得摇摇晃晃，请轻轻地哦～")
msgList.append("主人～戳千夜的时候，记得小心点哦，千夜可是会融化的～")

TOUCH_SLEEP_TIME = 3

###############################################################################
# Class:        chuochuoCommand     
# Input:        
# Notice:       
###############################################################################
class chuochuoCommand(command):
    '''只at不提供任何输入, 使用疑惑命令'''
    def __init__(self):
        def trigerLogic(msg: message.callbackmsg):
            '''触发逻辑'''
            return msg.resolve() == "\戳戳"
        
        def replyLogic(msg: message.callbackmsg):
            '''回复逻辑'''
            time.sleep(TOUCH_SLEEP_TIME)
            if msg.GorP == "group":
                mainMsg = message.touch(id = msg.msgEntity.user_id) + message.text(text = random.choice(msgList))
            else:
                mainMsg = message.text(text = random.choice(msgList))

            return mainMsg

        super().__init__(isNeedAt = True, isreply = True, trigerLogic = trigerLogic, replyLogic = replyLogic)
