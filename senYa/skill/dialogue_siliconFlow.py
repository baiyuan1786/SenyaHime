###############################################################################
#   File name:   dialogue_siliconFlow.py
#   Description: 使用硅基流动服务器完成文本对话请求
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .base import TriggerFunction
from ..physics import message, httpserver, websocketserver
from ..memory.user import userInfo
from ..memory.log import logInfo

import requests, json, time
from pathlib import Path
from control import GRoot, MASTERS, SILICON_API_KEY, DEBUG_MODE

NORMAL_HISTORY_LEN = 5
MASTER_HISITORY_LEN = 50

# 流量限制策略
PARALLEL_CONNECTION_LIMIT = 5 
PARALLEL_CONNECTION_NUM = 0
REQUESTS_PER_MIN = 5
REQUESTS_PER_DAY = 50
############################################################################################################################
# Class:        dialogue
# Notice:       千夜姬对话功能
############################################################################################################################
class dialogue(TriggerFunction[userInfo, httpserver|websocketserver, message.callbackmsg, message.messageSegment]):
    '''千夜姬对话功能, 使用硅基流动API实现对话'''
    def __init__(self):
        super().__init__(isNeedAt = True, isReply = False, isAt = True,\
                          skillName = "dialogue" , autoEscape = None, recallDuration = None)

    ###############################################################################
    # Function:     realize  
    # Notice:       实现
    ###############################################################################
    def realize(self, user, server, backMsg):

        # 构建messages
        commandText = backMsg.resolve()
        if commandText is not None:

            # 以管理员权限构建
            if user.user_id in MASTERS and backMsg.GorP == "private":

                messages = [{"role": "user", "content": user.setting}, {"role": "assistant", "content": "好的主人~小千夜为您服务"}]
                messages += user.readHistory(len = MASTER_HISITORY_LEN, format = "dict_timeless")
                messages.append({"role": "user", "content": commandText})

            # 以普通权限构建
            else:

                return message.text(text = "主人, 对话功能还在开发中哦")

                # 访问限制
                timesToday = user.readConf(configName = "commandUseTimesToday", skillName = self.skillName)
                timesToMin = user.readConf(configName = "commandUseTimesToMin", skillName = self.skillName)

                if PARALLEL_CONNECTION_NUM >= PARALLEL_CONNECTION_LIMIT:
                    return message.text(text = f"主人, 服务器繁忙, 请稍后再试哦~")
                if timesToday >= REQUESTS_PER_DAY:
                    return message.text(text = f"主人, 今天的对话次数达到了上限, 明天再来哦")
                if timesToMin >= REQUESTS_PER_MIN:
                    return message.text(text = f"主人, 你的请求太过频繁, 请稍后再试哦")

                messages = [{"role": "user", "content": normalSetting}, {"role": "assistant", "content": "好的主人~小千夜为您服务"}]
                messages += user.readHistory(len = NORMAL_HISTORY_LEN, format = "dict_timeless")
                messages.append({"role": "user", "content": commandText})

        else:
            raise NameError("not me")
        
        #print(messages)
        
        # 获取回复
        text, code = self.siliconResponse(messages)
        allMsg = message.text(text)
        if code == 200:
            user.recordAdd(role = "user", msg = commandText)
            user.recordAdd(role = "assistant", msg = text)

        return allMsg

    ###############################################################################
    # Function:     siliconResponse  
    # Notice:
    ###############################################################################
    def siliconResponse(self, messages: list):
        '''从硅基流动服务器获取回复'''

        global PARALLEL_CONNECTION_NUM

        try:
            PARALLEL_CONNECTION_NUM += 1
            url = "https://api.siliconflow.cn/v1/chat/completions"
            
            payload = {
                "model": "deepseek-ai/DeepSeek-V3",
                "messages": messages,
                "stream": False,
                "max_tokens": 512,
                "stop": ["null"],
                "temperature": 0.7,
                "top_p": 0.7,
                "top_k": 50,
                "frequency_penalty": 0.5,
                "n": 1,
                "response_format": {"type": "text"},
            }

            headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "authorization": f"Bearer {SILICON_API_KEY}"
                }
            
            response = requests.post(url, json=payload, headers=headers, stream = False)

            # 获取回复消息返回
            if response.status_code == 200: 
                data = json.loads(response.content)
                return data["choices"][0]["message"]["content"], response.status_code
            elif response.status_code == 400:
                data = json.loads(response.content)
                logInfo(f'[siliconResponse]Request failed with status code: {response.status_code}, data: {data}')
                return f"主人, 遇到了400错误: {data["message"]}", response.status_code
            elif response.status_code == 401:
                data = json.loads(response.content)
                logInfo(f'[siliconResponse]Request failed with status code: {response.status_code}, data: {data}')
                return f"主人, 遇到了401错误: {data}", response.status_code
            elif response.status_code == 403:
                data = json.loads(response.content)
                logInfo(f'[siliconResponse]Request failed with status code: {response.status_code}, data: {data}')
                return f"主人, 遇到了404错误: {data}", response.status_code
            elif response.status_code == 429:
                data = json.loads(response.content)
                logInfo(f'[siliconResponse]Request failed with status code: {response.status_code}, data: {data}')
                return f"主人, 遇到了429错误: {data["message"]}", response.status_code
            elif response.status_code == 503:
                data = json.loads(response.content)
                logInfo(f'[siliconResponse]Request failed with status code: {response.status_code}, data: {data}')
                return f"主人, 遇到了503错误: {data["message"]}", response.status_code
            elif response.status_code == 504:
                data = json.loads(response.content)
                logInfo(f'[siliconResponse]Request failed with status code: {response.status_code}, data: {data}')
                return f"主人, 遇到了504错误: {data}", response.status_code
            else:
                data = json.loads(response.content)
                logInfo(f'[siliconResponse]Request failed with status code: {response.status_code}, data: {data}')
                return f"主人, 遇到了未知错误: {data}", response.status_code

        finally:
            PARALLEL_CONNECTION_NUM -= 1