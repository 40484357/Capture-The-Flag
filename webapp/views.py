from flask import Blueprint, render_template, request, redirect, url_for, flash
import hashlib, random, time, math
from . import db
from flask_login import login_user, login_required, current_user
from .models import users, phone_challenge, laptop_challenge, server_challenge, points
from datetime import date, datetime
from .utils import timeChange
from flask import Blueprint, render_template, request, redirect, url_for, flash, Markup
import hashlib, random, time
passwords = []
with open('CaptureTheFlag\webapp\static\cyberA-Z.txt') as f:
    words = f.readlines()
    passwords = [x.strip().lower() for x in words]


# Diffie-Hellman Key Exchange start
N = 604931 
G = 30672

# List of potential a and b values
possibleValues = [503, 521, 541, 557, 563, 613, 631, 641, 653, 661]
    
# Need to select two random unique values from the list
possibleValuesLength = len(possibleValues) - 1
primeSelection1 = random.randint(0, possibleValuesLength)
prime1 = possibleValues[primeSelection1]

# Remove the first value from the list and decrease the length of the list by 1
possibleValues.pop(primeSelection1)
possibleValuesLength -= 1

# Select the second value from the list
primeSelection2 = random.randint(0, possibleValuesLength)
prime2 = possibleValues[primeSelection2]
    
a = prime1 #variable
b = prime2 #variable
A = pow(G,a) % N
B = pow(G,b) % N
secretKey = pow(B,a) % N
print("A: ", A)
print("B: ", B)
print("Secret Key: ", secretKey)

views = Blueprint('views', __name__)

def pointsLogic(timeLeft, hintsUsed, userTime, totalPoints):
    basePoints = 50
    #timeLPenalty = (24 - round(timeLeft /3600))*500
    timeTaken = timeChange(userTime)
    timeTPenalty = timeTaken * 0.005
    hintPenalty = 0
    if(hintsUsed > 0):
        hintPenalty = basePoints - ((basePoints-timeTPenalty) * (1-(hintsUsed * 0.08)))
    finalPoints = basePoints - (hintPenalty + timeTPenalty)
    newPoints = math.ceil(totalPoints + finalPoints)
    return(newPoints)



@views.route('/laptop', methods=['GET', 'POST'])
def laptop():
    #database query for passkey, if it exists then that is the passkey otherwise generate and store new passkey
    passkey = db.session.query(laptop_challenge.laptopPassword).filter_by(user_id = current_user.id).first()
    challengeState = db.session.query(laptop_challenge.challengeState).filter_by(user_id = current_user.id).first()
    #checks challenge state, if it's 2 it will redirect the user to second challenge
    if challengeState:
        if challengeState[0] > 1:
            return redirect('/desktop')
    
    if passkey:
        print(passkey)
        selected = passkey[0]
        password = hashlib.md5(passkey[0].encode())
        
        print(password.hexdigest())
    else:
        passLength = len(passwords) - 1
        selection = random.randint(0, passLength) 
        selected = passwords[selection]
        password = hashlib.md5(selected.encode())
        beginTime = datetime.now()
        new_password = laptop_challenge(user_id = current_user.id, challengeState = 1, laptopPassword = selected, hints = 0, startTime = beginTime)
        db.session.add(new_password)
        db.session.commit()
        print(password.hexdigest())

    response = None
    if request.method=='POST':
        if request.form['answer'] != selected:
            response = 'wrong password, try again'
            flash(response)
        else:
            userChallenge = laptop_challenge.query.get_or_404(current_user.id)
            print(userChallenge.challengeState)
            userChallenge.challengeState = 2
            userPoints = points.query.get_or_404(current_user.id)
            timeLeft = db.session.query(points.timeLeft).filter_by(id = current_user.id).first()
            hintsUsed = db.session.query(laptop_challenge.hints).filter_by(user_id = current_user.id).first()
            time = db.session.query(laptop_challenge.startTime).filter_by(user_id = current_user.id).first()
            totalPoints= db.session.query(points.pointsTotal).filter_by(id = current_user.id).first()

            newPoints = pointsLogic(timeLeft[0], hintsUsed[0],time[0], totalPoints[0])
            userPoints.pointsTotal = newPoints #add new points total to DB
            db.session.commit()
            return redirect('/desktop')
            
    return render_template('laptop.html',password = password.hexdigest(), response = response)
    
