from . import db
from flask_login import UserMixin
from datetime import datetime, date

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    admin = db.Column(db.String(100))
    email = db.Column(db.String(1000), unique=True)
    points = db.relationship('points')
    leaderBoard = db.relationship('leaderboard')
    laptop_challenge = db.relationship('laptop_challenge')
    phone_challenge = db.relationship('phone_challenge')
    server_challenge = db.relationship('server_challenge')

class laptop_challenge(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    challengeState = db.Column(db.Integer)
    laptopPassword = db.Column(db.String(1000))
    hints = db.Column(db.Integer)

class phone_challenge(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    challengeState = db.Column(db.Integer)
    phonePrime1 = db.Column(db.Integer)
    phonePrime2 = db.Column(db.Integer)
    hints = db.Column(db.Integer)

class server_challenge(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    challengeState = db.Column(db.Integer)
    hints = db.Column(db.Integer)

class points(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    pointsTotal = db.Column(db.Integer)
    timeLeft = db.Column(db.Integer)
    lastActive = db.Column(db.String(1000))
    leaderBoard = db.relationship('leaderboard')

class leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    points = db.Column(db.Integer, db.ForeignKey('points.pointsTotal'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))




