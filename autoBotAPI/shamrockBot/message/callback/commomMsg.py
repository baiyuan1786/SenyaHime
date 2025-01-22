###############################################################################
#   File name:   commmomMsg.py
#   Description: 常规消息
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from plugin.log import logInfo


###############################################################################
# Class:        lifecycleMsg     
# Input:        @qq
# Notice:       
###############################################################################
class lifecycleMsg:
    '''连接类型的消息'''
    needKeys = []
    needKeys += ["time", "self_id", "post_type", "meta_event_type", "sub_type", "status"]
    needKeys += ["interval"]
    needKeys = set(needKeys)
    ###############################################################################
    # Function:     isMe
    # Input:        void
    # Notice:       
    ############################################################################### 
    @classmethod
    def isMe(cls, receivedData: dict):
        '''判断消息是否是此类'''

        # 判断key是否符合
        if not set(receivedData.keys()) == cls.needKeys:
            return False
        
        # 判断值是否符合
        elif not (receivedData["post_type"] == "meta_event"):
            return False
        
        else:
            return True

    def __init__(self, receivedData: dict):
        '''初始化群聊类型的普通消息'''
        try:
            self.time = receivedData["time"]
            self.self_id = receivedData["self_id"]
            self.post_type = receivedData["post_type"]
            self.meta_event_type = receivedData["meta_event_type"]
            self.sub_type = receivedData["sub_type"]
            self.status = receivedData["status"]
            self.interval = receivedData["interval"]

        except KeyError as e:
            logInfo(f"[lifecycleMsg]callback message lack key of \"{e}\", the original msg is {receivedData}")

    ###############################################################################
    # Function:     isAtme
    # Input:        void
    # Notice:       
    ###############################################################################    
    def isAtme(self):
        '''判断该消息是否是at我的'''
        return False

    ###############################################################################
    # Function:     resolve
    # Input:        void
    # Notice:       
    ###############################################################################     
    def resolve(self):
        '''尝试从message解析命令'''
        return None
    
###############################################################################
# Class:        responseMsg     
# Input:        @qq
# Notice:       
###############################################################################
class responseMsg:
    '''回复类型的消息'''
    needKeys = []
    needKeys += ["status", "retcode", "data", "echo"]
    needKeys = set(needKeys)
    ###############################################################################
    # Function:     isMe
    # Input:        void
    # Notice:       
    ############################################################################### 
    @classmethod
    def isMe(cls, receivedData: dict):
        '''判断消息是否是此类'''

        # 判断key是否符合
        if not set(receivedData.keys()) == cls.needKeys:
            return False

        else:
            return True

    def __init__(self, receivedData: dict):
        '''初始化群聊类型的普通消息'''
        try:
            self.status = receivedData["status"]
            self.retcode = receivedData["retcode"]
            self.data = receivedData["data"]
            self.echo = receivedData["echo"]

        except KeyError as e:
            logInfo(f"[lifecycleMsg]callback message lack key of \"{e}\", the original msg is {receivedData}")

    ###############################################################################
    # Function:     isAtme
    # Input:        void
    # Notice:       
    ###############################################################################    
    def isAtme(self):
        '''判断该消息是否是at我的'''
        return False

    ###############################################################################
    # Function:     resolve
    # Input:        void
    # Notice:       
    ###############################################################################     
    def resolve(self):
        '''尝试从message解析命令'''
        return None