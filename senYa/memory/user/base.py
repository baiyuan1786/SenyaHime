###############################################################################
#   File name:   user.py
#   Description: 对于用户数据进行保存
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from typing import Literal
from datetime import datetime
import random, time, json
import numpy as np
from control import json2dict, GRoot, GUserInfoDir
from ...physics import message

COMMAND_SHOW_LEN = 5
FAVOR_GREAT_DISTASTE = -10000
FAVOR_DISTASTE = -1000
FAVOR_DISGUSTING = 0
FAVOR_NORMAL = 100
FAVOR_FAMILIARIZE = 700
FAVOR_INTIMATE = 1500
FAVOR_LOVE = 3000
FAVOR_HALF_DECAY = 100                           # 好感增长半衰
FAVOR_ADD_MAX_ADAY = 500                         # 一天允许增加好感度上限
FAVOR_DEADD_MAX_ADAY = 500                       # 一天允许减少好感度上限
############################################################################################################################
# Class:        userRecord
# Notice:       对话记录, 记录一条对话的角色, 时间戳和消息属性
############################################################################################################################
class userRecord:
    '''对话记录'''
    ###############################################################################
    # Function:     __init__  
    # Notice:       
    ############################################################################### 
    def __init__(self, role: Literal["assistant", "user"], content: str, timestamp = None):
        '''初始化一个record'''
        if timestamp is None:
            self.timestamp = time.time()
            
        else:
            self.timestamp = timestamp
        self.role = role
        self.content = content

    ###############################################################################
    # Function:     toDict  
    # Notice:       
    ###############################################################################     
    def toDict(self, neadTime: bool = True):
        '''转换为字典格式'''
        if neadTime:
            return {"timestamp": self.timestamp, 
                    "role": self.role, 
                    "content": self.content}
        else:
            return {"role": self.role, 
                    "content": self.content}

