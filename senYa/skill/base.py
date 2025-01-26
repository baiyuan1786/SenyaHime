###############################################################################
#   File name:   user.py
#   Description: 对于用户数据进行保存
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from typing import Literal
from types import FunctionType
from datetime import datetime
import random, time

from control import GUserInfoDir
from .user.config import userConfig
from .user.history import userRecord, userHistory
from ..physics import message, httpserver, websocketserver
from ..memory.tarot import tarotPool2233
from control import FAVOR_ADD_LEAST, FAVOR_ADD_MAX,\
                    touchReply, touchEarReply, touchBellyReply, touchFaceReply, touchFootReply, \
                    touchHairReply, touchHandReply, touchLegReply, touchSensitiveReply, touchUnknownReply, touchHeadReply

ADD_FAOVR = 10
COMMAND_SHOW_LEN = 5
TOUCH_COMMAND_LEN_MAX = 10

##############################################################
# Class:        skillArgs
# Notice:       
##############################################################
class skillArgs:
    def __init__(self, isNeedAt: bool, isreply: bool, isAt: bool, skillName: str|None, auto_escape: bool|None, recall_duration: int|None):
        """命令参数

        :param isNeedAt: 需要at
        :param isreply: 以回复格式进行
        :param isAt: 以@格式进行
        :param skillName: 命令名称
        :param auto_escape: 自动撤回
        :param recall_duration: 自动撤回时间
        """        
        self.isNeedAt = isNeedAt
        self.isreply = isreply
        self.isAt = isAt
        self.skillName = skillName
        self.auto_escape = auto_escape
        self.recall_duration = recall_duration

