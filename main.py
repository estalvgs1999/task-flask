from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '36d4J0Ltp3lRtee9HDxY3K'

bootstrap = Bootstrap(app)

tasks = ['Task 1','Task 2','Task 3']

@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('error/500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/home'))
    session['user_ip'] = user_ip
    return response


@app.route('/home')
def home():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'tasks': tasks
    }
    return render_template('home.html', **context)


if __name__ == '__main__':
    app.run(debug=True)