@views.route('/desktop', methods=['GET', 'POST'])
def desktop():
    ip = "85.50.46.53"
    completed = 'false'
    userChallenge = laptop_challenge.query.get_or_404(current_user.id)
    challengeStateCheck = db.session.query(laptop_challenge.challengeState).filter_by(user_id = current_user.id).first()
    if(challengeStateCheck[0] == 1):
        return redirect('/laptop')
    elif(challengeStateCheck[0] == 3):
        return redirect('/')
    else:
        userChallenge.hints = 0
        userChallenge.startTime = datetime.now()
        db.session.commit()

    response = None
    if request.method == 'POST':
        if request.form['answer'] != ip:
            response = 'not quite try again'
            flash(response)
            return render_template('desktop.html', response = response)
            
        else:
            response = "That's the IP, but where does it go? " + ip
            completed = 'true'
            flash(response)
            return render_template('desktop.html', response = response, completed = completed)

    return render_template('desktop.html', completed = completed)


@views.route('/phone', methods=['GET', 'POST'])
def phone():
    response = None
    primeA = db.session.query(phone_challenge.phonePrime1).filter_by(user_id = current_user.id).first()
    primeB = db.session.query(phone_challenge.phonePrime2).filter_by(user_id = current_user.id).first()

    if primeA:
        a = primeA[0] #variable
        b = primeB[0] #variable
        A = pow(G,a) % N
        B = pow(G,b) % N
        secretKey = pow(B,a) % N
        print("A: ", A)
        print("B: ", B)
        print("Secret Key: ", secretKey)
    else: 
        # Need to select two random unique values from the list
        possibleValuesLength = len(possibleValues) - 1
        primeSelection1 = random.randint(0, possibleValuesLength)
        prime1 = possibleValues[primeSelection1]

        # Remove the first value from the list and decrease the length of the list by 1
        possibleValues.pop(primeSelection1)
        possibleValuesLength -= 1

        # Select the second value from the list
        primeSelection2 = random.randint(0, possibleValuesLength)
        prime2 = possibleValues[primeSelection2]
            
        a = prime1 #variable
        b = prime2 #variable
        A = pow(G,a) % N
        B = pow(G,b) % N
        secretKey = pow(B,a) % N
        print("A: ", A)
        print("B: ", B)
        print("Secret Key: ", secretKey)
        new_phone_challenge = phone_challenge(user_id = current_user.id, challengeState = 1, phonePrime1 = a, phonePrime2 = b, hints = 0 )
        db.session.add(new_phone_challenge)
        db.session.commit()
    if request.method=='POST':
        secretKeyGuess=request.form.get('answer', type=int)
        #secretKeyGuess = int(request.form['answer'])
        if secretKeyGuess != secretKey:
            response = 'wrong password, try again'
            flash(response)
        else:
            # Redirect to the next page
            return redirect(url_for('views.phoneHome'))
            
    return render_template('phone.html',password = secretKey,a=a,b=b, response = response)

@views.route('/server')
def server():
    return render_template('server.html')


@views.route('/wcg', methods = ['GET', 'POST'])
def wcg():
    response = None
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            if request.form['password'] == 'IloveWickedGames2023':
                return redirect('/login_wcg')
            else: 
                response = 'wrong password'
        else: 
            response = 'wrong username'
            flash(response)
            return render_template('wickedcybergames.html', response = response)


    return render_template('wickedcybergames.html')

@views.route('/login_wcg')
def login_wcg():
    flag = 'FLAG = ROBOTS'
    return render_template('login_wcg.html', flag = flag)
@views.route('/phoneHome',methods =['GET','POST'])
def phoneHome():
    response = None
    if request.method=='POST':
        if request.form['password'] != "check_user.php":
            response = 'Incorrect password'
            flash(response)
        else:
            response = Markup("Correct. Now use it <a href ='http://52.1.222.178:8000'>here</a>")
            flash(response)
    return render_template('phoneHome.html')


"""@views.route('/Points_Logic', methods=['GET', 'POST'])
def points():
    response=None
    if request.method=='POST':
        timeLeft=request.form.get('timeLeft',type=int)
        hintsUsed=request.form.get('hintsUsed',type=int)
        timeTaken=request.form.get('timeTaken',type=int)
        basePoints=25000
        timeLPenalty = (24 - timeLeft)*500
        hintPenalty = basePoints - ((basePoints-timeLPenalty) * (1-(hintsUsed * 0.08)))
        timeTPenalty = timeTaken *0.03

        points = basePoints - (timeLPenalty + hintPenalty + timeTPenalty)

        response = points

        flash(response)
        
    return render_template('Points_Logic.html', response= response)"""
