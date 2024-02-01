# auth/routes.py
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('auth/login.html')
    
    return redirect(url_for('auth.login'))

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/login.html')

@auth_blueprint.route('/logout')
def logout():
    # Your logout logic goes here
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.login'))  # Redirect to login page after logout
