###############################################################################
#   File name:   groupMsg.py
#   Description: shamrock返回消息基类
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ....memory.log import logInfo

###############################################################################
# Class:        privateMsg_normal     
# Input:        @qq
# Notice:       
###############################################################################
class groupMsg_normal:
    '''群聊类型的普通消息'''
    needKeys = []
    needKeys += ["time", "self_id", "post_type", "message_type", "sub_type", "message_id"]
    needKeys += ["group_id", "peer_id", "user_id", "message", "raw_message", "font", "sender"]
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
        elif not (receivedData["post_type"] == "message" and
                 receivedData["message_type"] == "group" and
                   receivedData["sub_type"] == "normal"):
            return False
        
        else:
            return True

    def __init__(self, receivedData: dict):
        '''初始化群聊类型的普通消息'''
        try:
            self.time = receivedData["time"]
            self.self_id = receivedData["self_id"]
            self.post_type = receivedData["post_type"]
            self.message_type = receivedData["message_type"]
            self.sub_type = receivedData["sub_type"]
            self.message_id = receivedData["message_id"]
            self.group_id = receivedData["group_id"]
            self.peer_id = receivedData["peer_id"]
            self.user_id = receivedData["user_id"]
            self.message = receivedData["message"]
            self.raw_message = receivedData["raw_message"]
            self.font = receivedData["font"]
            self.sender = receivedData["sender"]

        except KeyError as e:
            logInfo(f"[groupMsg_normal]callback message lack key of \"{e}\", the original msg is {receivedData}")

    ###############################################################################
    # Function:     isAtme
    # Input:        void
    # Notice:       
    ###############################################################################    
    def isAtme(self):
        '''判断该消息是否是at我的'''
        for msg in self.message:
            if msg["type"] == "at" and int(msg["data"]["qq"]) == self.self_id:
                return True
        else:
            return False

    ###############################################################################
    # Function:     resolve
    # Input:        void
    # Notice:       
    ###############################################################################     
    def resolve(self):
        '''尝试从message解析命令'''
        for message in self.message:
            if message["type"] == "text":
                commandText = message["data"]["text"].strip()
                if bool(commandText):
                    return commandText
                else: 
                    continue
        return None
        
###############################################################################
# Class:        groupMsg_touch     
# Input:        @qq
# Notice:       
###############################################################################
class groupMsg_touch:
    '''群聊类型的戳戳消息'''
    needKeys = []
    needKeys += ["time", "self_id", "post_type", "notice_type", "sub_type", "operator_id"]
    needKeys += ["group_id", "operator_id", "user_id", "target_id", "poke_detail"]
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
        elif not (receivedData["post_type"] == "notice" and
                 receivedData["notice_type"] == "notify" and
                   receivedData["sub_type"] == "poke"):
            return False
        
        else:
            return True

    def __init__(self, receivedData: dict):
        '''初始化群聊类型的戳戳消息'''
        try:
            self.time = receivedData["time"]
            self.self_id = receivedData["self_id"]
            self.post_type = receivedData["post_type"]
            self.notice_type = receivedData["notice_type"]
            self.sub_type = receivedData["sub_type"]
            self.operator_id = receivedData["operator_id"]
            self.group_id = receivedData["group_id"]
            self.operator_id = receivedData["operator_id"]
            self.user_id = receivedData["user_id"]
            self.target_id = receivedData["target_id"]
            self.poke_detail = receivedData["poke_detail"]

        except KeyError as e:
            logInfo(f"[groupMsg_touch]callback message lack key of \"{e}\", the original msg is {receivedData}")

    ###############################################################################
    # Function:     isAtme
    # Input:        void
    # Notice:       
    ###############################################################################    
    def isAtme(self):
        '''判断该消息是否是at我的'''
        return self.target_id == self.self_id
    
    ###############################################################################
    # Function:     resolve
    # Input:        void
    # Notice:       
    ###############################################################################     
    def resolve(self):
        '''尝试从message解析命令'''
        return "\戳戳"
    
###############################################################################
# Class:        groupMsg_recall  
# Input:        @qq
# Notice:       
###############################################################################
class groupMsg_recall:
    '''群聊类型的消息撤回消息'''
    needKeys = []
    needKeys += ["time", "self_id", "post_type", "notice_type"]
    needKeys += ["group_id", "operator_id", "user_id", "message_id"]
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
        if not set(receivedData.keys()) >= cls.needKeys:
            return False
        
        # 判断值是否符合
        elif not (receivedData["post_type"] == "notice" and
                 receivedData["notice_type"] == "group_recall"):
            return False
        
        else:
            return True

    def __init__(self, receivedData: dict):
        '''初始化群聊类型的消息撤回消息'''
        try:
            self.time = receivedData["time"]
            self.self_id = receivedData["self_id"]
            self.post_type = receivedData["post_type"]
            self.notice_type = receivedData["notice_type"]
            self.group_id = receivedData["group_id"]
            self.operator_id = receivedData["operator_id"]
            self.user_id = receivedData["user_id"]
            # self.message_id = receivedData["message_id"] 无用
            if "tip_text" in receivedData:
                self.tip_text = receivedData["tip_text"]

        except KeyError as e:
            logInfo(f"[groupMsg_recall]callback message lack key of \"{e}\", the original msg is {receivedData}")

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
        return "撤回了消息"