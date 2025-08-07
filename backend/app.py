from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Users

def create_app():
	app = Flask(__name__, static_folder="static")

	from routes.home import home_bp
	from routes.auth import auth_bp

	app.register_blueprint(home_bp)
	app.register_blueprint(auth_bp)

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://neo:fefe@localhost:15432/tgt_db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	db.init_app(app)

	with app.app_context():
		db.create_all()

	return app
