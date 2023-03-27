from webapp import create_app
from flask import render_template, redirect, url_for, request, Markup
from flask_login import login_user, login_required, current_user
import atexit
from webapp import db
from webapp.models import users, phone_challenge, laptop_challenge, server_challenge, points
from datetime import date, datetime
from apscheduler.schedulers.background import BackgroundScheduler
from webapp.utils import timeChange

app = create_app()

constructKeyValidator = '<div id="keyValidator" onClick="goToKey()"><svg width="229" height="337" viewBox="0 0 229 337" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1 1H228V336H1V1Z" fill="#A57939"/><path d="M38.8335 32.6017H190.167V133.734H38.8335V32.6017ZM38.8335 228.546H190.167V298.071H38.8335V228.546Z" fill="#6A462F"/><path d="M1 1H228V336H1V1Z" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linejoin="round"/><path d="M196.472 184.3C205.179 184.3 212.236 178.64 212.236 171.657C212.236 164.675 205.179 159.014 196.472 159.014C187.766 159.014 180.708 164.675 180.708 171.657C180.708 178.64 187.766 184.3 196.472 184.3Z" fill="black"/><path d="M199.625 203.265H193.319C191.647 203.265 190.043 202.611 188.861 201.448C187.678 200.284 187.014 198.707 187.014 197.061V158.902C187.014 157.257 187.678 155.679 188.861 154.516C190.043 153.352 191.647 152.698 193.319 152.698H199.625C201.297 152.698 202.901 153.352 204.083 154.516C205.266 155.679 205.93 157.257 205.93 158.902V197.055C205.93 198.7 205.266 200.278 204.083 201.442C202.901 202.605 201.297 203.265 199.625 203.265Z" fill="black"/><path d="M38.8335 32.6017H190.167V133.734H38.8335V32.6017ZM38.8335 228.546H190.167V298.071H38.8335V228.546Z" stroke="black" stroke-width="2" stroke-miterlimit="10" stroke-linejoin="round"/></svg>'

@app.route('/cyberescape')
def landing():
    user_points = db.session.query(points.pointsTotal).filter_by(id = current_user.id).first()
    startGameTime = db.session.query(points.startGameTime).filter_by(id = current_user.id).first()
    laptopChallenge = db.session.query(laptop_challenge.challengeState).filter_by(user_id = current_user.id).first()
    phoneChallenge = db.session.query(phone_challenge.challengeState).filter_by(user_id = current_user.id).first()
    serverChallenge = db.session.query(server_challenge.challengeState).filter_by(user_id = current_user.id).first()
    if user_points:
        userPoints = user_points[0]
        startTime = startGameTime[0]
        timePassed = timeChange(startTime)
        timeLeft = 86400 - timePassed
        userTimeChange = points.query.get_or_404(current_user.id)
        userTimeChange.timeLeft = timeLeft
        db.session.commit()
    else:
        userPoints = 100
        timeLeft = 86400
        new_user_points = points(id = current_user.id, pointsTotal = 0, startGameTime = datetime.now())
        db.session.add(new_user_points)
        db.session.commit()

    if(laptopChallenge and phoneChallenge and serverChallenge):
        if(laptopChallenge[0] == 4 and phoneChallenge[0] == 3 and serverChallenge[0] == 4):
            keyValidator = Markup(constructKeyValidator)
            return render_template('cyberescape.html', user=current_user, userPoints = userPoints, userTime = timeLeft, keyValidator = keyValidator)
    id = current_user.id
    """def update_timeLeft():
        with app.app_context():
            print(id)
            timeLeft = db.session.query(points.timeLeft).filter_by(id = id).first()
            lastActive = db.session.query(points.lastActive).filter_by(id = id).first()
            print(timeLeft)
            print(lastActive)
            if timeLeft:
                lastActiveDate = lastActive[0]
                t = datetime.strptime(lastActiveDate, '%Y-%m-%d %H:%M:%S.%f')
                t2 = datetime.now()
                delta = t2-t 
                timeChange = delta.seconds
                timeLeftSeconds = timeLeft[0]
                timeLeftNew = timeLeftSeconds - timeChange
                updateTime = points.query.get_or_404(id)
                updateTime.timeLeft = timeLeftNew
                updateTime.lastActive = t2
                db.session.commit()
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(func = update_timeLeft, trigger="interval", seconds=10)

    scheduler.start()
    
    atexit.register(lambda: scheduler.shutdown())"""
    return render_template('cyberescape.html', user = current_user, userPoints = userPoints, userTime = timeLeft)


if __name__ == '__main__':
    app.run(debug=True)

   