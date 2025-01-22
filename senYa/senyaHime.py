###############################################################################
#   File name:   senyaHime.py
#   Description: 描述千夜姬响应逻辑
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from flask import request, jsonify
from typing import Literal
import asyncio, websockets, json, threading

from.core import mentalCore
from control import DEBUG_MODE
from plugin.log import logInfo
from autoBotAPI.shamrockBot import httpserver, websocketserver, message
##############################################################
# Class:        SenYaHime
# Notice:       
##############################################################
class SenYaHime:
    '''构建千夜姬机器人实例'''
    def __init__(self, name: str, clientPort: int, hostPort: int, clientIP: str, hostIP: str, accessToken: str, protocol: Literal["websocket", "http"]) -> None:

        # 定义命令集
        self.name = name
        self.protocol = protocol

        # http协议
        if protocol == "http":
            self.server = httpserver(name, clientPort, hostPort, clientIP, hostIP, accessToken)
            self.server.callbackDef(self.httpReceive)

        # websocket协议
        elif protocol == "websocket":
            self.server = websocketserver(name, hostPort, hostIP, accessToken)
            self.server.callbackDef(self.websocketReceive)

        else:
            raise TypeError(f"[SenYaHime]use undefined protocol \"{protocol}\"")
        
        # 心智核心
        self.core = mentalCore()
    ###############################################################################
    # Function:     httpReceive  
    # Notice:       
    ###############################################################################
    def httpReceive(self):
        '''HTTP接收消息'''

        try:
            backMsg = message.callbackmsg(request.get_json(force=True))

            if DEBUG_MODE:
                logInfo(f"[receive_debug]:{backMsg}")

            # 调用心智核心获取回复
            cmdMsgSeg, cmdSovled = self.core.resolve(backMsg, self.server)
            if cmdMsgSeg is not None and cmdSovled is not None:
                self.httpReply(backMsg, cmdMsgSeg, cmdSovled.auto_escape, cmdSovled.recall_duration, cmdSovled.isreply)

        except TypeError as e:
            logInfo(str(e))
            return jsonify({"status": "success"}), 200
        except Exception as e:
            logInfo(str(e))
            return jsonify({"status": "failed"}), 404
        else:
            return jsonify({"status": "success"}), 200

    ###############################################################################
    # Function:     httpReply   
    # Notice:       
    ###############################################################################  
    def httpReply(self, backMsg: message.callbackmsg, mainmsg: message.messageSegment | str, auto_escape = None, \
              recall_duration = None, isreply = False):
        """回复消息

        :param backMsg: callback消息
        :param mainmsg: 需要发送的消息
        :param auto_escape: 自动撤回, defaults to None
        :param recall_duration: 自动撤回时间间隔(ms), defaults to None
        :param isreply: 是否以回复方式回复, defaults to False
        """        
        
        # 类型处理
        if isinstance(mainmsg, message.reply):
            raise TypeError(r"can't use reply with reply message")
        if isinstance(mainmsg, str):
            mainmsg = message.text(text = mainmsg)

        # 回复处理
        allmsg = message.reply(id = backMsg.msgEntity.message_id) + mainmsg if isreply and backMsg.canReply() else mainmsg

        # 消息发送
        if backMsg.GorP == "group":
            returnInfo = self.server.send_group_msg(group_id = backMsg.msgEntity.group_id, message = allmsg, auto_escape = auto_escape, recall_duration = recall_duration)
        elif backMsg.GorP == "private":
            returnInfo = self.server.send_private_msg(user_id = backMsg.msgEntity.user_id, message = allmsg, auto_escape = auto_escape, recall_duration = recall_duration)
        else:
            raise TypeError(f"[reply]find unsupport message_type \"{backMsg.GorP}\"")
        
        logInfo(f"[reply_response]:{returnInfo}")

    ###############################################################################
    # Function:     websocketReceive    
    # Notice:       
    ###############################################################################       
    async def websocketReceive(self, backMsgStr: str):
        '''websocket接收消息'''

        #try:
        if True:
            backMsg = message.callbackmsg(json.loads(backMsgStr))

            if DEBUG_MODE:
                logInfo(f"[receive_debug]:{backMsg}")

            # 调用心智核心获取回复
            cmdMsgSeg, cmdSovled = self.core.resolve(backMsg, self.server)
            if cmdMsgSeg is not None and cmdSovled is not None:
                await self.websocketReply(backMsg, cmdMsgSeg, cmdSovled.auto_escape, cmdSovled.recall_duration, cmdSovled.isreply)

        #except TypeError as e:
        #    logInfo(str(e))

    ###############################################################################
    # Function:     websocketReply   
    # Notice:       
    ###############################################################################  
    async def websocketReply(self, backMsg: message.callbackmsg, mainmsg: message.messageSegment | str, auto_escape = None, \
              recall_duration = None, isreply = False):
        """回复消息

        :param backMsg: callback消息
        :param mainmsg: 需要发送的消息
        :param auto_escape: 自动撤回
        :param recall_duration: 自动撤回时间间隔(ms)
        :param isreply: 是否以回复方式回复
        """        
        
        # 类型处理
        if isinstance(mainmsg, message.reply):
            raise TypeError(r"can't use reply with reply message")
        if isinstance(mainmsg, str):
            mainmsg = message.text(text = mainmsg)

        # 回复处理
        allmsg = message.reply(id = backMsg.msgEntity.message_id) + mainmsg if isreply and backMsg.canReply() else mainmsg

        # 消息发送
        if backMsg.GorP == "group":
            await self.server.send_group_msg(group_id = backMsg.msgEntity.group_id, message = allmsg, auto_escape = auto_escape, recall_duration = recall_duration)
        elif backMsg.GorP == "private":
            await self.server.send_private_msg(user_id = backMsg.msgEntity.user_id, message = allmsg, auto_escape = auto_escape, recall_duration = recall_duration)
        else:
            raise TypeError(f"[reply]find unsupport message_type \"{backMsg.GorP}\"")

    ###############################################################################
    # Function:     run
    # Notice:       
    ###############################################################################  
    def run(self):
        '''运行服务器'''
        try:
            self.server.run()
        except KeyboardInterrupt:
            logInfo(f"[{self.name}]Server stopped.")
        