defaultArgs = skillArgs(isNeedAt = True, isreply = False, isAt = False, skillName = None, auto_escape = None, recall_duration = None)
##############################################################
# Class:        userInfo
# Notice:       
##############################################################
class userInfo:
    '''规定用户属性'''
    
    ###############################################################################
    # Function:     __init__  
    # Notice:       
    ###############################################################################
    def __init__(self, user_id: int):
        '''初始化用户'''
        self.user_id = user_id
        self.configDir = GUserInfoDir / f"{self.user_id}"

        # 创建目录
        self.configDir.mkdir(parents = False, exist_ok = True)

        # 创建配置和历史
        self.config = userConfig(user_id = user_id)
        self.history = userHistory(user_id = user_id)

        # 创建命令集合
        self.commandList: list[FunctionType] = []
        self.commandList.append(self._drawTarot)
        self.commandList.append(self._touch)
        self.commandList.append(self._hello)
        self.commandList.append(self._test)
        self.commandList.append(self._showFavor)

    ###############################################################################
    # Function:     triggle  
    # Notice:       
    ###############################################################################
    def trigger(self, backMsg: message.callbackmsg, server: httpserver|websocketserver)->tuple[message.messageSegment|None, skillArgs|None]:
        '''尝试触发命令'''
        # 命令解析
        commandText = backMsg.resolve()
        for command in self.commandList:
            try:
                allMsg, args = command(backMsg, server)
                break
            except NameError:
                continue
            #except Exception as e:
            #    allMsg = message.text(text = f"主人, 对\"{type(command).__name__}\"的调用出现未知错误")
            #    args = defaultArgs
            #    break
        else:
            args = defaultArgs
            if args.isNeedAt and not backMsg.isAtme():
                return None, None

            if commandText is None:
                allMsg = message.text(text = f"怎么啦主人, 想千夜了吗, 要和小千夜聊天, 请输入\\开头的命令哦")
            elif commandText.startswith("\\"):
                allMsg = message.text(text = f"呜呜, 对不起主人, 命令\"{commandText}\"还不支持呜喵")
            else:
                allMsg = message.text(text = f"对不起主人, 暂不支持直接聊天哦")

        # 命令统计
        if args.skillName is not None:
            now = datetime.now(); today = now.strftime("%Y%m%d")
            
            # 命令统计初始化
            if args.skillName not in self.config.config["commands"]:
                self.config.config["commands"].append(args.skillName)
                self.config.config["commandUseTimesAll"][args.skillName] = 0
                self.config.config["commandUseTimesAday"][args.skillName] = 0
                self.config.config["commandUseLastDay"][args.skillName] = today
                self.config.config["commandUseLastTimestamp"][args.skillName] = time.time()

            # 命令数据每日刷新
            if self.config.config["commandUseLastDay"][args.skillName] != today:
                self.config.config["commandUseTimesAday"][args.skillName] = 0

            # 命令数据统计
            self.config.config["commandUseTimesAll"][args.skillName] += 1
            self.config.config["commandUseTimesAday"][args.skillName] += 1
            self.config.config["commandUseLastDay"][args.skillName] = today
            self.config.config["commandUseLastTimestamp"][args.skillName] = time.time()

            # 添加历史
            pass

            # 保存配置
            self.config.save()


        # reply和at处理
        if args.isreply and backMsg.replyable() and args.isAt and backMsg.atable():
            allMsg = message.reply(id = backMsg.msgEntity.message_id) + message.at(qq = self.user_id) + allMsg
        elif args.isreply and backMsg.replyable():
            allMsg = message.reply(id = backMsg.msgEntity.message_id) + allMsg
        elif args.isAt and backMsg.atable():
            allMsg = message.at(qq = self.user_id) + allMsg
        
        return allMsg, args

    ###############################################################################
    # Function:     _drawTarot  
    # Notice:       
    ###############################################################################
    def _drawTarot(self, backMsg: message.callbackmsg, server: httpserver|websocketserver)->tuple[message.messageSegment, bool, bool]:
        '''抽取塔罗牌'''

        # 命令属性
        args = skillArgs(isNeedAt = True, isreply = False, isAt = True, skillName = "抽塔罗牌", auto_escape = False, recall_duration = None)

        # 触发逻辑
        if args.isNeedAt and not backMsg.isAtme():
            raise NameError

        commandText = backMsg.resolve()
        if commandText == "\\塔罗牌" or commandText == "\\抽塔罗牌":

            explainMsg, imaMsg, name = tarotPool2233.draw()
            helloMsg = message.text(f"主人酱(/ />/ ▽ /</ /)~ 你抽到了【{name}】哦\n")
            favorMsgAdd = self.config.favorAdd(ADD_FAOVR)
            allMsg = helloMsg + imaMsg + explainMsg + favorMsgAdd

        else:
            raise NameError

        return allMsg, args
    
    ###############################################################################
    # Function:     _touch  
    # Notice:       
    ###############################################################################
    def _touch(self, backMsg: message.callbackmsg, server: httpserver|websocketserver)->tuple[message.messageSegment, bool, bool, str]:
        '''戳戳命令'''
        ###############################################################################
        # Function:     __touchFavorHandle  
        # Notice:       
        ###############################################################################
        def __touchFavorHandle(sensitive: Literal[0, 1, 2], touchReply: dict):
            '''戳戳命令的好感处理'''
            favorStage = self.config.curFavor(key = "stage")

            # 非敏感部位触摸规则
            if sensitive == 0:
                addedFavor = random.randint(FAVOR_ADD_LEAST, FAVOR_ADD_MAX)
                favorMsgAdd = self.config.favorAdd(addedFavor)

            # 敏感部位触摸规则
            elif sensitive == 1:
                addedFavor = random.randint(2 * FAVOR_ADD_LEAST, 2 * FAVOR_ADD_MAX)
                decreaseFavor = random.randint(-5 * FAVOR_ADD_MAX, -5 * FAVOR_ADD_LEAST)
                if favorStage <= 2:
                    favorMsgAdd = self.config.favorAdd(decreaseFavor)
                else:
                    favorMsgAdd = self.config.favorAdd(addedFavor)

            # 禁止部位触摸规则
            else:
                favorMsgAdd = self.config.favorAdd(-1000)

            # 获取回复
            if favorStage == -3:
                favorMsg = message.text(text = random.choice(touchReply["List_3"] + touchReply["List_2"] + touchReply["List_1"] + touchReply["List0"]))
            elif favorStage == -2:
                favorMsg = message.text(text = random.choice(touchReply["List_2"] + touchReply["List_1"] + touchReply["List0"]))
            elif favorStage == -1:
                favorMsg = message.text(text = random.choice(touchReply["List_1"] + touchReply["List0"]))
            elif favorStage == 0:
                favorMsg = message.text(text = random.choice(touchReply["List0"]))
            elif favorStage == 1:
                favorMsg = message.text(text = random.choice(touchReply["List1"] + touchReply["List0"]))
            elif favorStage == 2:
                favorMsg = message.text(text = random.choice(touchReply["List2"] + touchReply["List1"]))
            elif favorStage == 3:
                favorMsg = message.text(text = random.choice(touchReply["List3"] + touchReply["List2"]))
            elif favorStage == 4:
                favorMsg = message.text(text = random.choice(touchReply["List4"] + touchReply["List3"]))
            else:
                favorMsg = message.text(f"好感度异常喵, 当前好感度\"{favorStage}\"不在列表之中")

            # 添加历史记录
            self.history.addRecord(role = "user", msg = commandText)
            self.history.addRecord(role = "bot", msg = favorMsg.data["text"])

            return favorMsg + favorMsgAdd

        # 命令属性
        args = skillArgs(isNeedAt = True, isreply = True, isAt = False, skillName = "触摸", auto_escape = False, recall_duration = None)

        # AT过滤
        if args.isNeedAt and not backMsg.isAtme():
            raise NameError

        commandText = backMsg.resolve()
        
        # 戳戳命令
        if commandText == "\\戳戳":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchReply)
        elif commandText == "摸头发":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchHairReply)
        elif commandText == "摸头":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchHeadReply)
        elif commandText == "摸耳朵":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchEarReply)
        elif commandText == "摸脸":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchFaceReply)
        elif commandText == "摸肚子":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchBellyReply)
        elif commandText == "摸手":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchHandReply)
        elif commandText == "摸腿":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchLegReply)
        elif commandText == "摸脚":
            allMsg = __touchFavorHandle(sensitive = 0, touchReply = touchFootReply)
        elif commandText == "摸胸":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchSensitiveReply)
        elif commandText == "摸小穴":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchSensitiveReply)
        elif commandText == "摸屁股":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchSensitiveReply)
        elif commandText == "摸尾巴":
            allMsg = __touchFavorHandle(sensitive = 1, touchReply = touchSensitiveReply)
        elif commandText is not None and (commandText.startswith("摸") and len(commandText) < TOUCH_COMMAND_LEN_MAX):
            allMsg = message.text(text = random.choice(touchUnknownReply["unknownTouchList"]))
            self.history.addRecord(role = "user", msg = commandText)
            self.history.addRecord(role = "bot", msg = allMsg.data["text"])
        else:
            raise NameError

        return allMsg, args

    ###############################################################################
    # Function:     _showFavor  
    # Notice:       
    ###############################################################################
    def _showFavor(self, backMsg: message.callbackmsg, server: httpserver|websocketserver):
        '''展示当前好感度'''

        # 命令属性
        args = skillArgs(isNeedAt = True, isreply = True, isAt = False, skillName = "查询好感度", auto_escape = False, recall_duration = None)

        # 触发逻辑
        if args.isNeedAt and not backMsg.isAtme():
            raise NameError

        commandText = backMsg.resolve()
        if commandText == "\\好感度" or commandText == "\\查询好感度":
            allMsg = message.text("主人, 您的好感度信息如下哦\n") + self.config.curFavor(key = 'seg')
        else:
            raise NameError

        return allMsg, args

    ###############################################################################
    # Function:     _hello  
    # Notice:       
    ###############################################################################
    def _hello(self, backMsg: message.callbackmsg, server: httpserver|websocketserver):
        '''晚安早安, 午安'''

        # 命令属性
        args = skillArgs(isNeedAt = False, isreply = False, isAt = False, skillName = "安安", auto_escape = False, recall_duration = None)

        # 触发逻辑
        if args.isNeedAt and not backMsg.isAtme():
            raise NameError

        commandText = backMsg.resolve()
        if commandText == "晚安" or commandText == "晚安安":
            allMsg = message.text(text = "晚安主人, 祝您好梦哦")
        else:
            raise NameError

        return allMsg, args
    
    ###############################################################################
    # Function:     _test  
    # Notice:       
    ###############################################################################
    def _test(self, backMsg: message.callbackmsg, server: httpserver|websocketserver):
        '''测试命令'''

        # 命令属性
        args = skillArgs(isNeedAt = True, isreply = False, isAt = True, skillName = "测试", auto_escape = False, recall_duration = None)

        # 触发逻辑
        if args.isNeedAt and not backMsg.isAtme():
            raise NameError

        commandText = backMsg.resolve()
        if commandText == "\\测试" or commandText == "\\test":
            mainMsg1 = message.text("主人, 这是你的测试消息")
            mainMsg2 = message.image(file = r"D:\Tool\Admin\SenyaHime\doc\image\test.png", subType = 1)
            allMsg = mainMsg1 + mainMsg2
        else:
            raise NameError

        return allMsg, args