###############################################################################
#   File name:   senyaHime.py
#   Description: 描述千夜姬响应逻辑
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from flask import Flask, request, jsonify

from path import initCardPool, stateCardPool
from plugin.cardPool import cardPool
from tool.common.log import logInfo
from autoBotAPI.shamrockBot import shamrockbot, message, callbackmsg
from .api.card import *
from .api.touch import *

##############################################################
# Class:        SenYaHime
# Input:        void
# Notice:       确保模拟器已经启动并启用ADB调试
##############################################################
class SenYaHime(shamrockbot):
    '''构建千夜姬机器人实例'''
    def __init__(self, name: str, clientPort: int, hostPort: int, hostIP: str, accessToken: str) -> None:
        super().__init__(name, clientPort, hostPort, hostIP, accessToken)

        # 初始化卡池
        self.qianyePool = cardPool("千夜酱测试卡池", stateCardPool)

        # 定义命令集
        self.commandMenu = {
            "抽奖" : self.drawCard,
            "重置卡池" : self.reInitCardPool,
            "查看卡池状态" : lambda msg : self.reply(msg, self.qianyePool.stateInfo()),
            "喵喵喵" : lambda msg : self.reply(msg, "喵喵喵~~~"),
            "测试": lambda msg : self.test(msg),
            "戳戳": lambda msg : self.chuochuo(msg)
        }

        # 定义回调函数
        self.HTTPcallbackDef(self.receive)

    ###############################################################################
    # Function:     test
    # Input:        void     
    # Notice:       测试响应是否正常
    ###############################################################################
    def test(self, msg: callbackmsg):
        # 测试一下群聊信息
        self.reply(msg, "收到命令")

        t3 = message.text(r"# 这是一级标题\n## 这是二级标题\n### 这是三级标题")
        response = self.send_group_msg(group_id = 104491286, message = t3)

        logInfo(f"[Test]:{response}")

    ###############################################################################
    # Function:     receive
    # Input:        void     
    # Notice:       
    ###############################################################################
    def receive(self):
        '''接收消息'''

        msg = callbackmsg(request.get_json(force=True))
        logInfo(f"[receive_debug]:{msg}")

        # 网络debug尝试
        shamrock_ip = request.remote_addr
        shamrock_port = request.environ.get('REMOTE_PORT')
        logInfo(f"[receive_debug]get Shamrock src IP: {shamrock_ip}, src port: {shamrock_port}")
        self.URLupdate(clientIP = shamrock_ip)

        commandText = msg.resolve()
        logInfo(f"[receive_debug]get command = \"{commandText}\"")
        if commandText is not None and commandText in self.commandMenu:
            self.commandMenu[commandText](msg)  # 执行命令对应的函数, 必须允许输入msg, 而且必须是单一输入
        elif commandText is not None:
            self.reply(msg, f"对不起主人喵, 你使用了不支持的命令\"{commandText}\"")

        # 返回数据
        return jsonify({"status": "success"}), 200

    ###############################################################################
    # Function:     reply
    # Input:        msg
    #               mainmsg     
    # Notice:       
    ###############################################################################  
    def reply(self, msg: callbackmsg, mainmsg: message.messageSegment | str, auto_escape = None, recall_duration = None, isreply = True):
        '''回复消息'''
        if isinstance(mainmsg, message.reply):
            raise TypeError(r"can't use reply with reply message")

        if isinstance(mainmsg, str):
            mainmsg = message.text(text = mainmsg)

        allmsg = message.reply(id = msg.message_id) + mainmsg if isreply and msg.message_id is not None else mainmsg

        if msg.message_type == "group":
            returnInfo = self.send_group_msg(group_id = msg.group_id, message = allmsg, auto_escape = auto_escape, recall_duration = recall_duration)
        elif msg.message_type == "private":
            returnInfo = self.send_private_msg(user_id = msg.user_id, message = allmsg, auto_escape = auto_escape, recall_duration = recall_duration)
        else:
            raise TypeError(f"[reply]find unsupport message_type \"{msg.message_type}\"")
        
        logInfo(f"[reply_response]:{returnInfo}")

    # 抽卡命令
    drawCard = drawCard
    reInitCardPool = reInitCardPool

    # 戳一戳命令
    chuochuo = chuochuo