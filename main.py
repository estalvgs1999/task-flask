from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/home'))
    response.set_cookie('user_ip',user_ip)
    return response


@app.route('/home')
def home():
    user_ip = request.cookies.get('user_ip')
    return render_template('home.html', user_ip=user_ip)


if __name__ == '__main__':
    app.run(debug=True)