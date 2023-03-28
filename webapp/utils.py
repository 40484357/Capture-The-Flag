from datetime import date, datetime
from . import db
from flask_login import current_user
from .models import users, phone_challenge, laptop_challenge, server_challenge, points


def timeChange(startTime):
    currTime = datetime.now()
    convertedTime  = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S.%f')
    timePassed = currTime - convertedTime
    timePassedS = timePassed.seconds

    return timePassedS



def pointsLogic(challenge):
    

    hintsUsed = db.session.query(challenge.hints).filter_by(user_id = current_user.id).first()
    time = db.session.query(challenge.startTime).filter_by(user_id = current_user.id).first()
    totalPoints= db.session.query(points.pointsTotal).filter_by(id = current_user.id).first() 
    
    basePoints = 50
    #timeTaken = timeChange(userTime)
    timeTaken = timeChange(time[0])
    penalty = 0
    
    if(timeTaken > 300 and timeTaken < 1200):
         penalty += 10
    elif (timeTaken > 1200):
        penalty += 20
    if(hintsUsed[0] == 1):
            penalty += 10
    elif(hintsUsed[0] >= 2):
        penalty += 20

    basePoints -= penalty

    newPoints = totalPoints[0] + basePoints
    return(newPoints)
