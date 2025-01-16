from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_callback():
    try:
        # 获取请求体中的 JSON 数据
        data = request.get_json(force=True)
        print("Received data:", data)
        
        # 返回接收到的数据
        return jsonify(data), 200
    except Exception as e:
        # 处理可能的错误
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
