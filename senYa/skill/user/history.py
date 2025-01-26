###############################################################################
#   File name:   history.py
#   Description: 处理用户记录
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from control import GUserInfoDir
import json, time

##############################################################
# Class:        record
# Notice:       
##############################################################
class userRecord:
    '''对话记录'''
    ###############################################################################
    # Function:     __init__  
    # Notice:       
    ############################################################################### 
    def __init__(self, role: str, msg: str):
        '''初始化一个record'''
        self.timestamp = time.time()
        self.role = role
        self.msg = msg
        self.recordDict = {"timestamp": self.timestamp, 
                            "role": self.role, 
                            "msg": self.msg}

###############################################################################
# Function:     userHistory  
# Notice:       
############################################################################### 
class userHistory:
    '''用户历史'''
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.configDir = GUserInfoDir / f"{self.user_id}"
        self.historyPath = GUserInfoDir / f"{self.user_id}" / f"history.json"

        if not self.configDir.exists():
            raise FileNotFoundError(f"folder not exist\"{self.configDir}\"")
        
        # 历史文件存在时初始化
        if self.historyPath.exists():
            self.history = []
            with self.historyPath.open(mode = "r", encoding="utf-8") as file:
                for line in file:
                    msg = json.loads(line)
                    aRecord = userRecord(msg["role"], msg["msg"])
                    self.history.append(aRecord)

        # 历史文件不存在时初始化
        else:
            self.history = []
    ###############################################################################
    # Function:     addRecord  
    # Notice:       
    ############################################################################### 
    def addRecord(self, role: str, msg: str)->list[userRecord]:
        '''添加记录'''
        aRecord = userRecord(role, msg)

        # 添加进文件
        with self.historyPath.open(mode = "a", encoding = "utf-8") as file:
            json.dump(aRecord.recordDict, file, ensure_ascii = False)
            file.write("\n")
        
        # 添加进历史
        self.history.append(aRecord)