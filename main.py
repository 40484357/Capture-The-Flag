from webapp import create_app
from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, current_user
import atexit
from webapp import db
from webapp.models import users, phone_challenge, laptop_challenge, server_challenge, points, leaderboard
from datetime import date, datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = create_app()
@app.route('/')
def landing():
    user_points = db.session.query(points.pointsTotal).filter_by(id = current_user.id).first()
    user_time = db.session.query(points.timeLeft).filter_by(id = current_user.id).first()
    if user_points:
        userPoints = user_points[0]
        userTime = user_time[0]
    else:
        userPoints = 0 
        userTime = 86400
        new_user_points = points(id = current_user.id, pointsTotal = 0, timeLeft = 86400, lastActive = datetime.now())
        db.session.add(new_user_points)
        db.session.commit()
    id = current_user.id
    def update_timeLeft():
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
    
    atexit.register(lambda: scheduler.shutdown())
    return render_template('cyberescape.html', user = current_user, userPoints = userPoints, userTime = userTime)


if __name__ == '__main__':
    app.run(debug=True)

   