from flask import Blueprint, render_template

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/auth/login')
def login():
	return render_template("login.html")


@auth_bp.route('/auth/register')
def register():
	return render_template("register.html")