from flask import flash, redirect, render_template, session, url_for
from app.auth import auth
from app.forms import LoginForm


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        if login_form.password.data == '12345':
            flash('Successful sign up', category='success')
            return redirect(url_for('home'))
        else:
            flash('Authentication Error', category='danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html', **context)
