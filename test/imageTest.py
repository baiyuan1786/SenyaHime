import base64
###############################################################################
# Function:    image_to_base64
# Input:       @image_path (str) - 图片文件的路径
# Notice:      支持常见的图片格式，如 JPG、PNG 等
###############################################################################
def imageToBase64(image_path: str) -> str:
    '''将本地的一张图片转换为base64格式'''

    with open(image_path, "rb") as image_file:
        # 读取图片文件并进行 Base64 编码
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return r"base64://" + encoded_string
    
path = r"D:\Task\004_JujoHotaru头像\Snipaste_2025-01-04_21-14-09.png"

encoded_string = imageToBase64(path)

print(f"转换出的字符串为: \"{encoded_string}\"")