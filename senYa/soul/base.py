###############################################################################
#   File name:   base.py
#   Description: 千夜姬主框架
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from flask import request, jsonify
from typing import Literal
import asyncio, json

from control import DEBUG_MODE
from ..memory import logInfo
from ..physics import httpserver, websocketserver, message

from.core import mentalCore
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
            # 格式化消息
            backMsg = message.callbackmsg(request.get_json(force=True))

            if DEBUG_MODE:
                logInfo(f"[receive_debug]:{backMsg}")

            # 调用心智核心获取回复
            cmdMsgSeg, cmdArgs = self.core.resolve(backMsg, self.server)
            if cmdMsgSeg is None or cmdArgs is None:
                raise ValueError

            # 消息发送
            if backMsg.GorP == "group":
                returnInfo = self.server.send_group_msg(group_id = backMsg.msgEntity.group_id, message = cmdMsgSeg, auto_escape = cmdArgs.auto_escape, recall_duration = cmdArgs.recall_duration)
            elif backMsg.GorP == "private":
                returnInfo = self.server.send_private_msg(user_id = backMsg.msgEntity.user_id, message = cmdMsgSeg, auto_escape = cmdArgs.auto_escape, recall_duration = cmdArgs.recall_duration)
            else:
                raise TypeError(f"[reply]find unsupport message_type \"{backMsg.GorP}\"")
            
            logInfo(f"[reply_response]:{returnInfo}")

        except TypeError as e:
            logInfo(str(e))
            return jsonify({"status": "success"}), 200
        except ValueError as e:
            return jsonify({"status": "success"}), 200
        except Exception as e:
            logInfo(str(e))
            return jsonify({"status": "failed"}), 404      
        else:
            return jsonify({"status": "success"}), 200

    ###############################################################################
    # Function:     websocketReceive    
    # Notice:       
    ###############################################################################       
    async def websocketReceive(self, backMsgStr: str):
        '''websocket接收消息'''

        # 格式化消息
        backMsg = message.callbackmsg(json.loads(backMsgStr))

        if DEBUG_MODE:
            logInfo(f"[receive_debug]:{backMsg}")

        # 调用心智核心获取回复
        cmdMsgSeg, cmdArgs = self.core.resolve(backMsg, self.server)
        if cmdMsgSeg is None or cmdArgs is None:
            return

        # 消息发送
        if backMsg.GorP == "group":
            await self.server.send_group_msg(group_id = backMsg.msgEntity.group_id, message = cmdMsgSeg, auto_escape = cmdArgs.auto_escape, recall_duration = cmdArgs.recall_duration)
        elif backMsg.GorP == "private":
            await self.server.send_private_msg(user_id = backMsg.msgEntity.user_id, message = cmdMsgSeg, auto_escape = cmdArgs.auto_escape, recall_duration = cmdArgs.recall_duration)
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