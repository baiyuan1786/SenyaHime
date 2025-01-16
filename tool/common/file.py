###############################################################################
#   File name:   file.py
#   Description: 文件处理工具
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
import json

###############################################################################
# Function:     readConfig
# Description:  读取配置文件(json)
# Input:        filePath, configName
# Return:       
# Notice:       
###############################################################################
def readConfig(filePath : str, configName : str):
    with open('config.json', 'r') as file:
        configValueDict = json.load(file)
        if not isinstance(configValueDict, dict):
            raise TypeError(f"[readConfig]can not open \"{filePath}\" as dict")

        if configName in configValueDict.keys():
            return configValueDict[configName]
        else:
            raise NameError(f"[readConfig]not found \"{configName}\" in \"{filePath}\"")

###############################################################################
# Function:     writeConfig
# Description:  写入配置文件
# Input:        filePath， configName， value
# Return:       void
# Notice:       
###############################################################################
def writeConfig(filePath : str, configName : str, value : str):
    with open('config.json', 'r+') as file:
        configValueDict = json.load(file)
        if not isinstance(configValueDict, dict):
            raise TypeError(f"[writeConfig]can not open \"{filePath}\" as dict")

        configValueDict[configName] = value
        json.dump(configValueDict, filePath, indent=4)
            