import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)  # Clé primaire pour chaque entrée
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)  # Nom de la carte
    date = db.Column(db.Date, nullable=False)  # Date de la partie
