###############################################################################
#   File name:   main.py
#   Description: 主函数文件
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from senYa import SenYaHime
from control import *

if __name__ == "__main__":
    SenYa = SenYaHime(name = BOT_NAME, clientPort = BOT_CLIENT_ACTIVE_HTTP_PORT,\
                         hostPort = BOT_HOST_HTTP_LISTEN_PORT,clientIP = BOT_CLIENT_IP,\
                              hostIP = BOT_HOST_IP, accessToken = BOT_ACCESSTOKEN, protocol = BOT_PROTOCOL)
    SenYa.run()