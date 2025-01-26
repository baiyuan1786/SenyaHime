###############################################################################
#   File name:   core.py
#   Description: 千夜姬心智核心
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from control import DEBUG_MODE
from ..memory import logInfo
from ..physics import httpserver, websocketserver, message
from ..skill.base import userInfo, skillArgs
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
        self.users: Dict[int: userInfo] = {}                                     # 当前用户集

    ###############################################################################
    # Function:     resolve  
    # Notice:       
    ###############################################################################
    def resolve(self, backMsg: message.callbackmsg, server: httpserver|websocketserver)->tuple[message.messageSegment | None , skillArgs|None]:
        """解析消息

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
            else:
                user_id = int(backMsg.msgEntity.user_id)
        
            # 新建用户
            if user_id is not None and "user_id" not in self.users:
                self.users[user_id] = userInfo(user_id = user_id)

            # 命令解析
            cmdMsgSeg, cmdArgs = self.users[user_id].trigger(backMsg = backMsg, server = server)


            return cmdMsgSeg, cmdArgs
        except Exception as e:
            logInfo(f"[resolve_debug]error:{str(e)}")
            return None, None