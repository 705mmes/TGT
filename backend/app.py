from flask import Flask

def create_app():
	app = Flask(__name__, static_folder="static")

	from routes.home import home_bp
	from routes.auth import auth_bp

	app.register_blueprint(home_bp)
	app.register_blueprint(auth_bp)

	return app
