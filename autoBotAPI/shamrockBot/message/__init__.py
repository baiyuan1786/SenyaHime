###############################################################################
#   File name:   __init__.py
#   Description: 整理所有消息接口
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from .msgSeg.base import messageSegment
from .msgSeg.common import at, face, bubble_face, reply, text, markDown
from .msgSeg.media import image, record, video
from .msgSeg.special import new_dice, basketball, new_rps, poke, touch ,music, weather, gift

from .callback.base import callbackmsg