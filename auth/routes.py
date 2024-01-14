# auth/routes.py
from flask import Blueprint, render_template, redirect, url_for, request

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('auth/login.html')
    return

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # Your registration logic goes here
    return render_template('auth/register.html')

@auth_blueprint.route('/logout')
def logout():
    # Your logout logic goes here
    return redirect(url_for('auth.login'))  # Redirect to login page after logout
