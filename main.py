from webapp import create_app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, current_user
import atexit
from webapp import db
from webapp.models import users, phone_challenge, laptop_challenge, server_challenge, points, leaderboard
from datetime import date, datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = create_app()

with app.app_context():
    def update_timeLeft(): 
        timeLeft = db.session.query(points.timeLeft).filter_by(user_id = current_user.id).first()
        lastActive = db.session.query(points.lastActive).filter_by(user_id = current_user.id).first()
        if timeLeft:
            lastActiveDate = lastActive[0]
            t = datetime.strptime(lastActiveDate, '%Y-%m-%d')
            t2 = datetime.now()
            delta = t-t2 
            timeChange = delta.seconds
            timeLeftSeconds = timeLeft[0]
            timeLeftNew = timeLeftSeconds - timeChange
            updateTime = points.query.get_or_404(current_user.id)
            updateTime.timeLeft = timeLeftNew
            updateTime.lastActive = t2.strftime()

scheduler = BackgroundScheduler()
scheduler.add_job(func = update_timeLeft, trigger="interval", seconds=10)


atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(debug=True)