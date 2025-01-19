###############################################################################
#   File name:   log.py
#   Description: log处理工具
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from typing import Literal
from datetime import datetime
from path import GRoot, GLogDir

LogPath = None
###############################################################################
# Function:     curHublog
# Input:        void
# Notice:       
###############################################################################
def curHublog():
    """获取当前log文件路径"""
    global LogPath
    return LogPath

###############################################################################
# Function:     dateTimeGet
# Input:        timeFormat
# Notice:       
###############################################################################
def dateTimeGet(timeFormat : Literal["underLine", "suffix", "log"] = "underLine"):
    """获取当前时间的年月日-时分秒字符串"""
    curDateTime = datetime.now()

    # 下划线格式
    if timeFormat == "underLine":
        formatTime = curDateTime.strftime("%Y_%m_%d_%H_%M_%S")

    # 后缀格式
    elif timeFormat == "suffix":
        formatTime = curDateTime.strftime("%Y%m%d%H%M%S")

    # log格式
    elif timeFormat == "log":
        formatTime = curDateTime.strftime("%Y-%m-%d %H:%M:%S")

    else:
        raise TypeError(f"[dateTimeGet]use unsupport type {timeFormat}")

    return formatTime
###############################################################################
# Function:     logInit
# Input:        void
# Notice:       
###############################################################################
def logInit():
    """log初始化函数"""
    global LogPath

    if LogPath is not None and LogPath.exists():
        return

    LogPath = GLogDir / f"HUB_{dateTimeGet()}.log"

    with LogPath.open(mode = "a", encoding = "utf-8") as file:
        file.write("===================AUTOTOOL HUB EXPORT LOG {0}================\n\n".format(dateTimeGet()))

###############################################################################
# Function:     logInfo
# Input:        @*args:输入参数
#               @**kwargs:可变关键字
# Notice:       
###############################################################################
def logInfo(*args, **kwargs):
    """带时间的输出函数,凡使用此函数进行的print都会保存log"""
    global LogPath
    logInit()
    datatimelog = "[{0}]".format(dateTimeGet(timeFormat = "log"))

    print(datatimelog, end = ""); print(*args, **kwargs)
    with LogPath.open(mode = "a", encoding = "utf-8") as file:
        outPutStr = " ".join(map(str, args))
        file.write(datatimelog)
        file.write(outPutStr + "\n")