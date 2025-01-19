###############################################################################
#   File name:   path.py
#   Description: 处理根路径
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
import sys
from pathlib import Path

###############################################################################
# Function:     isRunInexe
# Input:        void
# Notice:       
###############################################################################
def isRunInexe():
    """判断是否在exe中"""
    return getattr(sys, "frozen", False)

###############################################################################
# Function:     getRootDir
# Input:        void
# Notice:       
###############################################################################
def getRootDir():
    """获取整个工具所在根路径"""
    if isRunInexe():
        return Path(sys.executable).parent.resolve()          # 在exe中运行
    return Path(__file__).parent.resolve()                     # 直接运行

GRoot = getRootDir()
GLogDir = GRoot / "doc" / "log"
GreadmeDir = GRoot / "doc" / "readme"
initCardPool = GRoot / "doc" / "cardPool" / "qianyeServicePool_init.json"
stateCardPool = GRoot / "doc" / "cardPool" / "qianyeServicePool_state.json"