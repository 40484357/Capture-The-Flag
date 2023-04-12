from . import db
from flask_login import UserMixin
from datetime import datetime, date

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(1000))
    admin = db.Column(db.String(100))
    lecturerStatus = db.Column(db.Integer)
    lecturerId = db.Column(db.Integer, unique=True)
    lecturerCode = db.Column(db.Integer)
    email = db.Column(db.String(1000), unique=True)
    points = db.relationship('points')
    #leaderBoard = db.relationship('leaderboard')
    laptop_challenge = db.relationship('laptop_challenge')
    phone_challenge = db.relationship('phone_challenge')
    server_challenge = db.relationship('server_challenge')
    splunk_challenges = db.relationship('splunk_challenges')

class laptop_challenge(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    challengeState = db.Column(db.Integer)
    laptopPassword = db.Column(db.String(1000))
    hints = db.Column(db.Integer)
    startTime = db.Column(db.String)

class phone_challenge(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    challengeState = db.Column(db.Integer)
    phonePrime1 = db.Column(db.Integer)
    phonePrime2 = db.Column(db.Integer)
    startTime = db.Column(db.String)
    hints = db.Column(db.Integer)
    stegChallenge = db.Column(db.Integer)
    aesChallenge = db.Column(db.Integer)

class server_challenge(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    challengeState = db.Column(db.Integer)
    startTime = db.Column(db.String)
    hints = db.Column(db.Integer)

class points(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    pointsTotal = db.Column(db.Integer)
    timeLeft = db.Column(db.Integer)
    startGameTime = db.Column(db.String(1000))
    #leaderBoard = db.relationship('leaderboard')

class splunk_challenges(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    challengeState = db.Column(db.Integer)
    key_one = db.Column(db.Integer)
    key_two = db.Column(db.Integer)
    key_three = db.Column(db.Integer)

"""class leaderboard(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    points = db.Column(db.Integer, db.ForeignKey('points.pointsTotal'))
    lecturerId = db.Column(db.Integer, db.ForeignKey('users.lecturerId'))"""
    




