from flask import Flask,render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_user import User


@app.route('/user/new') #dispaly
def new_user():
    return render_template("user_new.html")

@app.route('/user/create', methods= ['post'])    # Action
def create_user():
    id = User.create(request.form)    
    print(id)    
    return redirect('/')

@app.route('/user/<int:id>/show')  # Display
def show_user(id):
    user = User.get_one({'id':id})
    return render_template('user_show.html', user = user)

@app.route('/user/<int:id>/edit')  # Display
def edit_user(id):
    user = User.get_one({'id': id})
    return render_template('user_edit.html', user = user)

@app.route('/user/<int:id>/update', methods=['post'])  # Action
def update_user(id):
    print(request.form)    
    User.update_one(request.form)
    return redirect('/')

@app.route('/user/<int:id>/delete')  # Action
def delete_user(id):
    User.delete_one({'id':id})
    return redirect ('/')


