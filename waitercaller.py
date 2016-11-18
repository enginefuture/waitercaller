from flask import Flask
from flask import request
from flask import render_template
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from mockdbhelper import MockDBHelper as DBHelper
from flask import redirect
from flask import url_for
from user import User


DB = DBHelper()
app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = "IT2x6U9MyLoA9xAcxfwem4FLy/8NM73Js9kG3W64qxP/l0Yl+4Ykmhecxbu\
wE4436H0hRQXUJSK+B4iOrych7DkGZxuBtTP8Niz"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/account')
@login_required
def account():
    return "You are fuck logged in!"


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user_password = DB.get_user(email)
    if user_password and user_password == password:
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()


@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
