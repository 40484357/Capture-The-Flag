from flask import Blueprint, render_template, request, redirect, url_for
import hashlib, random

passwords = ['crypto', 'desktop', 'hash', 'cipher', 'caeser', 'pigpen', 'ethereum']

    

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    passLength = len(passwords)
    selection = random.randint(0, passLength)
    selected = passwords[selection]
    password = hashlib.md5(selected.encode())
    print(password.hexdigest())
    return render_template('cyberescape.html')

    