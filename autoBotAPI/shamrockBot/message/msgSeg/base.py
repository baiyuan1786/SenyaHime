###############################################################################
#   File name:   base.py
#   Description: 消息段基类
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from typing import Literal

###############################################################################
# Class:        messageSegment     
# Input:        @type
#               @data
# Notice:       
###############################################################################
class messageSegment:
    '''QQ消息段, 用来处理QQ发送的各种消息类型, 如TEXT型, Image型, 这个是消息段基类'''
    def __init__(self, type: str | list[str], data: dict | list[dict], msgType: str = "base") -> None:
        self.type = type
        self.data = data

        if isinstance(type, str) and isinstance(data, dict):
            filterData = {key : data[key] for key in data.keys() if data[key] is not None} # 增加空值过滤
            self.types = [type]
            self.datas = [filterData]
        elif isinstance(type, list) and isinstance(data, list):
            self.types = type
            self.datas = data
        else:
            raise TypeError("use undefined type to init messageSegment")
        
        self.msgType = msgType
        
    ###############################################################################
    # Function:     __add__    
    # Input:        @other 另一个此类的实例
    # Notice:       
    ###############################################################################
    def __add__(self, other):
        '''类的加法'''
        if not isinstance(other, messageSegment):
            raise TypeError("[messageSegment]Unsupported operand type(s) for +")
        
        # 空格处理
        if self.msgType == "at" and other.msgType == "text":
            other.datas[0]["text"] = " " + other.datas[0]["text"]
        elif other.msgType == "at" and self.msgType == "text":
            self.datas[0]["text"] = self.datas[0]["text"] + " "

        return messageSegment(type = self.types + other.types, data = self.datas + other.datas, msgType = other.msgType)

    ###############################################################################
    # Function:     __str__    
    # Input:        void
    # Notice:       
    ###############################################################################
    def __str__(self):
        return "暂未实现该类的__str__"

    ###############################################################################
    # Function:     toList    
    # Input:        void
    # Notice:       
    ###############################################################################
    def toList(self):
        '''转换为消息段列表输出'''
        segments = [{"type": type, "data": data} for type, data in zip(self.types, self.datas)]
        return segments