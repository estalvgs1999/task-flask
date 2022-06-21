from flask import render_template
from app.auth import auth
from app.forms import LoginForm


@auth.route('/login')
def login():
    context = {
        'login_form': LoginForm()
    }

    return render_template('login.html', **context)
