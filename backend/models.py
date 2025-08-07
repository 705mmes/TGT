import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from argon2 import PasswordHasher

db = SQLAlchemy()

ph = PasswordHasher()

class User(db.Model):
	__tablename__ = 'Users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, nullable=False)
	email = db.Column(db.String(120), nullable=False)
	password = db.Column(db.String(128), nullable=False)
	date = db.Column(db.Date, nullable=True)

	def set_password(self, password: str):
		self.password = ph.hash(password)

	def check_password(self, password: str) -> bool:
		try:
			return ph.verify(self.password, password)
		except:
			return False