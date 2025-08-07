from flask import Blueprint, render_template, redirect, url_for
from flask import request

from models import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/auth/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	elif request.method == 'POST':
		print(f"{request.form}")
		return render_template("login.html")
		


@auth_bp.route('/auth/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template("register.html")
	elif request.method == 'POST':
		form = request.form
		print(form)
		user = User(username=form['username'], 
			  email=form['E-mail'])
		user.set_password(form['password'])
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('/auth/login'))