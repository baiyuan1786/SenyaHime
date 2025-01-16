###############################################################################
#   File name:   main.py
#   Description: 主函数文件
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from mainLogic.senyaHime import SenYaHime

# adb命令: adb forward tcp:5700 tcp:5700
# adb forward --list
# adb connect 127.0.0.1:16384
# http://192.168.0.108:5700/get_login_info?access_token=guzhaoqiaoqiaoa1
# http://127.0.0.1:5700/send_group_msg?access_token=guzhaoqiaoqiaoa1&group_id=606490627&message=%E6%B5%8B%E8%AF%95%E6%B6%88%E6%81%AF2

BOT_NAME = "SenyaHime"
BOT_CLIENT_ACTIVE_HTTP_PORT = 5700  # 客户端主动HTTP端口
BOT_HOST_HTTP_LISTEN_PORT = 5700    # 服务器端监听端口
BOT_HOST_IP = "192.168.0.106"       # 服务器端IP
BOT_ACCESSTOKEN = "guzhaoqiaoqiaoa1"# 鉴权密钥
        
if __name__ == "__main__":
    SenYa = SenYaHime(name = BOT_NAME, clientPort = BOT_CLIENT_ACTIVE_HTTP_PORT,\
                         hostPort = BOT_HOST_HTTP_LISTEN_PORT, hostIP = BOT_HOST_IP, accessToken = BOT_ACCESSTOKEN)
    SenYa.run()