from flask import Blueprint, render_template, request, redirect, url_for, flash
import hashlib, random
passwords = []
with open('CaptureTheFlag\webapp\static\cyberA-Z.txt') as f:
    passwords = f.readlines()

passLength = len(passwords) - 1
selection = random.randint(0, passLength)
selected = passwords[selection]
password = hashlib.sha256(selected.encode())  

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    passLength = len(passwords) - 1
    selection = random.randint(0, passLength)
    selected = passwords[selection]
    password = hashlib.sha256(selected.encode())
    print(password.hexdigest())
    print(passLength)
    return render_template('cyberescape.html')

@views.route('/laptop', methods=['GET', 'POST'])
def laptop():
    print(selected)
    response = None
    if request.method=='POST':
        if request.form['answer'] != selected:
            response = 'wrong password, try again'
            flash(response)
        else:
            response = 'correct password'
            flash(response)
            
    return render_template('laptop.html',password = password.hexdigest(), response = response)
    

