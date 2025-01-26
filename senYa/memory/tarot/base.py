###############################################################################
#   File name:   tarot.py
#   Description: 处理塔罗牌抽取
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ...physics import message
from ..log import logInfo
from control import GRoot, json2dict

from pathlib import Path
from typing import Dict
import random

tarotCardPoolPath = GRoot / "senYa" / "memory" / "tarot" / "card"
tarotReplyRootPath = GRoot / "senYa" / "memory" / "tarot" / "guidence"
###############################################################################
# Class:        tarot     
# Notice:       
###############################################################################
class tarot:
    '''塔罗牌'''
    ###############################################################################
    # Function:     __init__
    # Notice:       
    ###############################################################################  
    def __init__(self, imagePath: Path):
        '''初始化一张塔罗牌'''
        if not imagePath.exists():
            raise FileNotFoundError(f"tarot card \"{imagePath}\" not found")

        self.imagePath = imagePath
        self.cardName = self.imagePath.stem

        # 找到解释路径
        self.explainPath = tarotReplyRootPath / f"{self.cardName}.json"
        if not self.explainPath.exists():
            raise FileNotFoundError(f"tarot card \"{self.explainPath}\" not found")

        self.ReplyDict: Dict[str, list] = json2dict(configPath = self.explainPath)

    ###############################################################################
    # Function:     draw
    # Notice:       
    ###############################################################################  
    def draw(self)->tuple[message.text, message.image, str]:
        '''抽取该塔罗牌'''

        # 随机获取正逆位
        upDown: str = random.choice(list(self.ReplyDict.keys()))

        # 解释和图片
        explainMsg = message.text(text = f"GUIDENCE: {random.choice(self.ReplyDict[upDown])}")   # 获取当前解释对象
        imaMsg = message.image(file = self.imagePath, upDown = upDown, subType = 0)

        return explainMsg, imaMsg, f"{self.cardName}_{upDown.upper()}"
    
###############################################################################
# Class:        tarotPool     
# Notice:       
###############################################################################
class tarotPool:
    '''塔罗牌卡池'''
    ###############################################################################
    # Function:     __init__
    # Notice:       
    ###############################################################################  
    def __init__(self, tarotCardPoolPath: Path):
        '''初始化塔罗牌卡池'''
        if not tarotCardPoolPath.exists():
            raise FileNotFoundError(f"tarot card \"{tarotCardPoolPath}\" not found")
        
        try:
            # 获取当前所有塔罗牌路径
            self.tarotList = [tarot(imagePath) for imagePath in tarotCardPoolPath.glob('*.png')]
        except Exception as e:
            logInfo(f"[tarotPool]init error:{str(e)}")
        else:
            logInfo(f"[tarotPool]init success, get card \"{len(self.tarotList)}\"")

    ###############################################################################
    # Function:     __init__
    # Notice:       
    ###############################################################################  
    def draw(self):
        '''从卡池中随机抽取一张塔罗牌返回'''
        return random.choice(self.tarotList).draw()

# bilibili幻星集塔罗牌卡池 
tarotPool2233 = tarotPool(tarotCardPoolPath = tarotCardPoolPath)