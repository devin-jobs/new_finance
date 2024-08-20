from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
app = Flask(__name__)
# 允许所有域名的跨域请求
CORS(app)


# 假设这是你的用户数据，通常应该从数据库读取
users = {
    'admin': {
        'username': 'admin',
        'password': generate_password_hash('admin123')  # 使用hash存储密码
    }
}

@app.route('/', methods=['POST'])# 定义一个路由，处理POST请求，路径为'/'
def login(): # 定义登录视图函
    data = request.get_json()   # 从POST请求的body中解析JSON数据
    username = data.get('username') # 从JSON数据中获取'username'键对应的值
    password = data.get('password')

    if username not in users: # 检查用户名是否存在于用户字典中 如果不存在，则构建一个HTTP响应
        return make_response(jsonify({'error': '不存在这个用户，请联系管理员'}), 401)

    user = users[username]
    if not check_password_hash(user['password'], password):
        return make_response(jsonify({'error': '别输了，没有人知道答案'}), 401)

    # 登录成功，可以返回一个token或者其他认证信息
    token = "dummy_token"  # 通常这里会生成一个真实的token
    return make_response(jsonify({'token': token}), 200)

if __name__ == '__main__':
    app.run(debug=True)