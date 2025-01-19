###############################################################################
#   File name:   commandList.py
#   Description: 描述命令集
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from autoBotAPI.shamrockBot.message import callbackmsg, messageSegment

###############################################################################
# Class:        command     
# Input:        
# Notice:       
###############################################################################
class command:
    '''描述千夜姬使用的命令'''
    def __init__(self, isNeedAt: bool, isreply: bool, replyLogic = None, trigerLogic = None, auto_escape = None, \
              recall_duration = None):
        """
        :param isNeedAt: 是否需要AT触发
        :param isreply: 是否需要以回复格式响应
        :param replyLogic: 触发逻辑
        :param trigerLogic: 回复逻辑
        :param auto_escape: 自动撤回
        :param recall_duration: 撤回时间(ms)
        """
        self.isNeedAt = isNeedAt
        self.isreply = isreply
        self.replyLogic = replyLogic
        self.trigerLogic = trigerLogic
        self.auto_escape = auto_escape
        self.recall_duration = recall_duration
        
    ###############################################################################
    # Function:     replyLogicDef
    # Input:        void
    # Notice:       
    ############################################################################### 
    def replyLogicDef(self, replyLogic):
        '''自定义msg回复生成器'''
        self.replyLogic = replyLogic

    ###############################################################################
    # Function:     trrigerLogicDef
    # Input:        void
    # Notice:       
    ############################################################################### 
    def trigerLogicDef(self, trigerLogic):
        '''自定义触发逻辑'''
        self.trigerLogic = trigerLogic

    ###############################################################################
    # Function:     isTrigger
    # Input:        void
    # Notice:       
    ############################################################################### 
    def isTrigger(self, msg: callbackmsg):
        '''判断命令是否触发'''

        # at过滤
        if self.isNeedAt and not msg.isAtme():
            return False
        
        # triggerKey过滤
        elif not self.trigerLogic(msg):
            return False
        
        else:
            return True