############################################################################################################################
# Class:        userInfo
# Notice:       规定用户属性, 提供用户信息的存储和提取服务
############################################################################################################################
class userInfo:
    '''规定用户属性'''
    defaultConfig = {}
    defaultConfig["favorability"] = 0                   # 用户好感度
    defaultConfig["favorStage"] = 0                     # 好感度阶段
    defaultConfig["favorStageName"] = "普通"            # 好感度阶段名称
    defaultConfig["favorStageStr"] = "🤍🤍🤍🤍🤍"    # 好感度字符串
    defaultConfig["favorAddToday"] = 0                  # 今天用户改变增加值
    defaultConfig["favorDeaddToday"] = 0                # 今天用户改变减少值
    defaultConfig["favorChangedLastDay"] = datetime.now().strftime("%Y%m%d") # 上一次触发好感改变的时间

    defaultConfig["commandUseLastDay"] = {}             # 上次使用某命令的时间(精确到天)
    defaultConfig["commandUseLastMin"] = {}             # 上次使用某命令的时间(精确到分钟)
    defaultConfig["commandUseLastTimestamp"] = {}       # 上次使用某命令的时间(精确到秒)

    defaultConfig["commandUseTimesAll"] = {}            # 总共使用命令的次数 / 采用字典存储
    defaultConfig["commandUseTimesToday"] = {}          # 今天使用命令的次数 / 采用字典存储
    defaultConfig["commandUseTimesToMin"] = {}          # 当前分钟使用命令的次数 / 采用字典存储
    defaultConfig["skills"] = []                        # 所有的命令

    defaultConfig["historys"] = ["normal"]              # 用户的历史集
    defaultConfig["settings"] = ["normal"]              # 用户的设定集

    defaultConfig["chooseSetting"] = "normal"           # 当前使用设定
    defaultConfig["chooseHistory"] = "normal"           # 当前使用历史

    defaultSettingPath = GRoot / "senYa" / "memory" / "config" / "master2.txt" # 默认设定
    ###############################################################################
    # Function:     __init__  
    # Notice:       
    ###############################################################################
    def __init__(self, user_id: int):
        '''初始化用户数据, 包括用户配置信息和历史数据'''
        self.user_id = user_id
        self.configDir = GUserInfoDir / f"{self.user_id}"
        self.historyDir = GUserInfoDir / f"{self.user_id}" / "history"
        self.settingDir = GUserInfoDir / f"{self.user_id}" / "setting"
        self.configPath = GUserInfoDir / f"{self.user_id}" / f"config.json"

        # 创建目录并检查
        for dir in [self.configDir, self.historyDir, self.settingDir]:
            dir.mkdir(parents = False, exist_ok = True)
            if not dir.exists():
                raise FileNotFoundError(f"folder not exist\"{dir}\"")

        # 配置文件初始化
        if self.configPath.exists():
            self.config = json2dict(self.configPath)
            for key in self.defaultConfig.keys():
                if key not in self.config:
                    self.config[key] = self.defaultConfig[key]

        else:
            self.config = self.defaultConfig.copy()

        self.historyPath = self.historyDir / f"{self.config["chooseHistory"]}.json"
        self.settingPath = self.settingDir / f"{self.config["chooseSetting"]}.json"

        # 历史数据初始化
        if self.historyPath.exists():
            self.history: list[userRecord] = []
            with self.historyPath.open(mode = "r", encoding="utf-8") as file:
                for line in file:
                    msg = json.loads(line)
                    aRecord = userRecord(msg["role"], msg["content"], msg["timestamp"])
                    self.history.append(aRecord)

        else:
            self.history = []

        # 设定初始化
        if self.settingPath.exists():
            with self.settingPath.open("r", encoding = "utf-8") as file:
                self.setting = file.read()
        elif self.defaultSettingPath.exists():
            with self.defaultSettingPath.open("r", encoding = "utf-8") as file:
                self.setting = file.read()
        else:
            raise FileNotFoundError(f"{self.defaultSettingPath} not found")
        
        self.isDialogueBusy = False

    ###############################################################################
    # Function:     historyAdd  
    # Notice:       
    ###############################################################################      
    def historyAdd(self, newHistoryName: str):
        '''创建一个全新的历史文件'''
        if newHistoryName in self.config["historys"]:
            raise FileExistsError(f"curName {newHistoryName} existed")
        
        self.config["historys"].append(newHistoryName)

    ###############################################################################
    # Function:     historyShift  
    # Notice:       
    ###############################################################################   
    def historyShift(self, newHistoryName: str):
        '''切换到一个已经存在的历史文件中, 切换时必须确保历史文件存在'''
        pass


    ###############################################################################
    # Function:     readConf  
    # Notice:       获取参数时, 建议通过此接口调用, 而不是直接访问类中的成员s
    ############################################################################### 
    def readConf(self, configName: Literal["favorability", "favorStage", "favorStageName", "favorStageStr", "favorAddToday", "favorDeaddToday",\
                                    "commandUseLastDay", "commandUseLastMin", "commandUseLastTimestamp",\
                                    "commandUseTimesAll", "commandUseTimesToday", "commandUseTimesToMin",\
                                    "favorChangedLastDay"], skillName: None|str = None):
        '''获取用户参数'''

        self.update()

        if skillName is None:
            return self.config[configName]
        elif skillName in self.config["skills"]:
            return self.config[configName][skillName]
        else:
            raise ValueError(f"can't read para \'{configName}\'.\'{skillName}\', support configName is \"{self.config["skills"]}\"")


    ###############################################################################
    # Function:     readFavor  
    # Notice:       
    ############################################################################### 
    def readFavor(self, key: Literal["stage", "stageName", "stageStr", "favorability", "seg"]):
        '''获取当前好感度信息'''
        if key == "stage":
            return self.config["favorStage"]
        elif key == "stageName":
            return self.config["favorStageName"]
        elif key == "stageStr":
            return self.config["favorStageStr"]
        elif key == "favorability":
            return self.config["favorability"]
        elif key == "seg":
            return message.text(f"Current Favor:{self.config["favorability"]}, {self.config["favorStageStr"]}")
        else:
            raise ValueError(f"[readFavor]unsupported key \'{key}\'") 

    ###############################################################################
    # Function:     readHistory  
    # Notice:       
    ###############################################################################      
    def readHistory(self, len: int, format: Literal["record", "dict", "dict_timeless"]):
        '''读取历史数据'''
        if format == "record":
            return self.history[-1 * len:]
        elif format == "dict":
            data = [record.toDict() for record in self.history]
            return data[-1 * len:]
        elif format == "dict_timeless":
            data = [record.toDict(neadTime = False) for record in self.history]
            return data[-1 * len:]
        else:
            raise TypeError(f"[readHistory]unsupport format {format}")

    ###############################################################################
    # Function:     save  
    # Notice:       
    ############################################################################### 
    def save(self):
        '''保存配置文件'''
        with self.configPath.open("w", encoding="utf-8") as file:
            json.dump(self.config, file, ensure_ascii = False, indent = 4)

    ###############################################################################
    # Function:     favorAdd  
    # Notice:       
    ############################################################################### 
    def favorAdd(self, addValue: int):
        '''添加好感度'''

        # 查看当前时间
        self.update()
        now = datetime.now()
        self.config["favorChangedLastDay"] = now.strftime("%Y%m%d")

        # 调整增加值
        if addValue >= 0:

            # 好感衰减
            decayStage = self.config["favorAddToday"] // FAVOR_HALF_DECAY
            addValue = np.ceil((addValue / (2 ** decayStage)))

            addValue = min(addValue, FAVOR_ADD_MAX_ADAY - self.config["favorAddToday"])
            self.config["favorAddToday"] += abs(addValue)

        else:
            # 降低无衰减
            decreaseValue = abs(addValue)
            decreaseValue = min(decreaseValue, FAVOR_DEADD_MAX_ADAY - self.config["favorDeaddToday"])
            self.config["favorDeaddToday"] += decreaseValue
            addValue = -1 * decreaseValue

        self.config["favorability"] += addValue
        originStage = self.config["favorStage"]

        # 获取好感
        if addValue == 0:
            return message.text(f"\nFavor change limited today, 主人明天再来哦")
        else:
            
            if self.config["favorability"] < FAVOR_GREAT_DISTASTE:
                self.config["favorStage"] = -3; self.config["favorStageName"] = "非常厌恶"
                self.config["favorStageStr"] = "🖤🖤🖤"
            elif self.config["favorability"] < FAVOR_DISTASTE:
                self.config["favorStage"] = -2; self.config["favorStageName"] = "厌恶"
                self.config["favorStageStr"] = "🖤🖤"
            elif self.config["favorability"] < FAVOR_DISGUSTING:
                self.config["favorStage"] = -1; self.config["favorStageName"] = "讨厌"
                self.config["favorStageStr"] = "🖤"
            elif self.config["favorability"] < FAVOR_NORMAL:
                self.config["favorStage"] = 0; self.config["favorStageName"] = "普通"
                self.config["favorStageStr"] = "❤️🤍🤍🤍🤍"
            elif self.config["favorability"] < FAVOR_FAMILIARIZE:
                self.config["favorStage"] = 1; self.config["favorStageName"] = "熟悉"
                self.config["favorStageStr"] = "❤️❤️🤍🤍🤍"
            elif self.config["favorability"] < FAVOR_INTIMATE:
                self.config["favorStage"] = 2; self.config["favorStageName"] = "亲密"
                self.config["favorStageStr"] = "❤️❤️❤️🤍🤍"
            elif self.config["favorability"] < FAVOR_LOVE:
                self.config["favorStage"] = 3; self.config["favorStageName"] = "喜欢"
                self.config["favorStageStr"] = "❤️❤️❤️❤️🤍"
            else:
                self.config["favorStage"] = 4; self.config["favorStageName"] = "非常喜欢"
                self.config["favorStageStr"] = "❤️❤️❤️❤️❤️"

            self.save()

            # 回复消息
            if originStage == self.config["favorStage"]:
                return message.text(f"\nFavor added: {addValue}, {self.config["favorStageStr"]}")
            elif originStage < self.config["favorStage"]:
                return message.text(f"\nFavor added: {addValue}, 好感度已经提升到\"{self.config["favorStageName"]}\"了哦")
            else:
                return message.text(f"\nFavor added: {addValue}, 变态主人, 好感度已经降低到\"{self.config["favorStageName"]}\"了哦")

    ###############################################################################
    # Function:     recordAdd  
    # Notice:       
    ############################################################################### 
    def recordAdd(self, role: Literal["assistant", "user"], msg: str)->list[userRecord]:
        '''添加记录'''
        if msg is None:
            return

        aRecord = userRecord(role, msg)

        # 添加进文件
        with self.historyPath.open(mode = "a", encoding = "utf-8") as file:
            json.dump(aRecord.toDict(), file, ensure_ascii = False)
            file.write("\n")
        
        # 添加进历史
        self.history.append(aRecord)

    ###############################################################################
    # Function:     commandAdd  
    # Notice:       
    ###############################################################################
    def commandAdd(self, skillName: str):
        '''在命令被调用时同时调用此方法, 增加该用户对于该命令的调用统计'''

        now = datetime.now(); today = now.strftime("%Y%m%d"); toMin = now.strftime("%Y%m%d%H%M");

        # 命令统计初始化
        self.commandInit(skillName)

        # 命令统计增加
        self.config["commandUseTimesAll"][skillName] += 1
        self.config["commandUseTimesToday"][skillName] += 1
        self.config["commandUseTimesToMin"][skillName] += 1

        self.config["commandUseLastDay"][skillName] = today
        self.config["commandUseLastMin"][skillName] = toMin
        self.config["commandUseLastTimestamp"][skillName] = time.time()

        # 更新
        self.update()

    ###############################################################################
    # Function:     commandInit  
    # Notice:       
    ###############################################################################
    def commandInit(self, skillName: str):
        '''初始化一个用户命令统计, 在使用一个命令之前必须先使用此方法'''
        now = datetime.now(); today = now.strftime("%Y%m%d"); toMin = now.strftime("%Y%m%d%H%M");

        # 命令统计初始化
        if skillName not in self.config["skills"]:
            self.config["skills"].append(skillName)
            self.config["commandUseTimesAll"][skillName] = 0
            self.config["commandUseTimesToday"][skillName] = 0
            self.config["commandUseTimesToMin"][skillName] = 0
            self.config["commandUseLastDay"][skillName] = today
            self.config["commandUseLastMin"][skillName] = toMin
            self.config["commandUseLastTimestamp"][skillName] = time.time()

    ###############################################################################
    # Function:     update  
    # Notice:       
    ###############################################################################
    def update(self):
        '''刷新命令参数, 包括每分钟调用参数和每天调用参数'''

        now = datetime.now(); today = now.strftime("%Y%m%d"); toMin = now.strftime("%Y%m%d%H%M");

        # 所有命令更新
        for skillName in self.config["skills"]:
            if self.config["commandUseLastDay"][skillName] != today:
                self.config["commandUseTimesToday"][skillName] = 0
            if self.config["commandUseLastMin"][skillName] != toMin:
                self.config["commandUseTimesToMin"][skillName] = 0

        # 所有好感更新
        if self.config["favorChangedLastDay"] != today:
            self.config["favorAddToday"] = 0
            self.config["favorDeaddToday"] = 0
    
        self.save()