from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import Flaskform
from wtforms.fields import Stringfield, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar cafe', 'Enviar solicitud de compra', 'Entregar video a productor']


class LoginForm(Flaskform):
    username = Stringfield('Nombre de usuario', validaors=[DataRequired()])
    password = PasswordField('Password', validaors=[DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server(error):
    return render_template('500.html', error=error)


@app.route('/')
def index(): 
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    LoginForm = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form
    }

    return render_template('hello.html', **context)