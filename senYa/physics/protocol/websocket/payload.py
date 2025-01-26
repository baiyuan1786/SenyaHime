###############################################################################
#   File name:   payload.py
#   Description: websocket服务器类发送载荷
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ...message.msgSeg.base import messageSegment
import json, websockets, asyncio
from ....memory.log import logInfo
from control import DEBUG_MODE, LOG_LEN_MAX
###############################################################################
# Class:        payload     
# Input:        void
# Notice:       
###############################################################################
class payload:
    '''websocket服务器的发送载荷'''
    def __init__(self, websocket: websockets.WebSocketServerProtocol, accessToken: str, action: str, echo: str = " "):
        if websocket is None:
            raise ValueError(f"websocket not init, can't use \"{action}\"")
        
        if action.startswith("/"):
            action = action.split("/")[-1]
        self.websocket = websocket
        self.data = {"action": action, "echo": echo}
        self.params = {"access_token": accessToken}

    ###############################################################################
    # Function:     argAdd
    # Input:        @argName
    #               @argValue     
    # Notice:       
    ###############################################################################
    def argAdd(self, argName: str, argValue: str | int | messageSegment | None):
        '''为命令添加额外的参数'''
        if argValue is None:
            return
        elif isinstance(argValue, messageSegment):
            self.params[argName] = argValue.toList()
        else:
            self.params[argName] = argValue

    ###############################################################################
    # Function:     post
    # Notice:       
    ###############################################################################
    async def post(self):
        '''异步post函数'''
        self.data["params"] = self.params

        logInfo(f"[websocketserver]Posed: {self.data}\n")

        await self.websocket.send(json.dumps(self.data))