from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '36d4J0Ltp3lRtee9HDxY3K'

bootstrap = Bootstrap(app)

tasks = ['Task 1','Task 2','Task 3']

class LoginForm(FlaskForm):
    username = StringField('Username or email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')


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


@app.route('/home', methods=['GET','POST'])
def home():
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'tasks': tasks,
        'login_form': LoginForm()
    }
    return render_template('home.html', **context)


if __name__ == '__main__':
    app.run(debug=True)