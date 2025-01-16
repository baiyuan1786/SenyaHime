from plugin.cardPool import cardPool
from path import GRoot
import os


if __name__ == "__main__":
    initCardPool = os.path.join(GRoot, "doc", "cardPool", "qianyeServicePool_init.json")
    stateCardPool = os.path.join(GRoot, "doc", "cardPool", "qianyeServicePool_state.json")
    qianyePool = cardPool("千夜酱测试卡池", stateCardPool)
    qianyePool.reInit(initCardPool)

    for i in range(50):
        qianyePool.drawCard()