from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from extension import db
from dotenv import load_dotenv
import os
import sys


load_dotenv()

path = '/home/muddasir/mysite/flask_app.py'
if path not in sys.path:
    sys.path.append(path)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from models import User  
from routes import *     

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)