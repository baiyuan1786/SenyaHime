###############################################################################
#   File name:   websocketserver.py
#   Description: websocket服务器类
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
import asyncio
import websockets
import json

from plugin.log import logInfo
from .api.account import *
from .api.contacts import *
from .api.user import *
from .api.message import *
from .api.file import *
from .api.shamrock import *
from .api.group import *
from .api.handle import *
from .api.resource import *
from .api.other import *
###############################################################################
# Class:        websocketserver     
# Input:        @name
#               @hostPort
#               @hostIP
#               @accessToken 
# Notice:       
###############################################################################
class websocketserver:
    '''使用websocket协议的shamrockbot服务器类'''
    def __init__(self, name: str, hostPort: int, hostIP: str, accessToken: str) -> None:
        self.name = name
        self.hostPort = hostPort
        self.hostIP = hostIP
        self.accessToken = accessToken  # 服务器访问shamrock的token 
        self.callback = None            # 用户定义的回调函数
        self.websocket = None

    ###############################################################################
    # Function:     receive
    # Input:        void     
    # Notice:       
    ##############################################################################
    def callbackDef(self, callbackFunc):
        '''定义回调函数'''
        if not asyncio.iscoroutinefunction(callbackFunc):
            raise ValueError("[websocketserver]callbackFunc must be async func")
        self.callback = callbackFunc

    ###############################################################################
    # Function:     handleConnection
    # Input:        void     
    # Notice:       启动 WebSocket 服务器
    ###############################################################################
    async def handleConnection(self, websocket: websockets.WebSocketServerProtocol):
        '''处理客户端连接的异步函数'''
        try:
            self.websocket = websocket
            logInfo(f"[websocketserver]New connection from {self.websocket.remote_address}")

            # 监听消息
            async for backMsgStr in self.websocket:
                logInfo(f"[websocketserver]Received: {backMsgStr}\n")
                if self.callback:
                    await self.callback(backMsgStr, self.websocket)
                else:
                    logInfo("[websocketserver]No callback defined, ignoring message\n")

        except websockets.exceptions.ConnectionClosed as e:
            logInfo(f"[websocketserver]Connection closed: {e}\n")
        except Exception as e:
            logInfo(f"[websocketserver]Error handling connection: {e}\n")

    ###############################################################################
    # Function:     _startServer
    # Input:        void     
    # Notice:       
    ##############################################################################         
    async def _startServer(self):
        '''异步启动服务器'''
        server = await websockets.serve(self.handleConnection, self.hostIP, self.hostPort)
        logInfo(f"[{self.name}]Running on ws://{self.hostIP}:{self.hostPort}")
        await server.wait_closed()
      
    ###############################################################################
    # Function:     run
    # Input:        void     
    # Notice:       
    ##############################################################################
    def run(self):
        '''运行服务器'''   
        asyncio.run(self._startServer())

    # 下面是shamrock客户端提供的API
    # account
    get_login_info = get_login_info             # 获取登录信息
    set_qq_profile = set_qq_profile             # 设置QQ信息
    get_model_show = get_model_show             # 获取机型信息

    # contacts
    get_stranger_info = get_stranger_info                           # 获取陌生人信息
    get_friend_list = get_friend_list                               # 获取好友列表
    get_unidirectional_friend_list = get_unidirectional_friend_list # 获取单向好友列表
    get_group_list = get_group_list                                 # 获取群列表
    get_group_member_info = get_group_member_info                   # 获取群的一个成员的信息
    get_group_member_list = get_group_member_list                   # 获取群成员列表
    get_group_honor_info = get_group_honor_info                     # 获取群荣誉信息
    get_group_system_msg = get_group_system_msg                     # 获取群组系统消息
    get_friend_system_msg = get_friend_system_msg                   # 获取好友系统消息
    get_essence_msg_list = get_essence_msg_list                     # 获取精华消息列表
    is_blacklist_uin = is_blacklist_uin                             # 判断是否在黑名单中

    # user
    delete_friend = delete_friend                                   # 删除好友
    delete_unidirectional_friend = delete_unidirectional_friend     # 删除单向好友
    send_like = send_like                                           # 主页点赞

    # message
    send_private_msg = send_private_msg                     # 发送私聊消息
    send_group_msg = send_group_msg                         # 发送群聊消息
    send_msg = send_msg                                     # 同时发送私聊群聊消息
    get_msg = get_msg                                       # 由ID获取某消息
    delete_msg = delete_msg                                 # 撤回消息
    get_history_msg = get_history_msg                       # 获取历史消息（同时群聊和私聊）
    get_group_msg_history = get_group_msg_history           # 获取群聊历史消息
    clear_msgs = clear_msgs                                 # 清除消息缓存
    get_forward_msg = get_forward_msg                       # 获取合并转发消息
    send_group_forward_msg = send_group_forward_msg         # 向某群聊发送合并消息
    send_private_forward_msg = send_private_forward_msg     # 向某私聊发送合并消息

    # resource
    get_image = get_image               # 获取图片,只能获得已缓存的图片
    can_send_image = can_send_image     # 判断是否可以发送图片
    ocr_image = ocr_image               # 图片 OCR
    can_send_record = can_send_record   # 检查是否可以发送语音
    get_record = get_record             # 获取语音
    get_file = get_file                 # 获取某文件

    # handle
    set_friend_add_request = set_friend_add_request # 处理加好友请求
    set_group_add_request = set_group_add_request   # 处理加群请求

    # group
    set_group_name = set_group_name                         # 设置群名
    set_group_portrait = set_group_portrait                 # 设置群头像
    set_group_admin = set_group_admin                       # 设置管理员
    set_group_card = set_group_card                         # 设置群成员名片
    set_group_remark = set_group_remark                     # 设置群备注
    set_group_special_title = set_group_special_title       # 设置群组专属头衔
    set_group_ban = set_group_ban                           # 禁言群组成员
    set_group_whole_ban = set_group_whole_ban               # 禁言全群
    set_essence_msg = set_essence_msg                       # 设置精华消息
    send_group_sign = send_group_sign                       # 群打卡
    send_group_notice = send_group_notice                   # 发送群公告
    get_group_notice = get_group_notice                     # 获取群公告
    set_group_kick = set_group_kick                         # 群组踢人
    set_group_leave = set_group_leave                       # 退出群组
    group_touch = group_touch                               # 群内戳一戳
    get_prohibited_member_list = get_prohibited_member_list # 获取被禁言成员列表
    get_group_at_all_remain = get_group_at_all_remain       # 获取群 @全体成员 剩余次数
    set_group_comment_face = set_group_comment_face         # 设置消息底部评论小表情(可能无效)

    # file
    upload_private_file = upload_private_file               # 上传私聊文件
    upload_group_file = upload_group_file                   # 上传群文件
    delete_group_file = delete_group_file                   # 删除群文件
    create_group_file_folder = create_group_file_folder     # 创建群文件文件夹
    rename_group_folder = rename_group_folder               # 重命名群文件夹
    delete_group_folder = delete_group_folder               # 删除群文件夹
    get_group_file_system_info = get_group_file_system_info # 获取群文件系统信息,例如文件总数,已使用空间
    get_group_root_files = get_group_root_files             # 获取群根目录文件列表
    get_group_files_by_folder = get_group_files_by_folder   # 获取群子目录文件列表
    get_group_file_url = get_group_file_url                 # 获取群文件资源链接

    # shamrock
    switch_account = switch_account                         # 切换当前shamrockQQ号
    upload_file = upload_file                               # 上传文件到缓存目录,输入的file是文件路径
    download_file = download_file                           # Shamrock下载文件到缓存目录
    clean_cache = clean_cache                               # 清除当前shamrock缓存
    get_device_battery = get_device_battery                 # 获取手机电池信息
    get_start_time = get_start_time                         # 获取Shamerock启动时间
    log = log                                               # 获取Shamrock日志
    shut = shut                                             # 关闭Shamrock
    get_supported_actions = get_supported_actions           # 获取所有支持的动作

    # other
    get_weather_city_code = get_weather_city_code           # 获取城市ADCode
    get_weather = get_weather                               # 获取天气
    upload_group_image = upload_group_image                 # 上传群图片,注意该接口是上传群消息的图片，不是群文件，也不是群相册
    get_cookies = get_cookies                               # 获取 Cookie
    get_csrf_token = get_csrf_token                         # 获取 CSRF 令牌
    get_credentials = get_credentials                       # 获取 Cookie 与 CSRF 令牌