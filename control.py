###############################################################################
#   File name:   control.py
#   Description: 提供部分控制参数
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
import sys, json
from pathlib import Path

BOT_NAME = "SenyaHime"
BOT_CLIENT_ACTIVE_HTTP_PORT = 5001  # 客户端主动HTTP端口 / 可以选择auto
BOT_CLIENT_IP = "192.168.0.150"     # 客户端主动HTTPIP / 可以选择auto
BOT_HOST_HTTP_LISTEN_PORT = 5700    # 服务器端监听端口
BOT_HOST_IP = "192.168.0.105"       # 服务器端IP
BOT_ACCESSTOKEN = "guzhaoqiaoqiaoa1"# 鉴权密钥
BOT_PROTOCOL = "websocket"          # 使用bot协议 / 可以选择websocket或者http

PRODUCTION_MODE = False             # 生产模式 / 仅HTTP有效
DEBUG_MODE = False                  # 开启debug输出
HEARTBEAT_INTETNAL = 5              # 心跳包间隔时间(s)
LOG_LEN_MAX = 1000                  # log输出最大长度

FAVOR_ADD_LEAST = 30                # 单次行为好感增加下限
FAVOR_ADD_MAX = 40                  # 单次行为好感增加上限
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

###############################################################################
# Function:     json2dict  
# Notice:       
###############################################################################
def json2dict(configPath: Path)->dict:
    '''将json转换为dict'''
    with configPath.open("r", encoding = "utf-8") as file:
        touchList = json.load(file)
        return touchList

# 初始化所有路径
GRoot = getRootDir()
GLogDir = GRoot / "senYa" / "memory" / "log" / "logs"
GUserInfoDir = GRoot / "senYa" / "memory" /  "user" / "users"
replyPath = GRoot / "senYa" / "memory" / "reply" / "touch"

# 初始化所有回复列表
touchReply = json2dict(replyPath / "touch.json")
touchBellyReply = json2dict(replyPath / "touchBelly.json")
touchEarReply = json2dict(replyPath / "touchEar.json")
touchFaceReply = json2dict(replyPath / "touchFace.json")
touchFootReply = json2dict(replyPath / "touchFoot.json")
touchHairReply = json2dict(replyPath / "touchHair.json")
touchHandReply = json2dict(replyPath / "touchHand.json")
touchHeadReply = json2dict(replyPath / "touchHead.json")
touchLegReply = json2dict(replyPath / "touchLeg.json")
touchSensitiveReply = json2dict(replyPath / "touchSensitive.json")
touchUnknownReply = json2dict(replyPath / "touchUnknown.json")