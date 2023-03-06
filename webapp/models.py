from . import db
from flask import UserMixin
from datetime import datetime, date

class Users(db.Model, UserMixin):
    id = db.Column(db.Interger, primaryKey=True)
    user_name = db.Column(db.String(1000))
    password = db.Column(db.String(1000))
    admin = db.Column(db.String(100))
    email = db.Column(db.String(1000), unique=True)
    Challenge = db.relationship('Challenge')
    points = db.relationship('points')
    leaderBoard = db.relationship('leaderBoard')

class Challenge(db.Model):
    id = db.Column(db.Interger, primaryKey=True)
    user_id = db.Column(db.Interger, db.ForeignKey('Users.id'))
    challengeState = db.Column(db.Interger)
    laptopPassword = db.Column(db.String(1000))
    phonePassword = db.Column(db.Interger)
    hints = db.relationship('hints')

class points(db.Model):
    id = db.Column(db.Interger, db.ForeignKey('Users.id'), primaryKey=True)
    pointsTotal = db.Column(db.Interger)
    timeLeft = db.Column(db.Interger)
    lastAvtive = db.Column(db.String(1000))
    leaderBoard = db.relationship('leaderBoard')

class leaderBoard(db.Model):
    id = db.Column(db.interger, primaryKey = True)
    points = db.Column(db.interger, db.ForeignKey('points.pointsTotal'))
    user_id = db.Column(db.Interger, db.ForeignKey('Users.id'))

class hints(db.Model):
    challengeId = db.Column(db.Interger, db.ForeignKey('Challenge.id'), primaryKey=True)
    hintCount = db.Column(db.Interger)



