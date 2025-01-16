import requests

# Flask 服务器的地址
url = 'http://localhost:8888/callback'

# 要发送的数据
data = {
    "message": "Hello, Flask!",
    "number": 123,
    "status": True
}

# 发送 POST 请求
response = requests.post(url, json=data)

# 打印服务器的响应
print(f"Response Status Code: {response.status_code}")
print(f"Response Data: {response.json()}")
