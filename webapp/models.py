from . import db
from flask_login import UserMixin
from datetime import datetime, date

class users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    admin = db.Column(db.String(100))
    email = db.Column(db.String(1000), unique=True)
    Challenge = db.relationship('Challenge')
    points = db.relationship('points')
    leaderBoard = db.relationship('leaderBoard')

class challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    challengeState = db.Column(db.Integer)
    laptopPassword = db.Column(db.String(1000))
    phonePassword = db.Column(db.Integer)
    hints = db.relationship('hints')

class points(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    pointsTotal = db.Column(db.Integer)
    timeLeft = db.Column(db.Integer)
    lastAvtive = db.Column(db.String(1000))
    leaderBoard = db.relationship('leaderBoard')

class leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    points = db.Column(db.Integer, db.ForeignKey('points.pointsTotal'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class hints(db.Model):
    challengeId = db.Column(db.Integer, db.ForeignKey('challenge.id'), primary_key=True)
    hintCount = db.Column(db.Integer)



