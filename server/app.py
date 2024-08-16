# from flask import Flask, request, jsonify, make_response
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_cors import CORS
# app = Flask(__name__)
# CORS(app)  # 允许所有域名的跨域请求
#
# # 假设这是你的用户数据，通常应该从数据库读取
# users = {
#     'admin': {
#         'username': 'admin',
#         'password': generate_password_hash('admin123')  # 使用hash存储密码
#     }
# }
#
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#
#     if username not in users:
#         return make_response(jsonify({'error': 'Invalid username or password'}), 401)
#
#     user = users[username]
#     if not check_password_hash(user['password'], password):
#         return make_response(jsonify({'error': 'Invalid username or password'}), 401)
#
#     # 登录成功，可以返回一个token或者其他认证信息
#     token = "dummy_token"  # 通常这里会生成一个真实的token
#     return make_response(jsonify({'token': token}), 200)
#
# if __name__ == '__main__':
#     app.run(debug=True)