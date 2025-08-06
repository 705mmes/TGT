from flask import Blueprint, render_template, send_from_directory

home_bp = Blueprint("home", __name__)

@home_bp.route('/')
def index():
	return render_template("homepage.html")
