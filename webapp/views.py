from flask import Blueprint, render_template, request, redirect, url_for
import hashlib, random

passwords = ['crypto', 'desktop', 'hash', 'cipher', 'caeser', 'pigpen', 'ethereum']

    

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template('cyberescape.html')

@views.route('/laptop')
def laptop():
    passLength = len(passwords) - 1
    selection = random.randint(0, passLength)
    selected = passwords[selection]
    password = hashlib.sha256(selected.encode())
    return render_template('laptop.html',password = password.hexdigest())
    