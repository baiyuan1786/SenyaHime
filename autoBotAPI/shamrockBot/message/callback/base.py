###############################################################################
#   File name:   base.py
#   Description: shamrock返回消息基类
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..msgSeg.base import messageSegment
from .groupMsg import *
from .privateMsg import *
from .commomMsg import *
from plugin.log import logInfo

MSG_CLSES = [privateMsg_normal, privateMsg_touch, privateMsg_recall, groupMsg_touch, groupMsg_recall, groupMsg_normal]
MSG_CLSES += [lifecycleMsg, responseMsg]
###############################################################################
# Class:        callbackmsg     
# Input:        @qq
# Notice:       当 qq 字段为 "0"或"all" 时, 表示 AT 全体成员
###############################################################################
class callbackmsg:
    '''shamrock返回类型的消息'''
    def __init__(self, receivedData: dict):
        self.receivedData = receivedData
        for cls in MSG_CLSES:
            if cls.isMe(receivedData):
                self.msgEntity = cls(receivedData)
                self.msgName = cls.__name__
                # self.__dict__.update(self.msg.__dict__)
                break
        else:
            raise TypeError(f"[callbackmsg]meet undefined msg, msg is {self.receivedData}")
        
        # 群聊或私聊消息
        self.GorP = "group" if hasattr(self.msgEntity, "group_id") else "private"

    ###############################################################################
    # Function:     __str__
    # Input:        void
    # Notice:       
    ###############################################################################  
    def __str__(self):
        #return f"message_type=\"{self.message_type}\", user_id=\"{self.user_id}\", rawMessage={self.rawMessage}"
        return f"curMsgType is {self.msgName}, the original msg is {self.receivedData}"

    ###############################################################################
    # Function:     isAtme
    # Input:        void
    # Notice:       
    ###############################################################################  
    def isAtme(self):
        '''判断是否是at我'''
        return self.msgEntity.isAtme()
    
    ###############################################################################
    # Function:     resolve
    # Input:        void
    # Notice:       
    ###############################################################################    
    def resolve(self):
        '''从收到的data尝试解析文字信息'''
        return self.msgEntity.resolve()
    
    ###############################################################################
    # Function:     canReply
    # Input:        void
    # Notice:       
    ###############################################################################  
    def canReply(self):
        '''是否可以回复'''
        return hasattr(self.msgEntity, "message_id")