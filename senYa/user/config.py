###############################################################################
#   File name:   config.py
#   Description: 处理用户配置
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from pathlib import Path
from path import GUserInfoDir
import yaml, json, time
from autoBotAPI.shamrockBot import httpserver, websocketserver, message
from control import DEBUG_MODE
from plugin.log import logInfo
from datetime import datetime

FAVOR_GREAT_DISTASTE = -10000
FAVOR_DISTASTE = -1000
FAVOR_DISGUSTING = 0
FAVOR_NORMAL = 100
FAVOR_FAMILIARIZE = 700
FAVOR_INTIMATE = 1500
FAVOR_LOVE = 3000
FAVOR_ADD_MAX_ADAY = 100                         # 一天允许增加好感度上限
FAVOR_DEADD_MAX_ADAY = 500                       # 一天允许减少好感度上限
##############################################################
# Class:        userConfig
# Input:        void
# Notice:       
##############################################################
class userConfig:
    '''用户配置文件'''
    defaultConfig = {}
    defaultConfig["favorability"] = 0                   # 用户好感度
    defaultConfig["favorStage"] = 0                     # 好感度阶段
    defaultConfig["favorStageName"] = "普通"            # 好感度阶段名称
    defaultConfig["favorStageStr"] = "🤍🤍🤍🤍🤍"    # 好感度字符串
    defaultConfig["favorAddAday"] = 0                   # 用户改变增加值
    defaultConfig["favorDeaddAday"] = 0                 # 用户改变减少值
    defaultConfig["commandlastUseTimestamp"] = {}       # 上次使用某命令的时间戳
    defaultConfig["commandUseTimes"] = {}               # 使用命令的次数 / 采用字典存储
    defaultConfig["favorChangedTimeLast"] = None        # 上一次触发好感改变的时间

    ###############################################################################
    # Function:     __init__  
    # Notice:       
    ############################################################################### 
    def __init__(self, user_id: int):
        '''使用user_id初始化即可'''
        self.user_id = user_id
        self.configDir = GUserInfoDir / f"{self.user_id}"
        self.configPath = GUserInfoDir / f"{self.user_id}" / f"config.json"

        if not self.configDir.exists():
            raise FileNotFoundError(f"folder not exist\"{self.configDir}\"")

        # 配置文件已经存在时初始化
        if self.configPath.exists():
            with self.configPath.open("r", encoding="utf-8") as file:
                self.config = json.load(file)
                for key in self.defaultConfig.keys():
                    if key not in self.config:
                        self.config[key] = self.defaultConfig[key]

        # 配置文件不存在时初始化
        else:
            self.config = self.defaultConfig.copy()

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
        now = datetime.now()
        if self.config["favorChangedTimeLast"] is None:
            self.config["favorChangedTimeLast"] = now.strftime("%Y%m%d")
        
        # 重置每日限度
        if self.config["favorChangedTimeLast"] != now.strftime("%Y%m%d"):
            self.config["favorAddAday"] = 0
            self.config["favorDeaddAday"] = 0

        # 调整增加值
        if addValue >= 0:
            addValue = min(addValue, FAVOR_ADD_MAX_ADAY - self.config["favorAddAday"])
            self.config["favorAddAday"] += abs(addValue)
        else:
            decreaseValue = abs(addValue)
            decreaseValue = min(decreaseValue, FAVOR_DEADD_MAX_ADAY - self.config["favorDeaddAday"])
            self.config["favorDeaddAday"] += decreaseValue
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
        