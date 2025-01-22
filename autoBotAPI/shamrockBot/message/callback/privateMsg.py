###############################################################################
#   File name:   privateMsg.py
#   Description: 私聊消息类型
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from plugin.log import logInfo

###############################################################################
# Class:        privateMsg_normal     
# Input:        @qq
# Notice:       
###############################################################################
class privateMsg_normal:
    '''私聊类型的普通消息'''
    needKeys = []
    needKeys += ["time", "self_id", "post_type", "message_type", "sub_type", "message_id"]
    needKeys += ["target_id", "peer_id", "user_id", "message", "raw_message", "font", "sender"]
    needKeys = set(needKeys)
    ###############################################################################
    # Function:     isMe
    # Input:        void
    # Notice:       
    ############################################################################### 
    @classmethod
    def isMe(cls, receivedData: dict):
        '''判断消息是否是此类, 注意必须是friend才算作此类消息'''

        # 判断key是否符合
        if not set(receivedData.keys()) == cls.needKeys:
            return False
        
        # 判断值是否符合
        elif not (receivedData["post_type"] == "message" and
                 receivedData["message_type"] == "private" and
                   receivedData["sub_type"] == "friend"):
            return False
        
        else:
            return True

    def __init__(self, receivedData: dict):
        '''初始化私聊消息普通消息'''
        try:
            self.time = receivedData["time"]
            self.self_id = receivedData["self_id"]
            self.post_type = receivedData["post_type"]
            self.message_type = receivedData["message_type"]
            self.sub_type = receivedData["sub_type"]
            self.message_id = receivedData["message_id"]
            self.target_id = receivedData["target_id"]
            self.peer_id = receivedData["peer_id"]
            self.user_id = receivedData["user_id"]
            self.message = receivedData["message"]
            self.raw_message = receivedData["raw_message"]
            self.font = receivedData["font"]
            self.sender = receivedData["sender"]

        except KeyError as e:
            logInfo(f"[privateMsg_normal]callback message lack key of \"{e}\", the original msg is {receivedData}")

    ###############################################################################
    # Function:     isAtme
    # Input:        void
    # Notice:       
    ###############################################################################    
    def isAtme(self):
        '''判断该消息是否是at我的'''
        # 私聊消息普通必定是at我的
        return True
    
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
# Class:        privateMsg_touch     
# Input:        @qq
# Notice:       
###############################################################################
class privateMsg_touch:
    '''私聊类型的戳戳消息'''
    needKeys = []
    needKeys += ["time", "self_id", "post_type", "notice_type", "sub_type", "operator_id"]
    needKeys += ["user_id", "sender_id", "target_id", "poke_detail"]
    needKeys = set(needKeys)
    ###############################################################################
    # Function:     isMe
    # Input:        void
    # Notice:       
    ############################################################################### 
    @classmethod
    def isMe(cls, receivedData: dict):
        '''判断消息是否是此类, 注意必须是friend才算作此类消息'''

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
        '''初始化私聊消息普通消息'''
        try:
            self.time = receivedData["time"]
            self.self_id = receivedData["self_id"]
            self.post_type = receivedData["post_type"]
            self.notice_type = receivedData["notice_type"]
            self.sub_type = receivedData["sub_type"]
            self.operator_id = receivedData["operator_id"]
            self.user_id = receivedData["user_id"]
            self.sender_id = receivedData["sender_id"]
            self.target_id = receivedData["target_id"]
            self.poke_detail = receivedData["poke_detail"]

        except KeyError as e:
            logInfo(f"[privateMsg_touch]callback message lack key of \"{e}\", the original msg is {receivedData}")

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
# Class:        privateMsg_recall  
# Input:        @qq
# Notice:       
###############################################################################
class privateMsg_recall:
    '''私聊类型的消息撤回消息'''
    needKeys = []
    needKeys += ["time", "self_id", "post_type", "notice_type", "operator_id"]
    needKeys += ["user_id", "message_id"]
    needKeys = set(needKeys)
    ###############################################################################
    # Function:     isMe
    # Input:        void
    # Notice:       
    ############################################################################### 
    @classmethod
    def isMe(cls, receivedData: dict):
        '''判断消息是否是此类, 注意必须是friend才算作此类消息'''

        # 判断key是否符合
        if not set(receivedData.keys()) >= cls.needKeys:
            return False
        
        # 判断值是否符合
        elif not (receivedData["post_type"] == "notice" and
                 receivedData["notice_type"] == "friend_recall"):
            return False
        
        else:
            return True

    def __init__(self, receivedData: dict):
        '''初始化私聊消息普通消息'''
        try:
            self.time = receivedData["time"]
            self.self_id = receivedData["self_id"]
            self.post_type = receivedData["post_type"]
            self.notice_type = receivedData["notice_type"]
            self.operator_id = receivedData["operator_id"]
            self.user_id = receivedData["user_id"]
            # self.message_id = receivedData["message_id"] 无用
            if "tip_text" in receivedData:
                self.tip_text = receivedData["tip_text"]

        except KeyError as e:
            logInfo(f"[privateMsg_recall]callback message lack key of \"{e}\", the original msg is {receivedData}")

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