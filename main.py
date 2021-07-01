from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    user_ip = request.remote_addr
    return f'Hello World! Your Ip:{user_ip}'

if __name__ == '__main__':
    app.run(debug=True)