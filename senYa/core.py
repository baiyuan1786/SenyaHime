###############################################################################
#   File name:   core.py
#   Description: 千夜姬心智核心
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .command.base import command
from .command.card import *
from .command.excepts import *
from .command.touch.touch import *
from .command.hello import *
from .command.test import *
from .command.touch import *
from .command.favor import *
import schedule, threading
from .user import user
from control import DEBUG_MODE
from plugin.log import logInfo
from autoBotAPI.shamrockBot import httpserver, websocketserver, message
##############################################################
# Class:        mentalCore
# Notice:       
##############################################################
class mentalCore:
    '''千夜姬心智核心'''
    def __init__(self):
        '''初始化千夜姬心智核心'''
        self.commandMenu = []
        self.commandMenu.append(testCommand())              # 测试命令
        self.commandMenu.append(drawCardCommand())          # 抽卡命令
        self.commandMenu.append(reInitCardPoolCommand())    # 重置卡池
        self.commandMenu.append(stateInfoCommand())         # 卡池状态
        self.commandMenu.append(showFavor())                # 查询好感度

        # 全套摸摸命令
        self.commandMenu.append(touchCammand())             # 戳戳
        self.commandMenu.append(touchBellyCammand())        # 摸摸肚子
        self.commandMenu.append(touchEarCammand())          # 摸摸耳朵
        self.commandMenu.append(touchFootCammand())         # 摸摸脚
        self.commandMenu.append(touchHairCammand())         # 摸摸头发
        self.commandMenu.append(touchHandCammand())         # 摸摸手
        self.commandMenu.append(touchHeadCammand())         # 摸摸头
        self.commandMenu.append(touchLegCammand())          # 摸摸脚
        self.commandMenu.append(touchFaceCammand())         # 摸摸脸
        self.commandMenu.append(touchSensitiveCammand())      # 敏感触摸
        self.commandMenu.append(touchUnknownCammand())      # 未知触摸
        self.commandMenu.append(wananCommand())             # 晚安

        # 错误处理命令
        self.commandMenu.append(sorryCommand())             # 不能解释的命令 / 这个命令必须放在最后
        self.commandMenu.append(confuseCommand())           # 只at不输入 / 这个命令必须放在最后
        self.users = {}                                     # 当前用户集

    ###############################################################################
    # Function:     resolve  
    # Notice:       
    ###############################################################################
    def resolve(self, backMsg: message.callbackmsg, server: httpserver|websocketserver)->tuple[message.messageSegment | None , command|None]:
        """通过心智核心获取响应

        :param backMsg: 返回类型消息
        :param server: 服务器类, 某些命令可能需要接口获取客户端数据
        """
        try:
            cmdMsgSeg = None   # 命令解析消息
            cmdSovled = None      # 命令
            user_id = None      # 用户ID
        
            # 用户解析
            if not hasattr(backMsg.msgEntity, "user_id"):
                return cmdMsgSeg, cmdSovled
            user_id = int(backMsg.msgEntity.user_id)

            if DEBUG_MODE:
                logInfo(f"[resolve_debug]cur user is \"{user_id}\"")
        
            if user_id is not None and "user_id" not in self.users:
                self.users[user_id] = user(user_id = user_id)

            if DEBUG_MODE:
                logInfo(f"[resolve_debug]user_id 存在于用户集中为 \"{user_id in self.users}\"")

            # 命令解析
            for cmd in self.commandMenu:
                cmdMsgSeg = cmd.trigger(backMsg = backMsg, server = server, userOBJ = self.users[user_id])
                cmdSovled = cmd
                if isinstance(cmdMsgSeg, message.messageSegment):
                    if DEBUG_MODE:
                        logInfo(f"[resolve_debug]cmd \"{type(cmd).__name__}\" triggered\n")
                    break

            return cmdMsgSeg, cmdSovled
        except Exception as e:
            logInfo(f"[resolve_debug]error:{str(e)}")
            return None, None