###############################################################################
#   File name:   callback.py
#   Description: shamrock返回类型的消息
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from . import message
from tool.common import logInfo

###############################################################################
# Class:        callbackmsg     
# Input:        @qq
# Notice:       当 qq 字段为 "0"或"all" 时, 表示 AT 全体成员
###############################################################################
class callbackmsg:
    '''shamrock返回类型的消息'''
    def __init__(self, receivedData: dict):
        
        try:
            self.receivedData = receivedData
            self.post_type = receivedData["post_type"]          # 目前观察到分message和notice
            self.time = receivedData["time"]
            self.self_id = int(receivedData["self_id"])
            self.sub_type = receivedData["sub_type"]            # 现在观察到有friend和normal两种类型
            self.user_id = int(receivedData["user_id"])         # 发送者ID
            self.message_id = None

            # 类型判断
            if "group_id" in receivedData:
                self.group_id = int(receivedData["group_id"])
                self.message_type = "group"
            else:
                self.message_type = "private"

            # 消息类型
            if self.post_type == "message":
                self.messages = [message.messageSegment(type = msg["type"], data = msg["data"]) for msg in receivedData["message"]]
                self.rawMessage = receivedData["raw_message"]
                self.peer_id = int(receivedData["peer_id"])
                self.message_id = int(receivedData["message_id"])        # 消息ID

            # 戳一戳消息
            elif self.post_type == "notice":
                self.target_id = int(receivedData["target_id"]) # 目标ID

            else:
                logInfo(f"[callbackmsg]unrecognized post_type\"{self.post_type}\"")


        except KeyError as e:
            logInfo(f"[callbackmsg]callback message lack key of \"{e}\", the original msg is {receivedData}")

    ###############################################################################
    # Function:     __str__
    # Input:        void
    # Notice:       
    ###############################################################################  
    def __str__(self):
        #return f"message_type=\"{self.message_type}\", user_id=\"{self.user_id}\", rawMessage={self.rawMessage}"
        return f"the original msg is {self.receivedData}"

    ###############################################################################
    # Function:     isAtme
    # Input:        void
    # Notice:       
    ###############################################################################    
    def isAtme(self):
        '''判断该消息是否是at我的'''

        # 群聊消息
        if self.post_type == "message" and self.message_type == "group":
            for msg in self.messages:
                if msg.type == "at" and int(msg.data["qq"]) == self.self_id:
                    return True
        
        # 戳一戳消息
        elif self.post_type == "notice":
            if self.target_id == self.self_id:
                return  True

        # 私聊消息
        elif self.message_type == "private":
            return True

        else:
            return False
    
    ###############################################################################
    # Function:     resolve
    # Input:        void
    # Notice:       
    ###############################################################################    
    def resolve(self):
        '''从收到的data尝试解析文字信息'''

        if not self.isAtme():
            return None

        try:
            # 消息类型
            if self.post_type == "message":
                for message in self.messages:
                    if message.type == "text":
                        commandText = message.data["text"].strip()
                        break

            # 戳一戳类型
            elif self.post_type == "notice":
                commandText = "戳戳"

            # 其他类型
            else:
                commandText = None
        finally:
            if bool(commandText):
                return commandText
            else:
                return None