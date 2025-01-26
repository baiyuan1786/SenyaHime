###############################################################################
#   File name:   cardPool.py
#   Description: 卡池定义文件
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .. import logInfo
import json
import numpy as np
import random
from control import GRoot
initCardPool = GRoot / "senYa" / "memory" /  "propCardPool" / "qianyeServicePool_init.json"
stateCardPool = GRoot / "senYa" / "memory" /  "propCardPool" / "qianyeServicePool_state.json"
###############################################################################
# Class:        card
# Description:  定义一个卡片类
# Input:        name
# Return:       
# Notice:       
###############################################################################
class card:
    ###############################################################################
    # Function:     __init__
    # Description:  初始化一个卡片类
    # Input:        @name:      卡片名称
    #               @weight:    卡片权重
    #               @quantity:  卡片数量
    # Return:       
    # Notice:       
    ###############################################################################
    def __init__(self, name : str, weight : int, quantity : int, weightEquelToNum : bool = False) -> None:
        if weight < 0:
            raise ValueError(f"[card]get Err weight \"{weight}\"")
        if quantity < 0:
            raise ValueError(f"[card]get Err quantity \"{quantity}\"")

        self.name = name
        self.quantity = quantity
        self.weight = quantity if weightEquelToNum else weight
        self.weightEquelToNum = weightEquelToNum

    ###############################################################################
    # Function:     draw
    # Description:  抽取一张卡
    # Input:        None
    # Return:       @self.name: 卡片名
    # Notice:       
    ###############################################################################
    def draw(self):
        if self.quantity <= 0:
            raise TypeError(f"[card] card \"{self.name}\" is empty")

        self.quantity = self.quantity - 1
        self.weight = self.quantity if self.weightEquelToNum else self.weight
        #logInfo(f"[{self.name}]当前卡片剩余数量{self.quantity}")
        return self.name

###############################################################################
# Class:        cardPool
# Description:  定义一个卡池类
# Input:        name
# Return:       
# Notice:       
###############################################################################
class cardPool:
    ###############################################################################
    # Function:     __init__
    # Description:  初始化一个卡池类
    # Input:        @name:      卡池名称
    #               @stateFile: 卡池当前状态描述文件
    # Return:       
    # Notice:       
    ###############################################################################
    def __init__(self, name : str, stateFile : str) -> None:
        self.name = name
        self.stateFile = stateFile
        self.reInit(stateFile)

    ###############################################################################
    # Function:     reInit
    # Description:  重新初始化一个卡池类
    # Input:        @initFile:  卡池初始化文件
    # Return:       
    # Notice:       
    ###############################################################################
    def reInit(self, initFile):
        
        with open(initFile, "r", encoding = "utf-8") as file:
            cardPoolData = json.load(file)

        # 初始化卡片列表
        self.cardList = [card(obj["name"], obj["weight"], obj["quantity"], cardPoolData["weightEquelToNum"]) \
                         for obj in cardPoolData["cardPool"]]
        self.save()

    ###############################################################################
    # Function:     save
    # Description:  保存抽卡结果
    # Input:        void
    # Return:       
    # Notice:       
    ###############################################################################   
    def save(self):
        cardSaveList = [{"name" : obj.name, "quantity" : obj.quantity, "weight" : obj.weight} for obj in self.cardList]
        with open(self.stateFile, "r", encoding = "utf-8") as file:
            cardPoolData = json.load(file)
            cardPoolData["cardPool"] = cardSaveList

        with open(self.stateFile, "w", encoding = "utf-8") as file:
            json.dump(cardPoolData, file, indent = 4)

    ###############################################################################
    # Function:     drawCard
    # Description:  抽卡
    # Input:        None
    # Return:       @cardName:      抽到的卡
    # Notice:       
    ###############################################################################
    def drawCard(self):
        # 过滤卡列表
        validCardList = [obj for obj in self.cardList if obj.quantity > 0]
        if not validCardList:
            logInfo(f"[{self.name}]卡池为空，请重置卡池")
            return "空白卡"

        # 获取抽卡随机数
        weightList = [obj.weight for obj in validCardList]
        cumulativaWeights = [np.sum(weightList[0 : i + 1]) for i, weight in enumerate(weightList)]
        randomIndex = random.uniform(0, cumulativaWeights[-1])

        # 抽卡
        for i, cumulativeWeight in enumerate(cumulativaWeights):
            if randomIndex < cumulativeWeight:
                drawCardName = validCardList[i].draw()
                break

        # 保存抽卡结果
        self.save()

        logInfo(f"[{self.name}]get card \"{drawCardName}\", 该卡片剩余数量 \"{validCardList[i].quantity}\"张")
        return drawCardName

    ###############################################################################
    # Function:     stateInfo
    # Description:  展示当前卡池状态
    # Input:        None
    # Return:       @cardName:      抽到的卡
    # Notice:       
    ###############################################################################
    def stateInfo(self):
        info = f"好，当前卡池\"{self.name}\"状态如下:\n"
        for index, obj in enumerate(self.cardList):
            info += f"{index + 1}: 卡片\"{obj.name}\", 剩余 {obj.quantity} 张\n"

        return info
    
cardPooltest = cardPool(name = "千夜姬测试卡池", stateFile = stateCardPool)
        