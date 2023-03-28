from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import users
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import random
auth = Blueprint('auth', __name__)

with open(r'webapp\static\usernames.txt') as l:
    words = l.readlines()
    usernames = [x.strip().lower() for x in words]

def selectUsername():
    usernameLen = len(usernames) -1
    selection = random.randint(0, usernameLen)
    username = usernames[selection]
    return username

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = users.query.filter_by(email=email).first()
       
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('landing'))
            else:
                flash('incorrect password', category='error')
        else:
            flash('email does not exist', category='error')
    return render_template("login.html")

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        username = selectUsername()
        user = users.query.filter_by(email=email).first()
        usernameCheck = users.query.filter_by(user_name = username)

        if usernameCheck:
            number = usernameCheck.length + 1
            newUsername = username + number
            username = newUsername
        elif user:
            flash('email already exists.', category='error')
        elif len(email) < 8:
            flash('Email must be greater than 7 characters', category='error')
            pass
        elif len(password) < 7:
            flash('Password must be greater than 7 characters', category='error')
            pass
        elif password != password2:
          flash('Passwords don\'t match', category='error')
          pass
        else:
            new_user = users(email=email, password=generate_password_hash(password, method='sha256'), user_name = username)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
            login_user(new_user, remember=True) 
            return redirect(url_for('landing'))


    return render_template("register.html")