###############################################################################
#   File name:   base.py
#   Description: 触发函数基类
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from ..physics import message, httpserver, websocketserver

# 定义泛型类型
User = TypeVar('User')       # 用户类类型
Server = TypeVar('Server')   # 服务器类类型
BackMsg = TypeVar('BackMsg') # 回传消息类类型
Message = TypeVar('Message') # 返回消息类类型

############################################################################################################################
# Class:        TriggerFunction
# Notice:       抽象基类，定义了触发函数的接口和通用属性。
############################################################################################################################
class TriggerFunction(ABC, Generic[User, Server, BackMsg, Message]):
    """触发函数抽象基类，定义通用接口和属性"""

    def __init__(self, isNeedAt: bool, isReply: bool, isAt: bool, skillName: str | None, autoEscape: bool | None = None, recallDuration: int | None = None):
        """初始化通用参数

        :param isNeedAt: 是否需要 @ 指定用户触发
        :param isReply: 是否以回复格式进行
        :param isAt: 是否以 @ 格式进行
        :param skillName: 触发的技能名称（命令名称）
        :param autoEscape: 是否启用自动撤回
        :param recallDuration: 自动撤回时间,单位为ms
        """
        super().__init__()
        self.isNeedAt = isNeedAt
        self.isReply = isReply
        self.isAt = isAt
        self.skillName = skillName
        self.autoEscape = autoEscape
        self.recallDuration = recallDuration

    @abstractmethod
    def realize(self, user: User, server: Server, backMsg: BackMsg) -> Message|None:
        """
        定义接口：接收用户、服务器和回传消息，返回消息类型。
        强制要求触发函数的子类实现此方法。
        
        :param user: 用户信息对象
        :param server: 服务器信息对象
        :param backMsg: 回传消息对象
        :return: 消息对象
        """
        pass

    def execute(self, user: User, server: Server, backMsg: BackMsg)-> Message|None:
        '''
        执行触发函数实现, 并进行包装
        '''

        if self.isNeedAt and not backMsg.isAtme():
            raise NameError("not at me")

        user.commandInit(self.skillName)
        allMsg = self.realize(user, server, backMsg)
        user.commandAdd(self.skillName)

        # reply和at处理
        if self.isReply and backMsg.replyable() and self.isAt and backMsg.atable():
            allMsg = message.reply(id = backMsg.msgEntity.message_id) + message.at(qq = user.user_id) + allMsg
        elif self.isReply and backMsg.replyable():
            allMsg = message.reply(id = backMsg.msgEntity.message_id) + allMsg
        elif self.isAt and backMsg.atable():
            allMsg = message.at(qq = user.user_id) + allMsg
        
        return allMsg