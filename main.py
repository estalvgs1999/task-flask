from app import create_app
from flask import request, make_response, redirect, render_template, session, url_for, flash

import unittest
from app import create_app
from app.forms import LoginForm

app = create_app()

tasks = ['Task 1','Task 2','Task 3']




@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('error/404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('error/500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/login'))
    session['user_ip'] = user_ip
    return response


@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    user_ip = session.get('user_ip')
    context = {
        'login_form': login_form,
        'user_ip': user_ip,
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        
        if auth(login_form):
            flash('Successful sign up', category='success')
            return redirect(url_for('home'))
        else:
            flash('Authentication Error', category='danger')
            return redirect(url_for('login'))
    
    return render_template('login.html', **context)


@app.route('/home')
def home():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'tasks': tasks,
        'login_form': login_form,
        'username': username
    }

    if username:
        return render_template('home.html', **context)
    return make_response(redirect('/login'))


def auth(login):
    return login.password.data == '12345'


if __name__ == '__main__':
    app.run(debug=True)