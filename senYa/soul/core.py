###############################################################################
#   File name:   core.py
#   Description: 千夜姬心智核心
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from control import DEBUG_MODE
from ..memory import logInfo
from ..physics import httpserver, websocketserver, message
from ..memory.user import userInfo
from ..skill import *
from typing import Dict
##############################################################
# Class:        mentalCore
# Notice:       
##############################################################
class mentalCore:
    '''千夜姬心智核心'''
    ###############################################################################
    # Function:     __init__
    # Notice:       
    ###############################################################################
    def __init__(self):
        '''初始化千夜姬心智核心'''
        # 当前用户集
        self.users: Dict[int: userInfo] = {}

        # 当前命令集       
        self.commandList: list[TriggerFunction] = []
        self.commandList.append(ShowFavor())
        self.commandList.append(GreetingMor())
        self.commandList.append(GreetingNoon())
        self.commandList.append(GreetingNight())
        self.commandList.append(DrawTarot())
        self.commandList.append(Touch())
        self.commandList.append(Test())

    ###############################################################################
    # Function:     resolve  
    # Notice:       
    ###############################################################################
    def resolve(self, backMsg: message.callbackmsg, server: httpserver|websocketserver)->tuple[message.messageSegment | None , TriggerFunction|None]:
        """解析消息

        :param backMsg: 返回类型消息
        :param server: 服务器类, 某些命令可能需要接口获取客户端数据
        """
        try:
            cmdMsgSeg = None    # 命令解析消息
            cmd = None          # 命令信息
            user_id = None      # 用户ID
        
            # 用户解析
            if not hasattr(backMsg.msgEntity, "user_id"):
                return cmdMsgSeg, cmd
            else:
                user_id = int(backMsg.msgEntity.user_id)
        
            # 新建用户
            if user_id is not None and user_id not in self.users:
                self.users[user_id] = userInfo(user_id = user_id)

            # 命令解析
            commandText = backMsg.resolve()
            for command in self.commandList:
                try:
                    cmdMsgSeg = command.execute(self.users[user_id], server, backMsg)
                    cmd = command
                    break
                except NameError:
                    continue
                except Exception as e:
                    cmdMsgSeg = message.text(text = f"主人, 对\"{command.skillName}\"的调用出现未知错误")
                    cmd = command
                    logInfo(f"[resolve_debug]error for \"{command.skillName}\": {str(e)}")
                    break
            else:
                if commandText is None:
                    cmdMsgSeg = message.text(text = f"怎么啦主人, 想千夜了吗, 要和小千夜聊天, 请输入\\开头的命令哦")
                elif commandText.startswith("\\"):
                    cmdMsgSeg = message.text(text = f"呜呜, 对不起主人, 命令\"{commandText}\"还不支持呜喵")
                else:
                    cmd = dialogue()
                    cmdMsgSeg = cmd.execute(self.users[user_id], server, backMsg)

            return cmdMsgSeg, cmd
        except Exception as e:
            logInfo(f"[resolve_debug]error:{str(e)}")
            return None, None