from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()

DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
<<<<<<< HEAD
    app.config['SECRET_KEY'] = 'Amberjack'
=======
    app.config['SECRET_KEY'] = 'itsasecret'
>>>>>>> main
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    
   

    with app.app_context():
        db.create_all()
    
        
    return app