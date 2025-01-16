###############################################################################
#   File name:   user.py
#   Description: 用户相关API
#   Authors:     BaiYuan <395642104@qq.com>
###############################################################################
from ..url import shamrockURL
###############################################################################
# Function:     delete_friend
# Input:        @user_id 用户ID    
# Notice:       
###############################################################################
def delete_friend(self, user_id: int):
    '''shamrockAPI, 删除好友'''
    raise TypeError("shamrock暂未实现该API")
    url = shamrockURL(self.baseURL, self.accessToken, "/delete_friend")
    url.argAdd("user_id", user_id)

    return url.get()

###############################################################################
# Function:     delete_unidirectional_friend
# Input:        @user_id 用户ID    
# Notice:       
###############################################################################
def delete_unidirectional_friend(self, user_id: int):
    '''shamrockAPI, 删除单向好友'''
    raise TypeError("shamrock暂未实现该API")
    url = shamrockURL(self.baseURL, self.accessToken, "/delete_unidirectional_friend")
    url.argAdd("user_id", user_id)

    return url.get()

###############################################################################
# Function:     send_like
# Input:        @user_id 用户ID
#               @times 点赞次数    
# Notice:       
###############################################################################
def send_like(self, user_id: int, times: int):
    '''shamrockAPI, 点赞资料卡'''
    url = shamrockURL(self.baseURL, self.accessToken, "/send_like")
    url.argAdd("user_id", user_id)
    url.argAdd("times", times)

    return url.get()