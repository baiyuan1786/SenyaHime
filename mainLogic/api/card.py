###############################################################################
#   File name:   card.py
#   Description: 描述关于抽卡的接口
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from path import initCardPool, stateCardPool

###############################################################################
# Function:     drawCard
# Input:        void    
# Notice:       
###############################################################################    
def drawCard(self, data):
    '''千夜机器人的抽卡API'''
    card = self.qianyePool.drawCard()
    message = f"收到，恭喜你抽中了 \"{card}\" 一张"
    self.reply(data, message)

###############################################################################
# Function:     reInitCardPool
# Input:        void  
# Notice:       
###############################################################################  
def reInitCardPool(self, data):
    '''千夜机器人的重置卡池API'''
    self.qianyePool.reInit(initFile = initCardPool)
    message = "好的哦，重置卡池成功"
    self.reply(data, message)