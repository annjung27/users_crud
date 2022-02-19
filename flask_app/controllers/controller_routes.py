from flask import Flask,render_template, redirect, request, session
from flask_app import app
from flask_app.models import model_user

@app.route('/')
def index():
    all_users = model_user.User.get_all()
    return render_template('index.html', all_users = all_users)