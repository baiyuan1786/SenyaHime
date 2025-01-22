###############################################################################
#   File name:   user.py
#   Description: 对于用户数据进行保存
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from path import GUserInfoDir
from typing import Literal
from .config import userConfig
from .history import userRecord, userHistory
from autoBotAPI.shamrockBot import message

##############################################################
# Class:        user
# Input:        void
# Notice:       
##############################################################
class user:
    '''规定用户属性'''
    def __init__(self, user_id: int):
        '''使用user_id初始化即可'''
        self.user_id = user_id
        self.configDir = GUserInfoDir / f"{self.user_id}"

        # 创建目录
        self.configDir.mkdir(parents = False, exist_ok = True)

        # 创建配置和历史
        self.config = userConfig(user_id = user_id)
        self.history = userHistory(user_id = user_id)

    ###############################################################################
    # Function:     save  
    # Notice:       
    ###############################################################################
    def save(self):
        '''存储用户信息'''
        self.config.save()

    ###############################################################################
    # Function:     addRecord  
    # Notice:       
    ############################################################################### 
    def addRecord(self, role: str, msg: str):
        '''添加记录'''
        self.history.addRecord(role, msg)

    ###############################################################################
    # Function:     favorAdd  
    # Notice:       
    ############################################################################### 
    def favorAdd(self, addValue: int):
        '''增加好感度'''
        return self.config.favorAdd(addValue)

    ###############################################################################
    # Function:     curFavor  
    # Notice:       
    ############################################################################### 
    def curFavor(self, key: Literal["stage", "stageName", "stageStr", "favorability", "seg"]):
        '''获取当前好感度信息'''
        if key == "stage":
            return self.config.config["favorStage"]
        elif key == "stageName":
            return self.config.config["favorStageName"]
        elif key == "stageStr":
            return self.config.config["favorStageStr"]
        elif key == "favorability":
            return self.config.config["favorability"]
        elif key == "seg":
            return message.text(f"Current Favor:{self.config.config["favorability"]}, {self.config.config["favorStageStr"]}")
        else:
            raise ValueError(f"[curFavor]unsupported key \'{key}\'")





