###############################################################################
#   File name:   commandList.py
#   Description: 描述命令集
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from autoBotAPI.shamrockBot import message
from autoBotAPI.shamrockBot import httpserver, websocketserver
from types import FunctionType
from ..user import user
###############################################################################
# Class:        commandArgs        
# Notice:       
###############################################################################
class commandArgs:
    '''命令参数'''
    def __init__(self, isNeedAt: bool, isreply: bool, auto_escape: bool|None = None, recall_duration: int|None = None):
        self.isNeedAt = isNeedAt
        self.isreply = isreply
        self.auto_escape = auto_escape
        self.recall_duration = recall_duration

###############################################################################
# Class:        command          
# Notice:       
###############################################################################
class command(commandArgs):
    '''描述千夜姬使用的命令'''
    def __init__(self, isNeedAt: bool, isreply: bool, auto_escape: bool|None = None, \
              recall_duration: int|None = None, replyLogic = None, trigerLogic = None):
        """ 千夜姬命令
        :param isNeedAt: 是否需要AT触发
        :param isreply: 是否需要以回复格式响应
        :param replyLogic: 触发逻辑
        :param trigerLogic: 回复逻辑
        :param auto_escape: 自动撤回
        :param recall_duration: 撤回时间(ms)
        """
        super().__init__(isNeedAt, isreply, auto_escape, recall_duration)
        self.replyLogic = replyLogic    # 回复逻辑, 必须支持msg和server输入
        self.trigerLogic = trigerLogic  # 触发逻辑, 必须支持msg输入

    ###############################################################################
    # Function:     isTrigger
    # Input:        void
    # Notice:       
    ############################################################################### 
    def isTrigger(self, backMsg: message.callbackmsg):
        '''判断命令是否触发'''

        # at过滤
        if self.isNeedAt and not backMsg.isAtme():
            return False
        
        # triggerKey过滤
        elif not self.trigerLogic(backMsg):
            return False
        
        else:
            return True

    ###############################################################################
    # Function:     trigger
    # Input:        void
    # Notice:       
    ###############################################################################     
    def trigger(self, backMsg: message.callbackmsg, server: httpserver|websocketserver, userOBJ: user)->message.messageSegment|None:
        '''触发命令'''
        if not isinstance(self.replyLogic, FunctionType):
            raise TypeError("replyLogic not defined")
        if self.isTrigger(backMsg):
            return self.replyLogic(backMsg, server, userOBJ)
        else:
            return None