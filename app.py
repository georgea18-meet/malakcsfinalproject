from flask import Flask, redirect, flash, request, render_template, url_for, session, abort
import os
from flask_sqlalchemy import SQLAlchemy
from flask.ext.session import Session


app = Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' , 'mysql://username:password@server/db'
db=SQLAlchemy(app)
sess = Session()


class User(db.Model): #table
	id = db.Column(db.Integer, primary_key=True)
	firstname=db.Column(db.String(20), nullable=False)
	lastname=db.Column(db.String(20), nullable=False)
	username=db.Column(db.String(20), nullable=False, unique=True)
	password=db.Column(db.String(20), nullable=False, unique=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String(200), nullable=False)   
    username=db.Column(db.String(20), nullable=False, unique=True)

@app.route('/')
def index():
    return render_template('HH.HTML')

@app.route('/homepage')
def homepage():
    return render_template('homepage.HTML')

@app.route('/keepup')
def keepup():
    return render_template('keepup.HTML')

# @app.route('/clothes')
# def keepup():
#     return render_template('dresses.HTML')

@app.route('/feedback', methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        new_feedback = Feedback(comment=request.form['comment'],
                        username=request.form['username'])
        db.session.add(new_feedback)
        db.session.commit()


@app.route('/y')
@app.route('/add_user')
def add_user_fx():
    new_user=User()
    new_user.firstname=request.form.get("firstname")
    new_user.lastname=request.form.get("lastname")
    new_user.username=request.form.get("username")
    new_user.password=request.form.get("password")
    new_user.favorites=request.form.get("favorites")
    db.session.add(new_user)
    db.session.commit()

@app.route('/signup', methods='GET','POST')
def sign_up():
    user=User()
    user.firstname=request.form.post("firstname")
    user.lastname=request.form.post("lastname")
    user.username=request.form.post("username")
    user.password=request.form.post("password")
    user.favorites=request.form.post("favorites")
    db.session.add(user)
    db.session.commit()
    render_template('homepage.HTML')
# @app.route('/signin', method='GET')
# def signin():
#     user=User()
#     user.

@app.route('/login',methods=['GET','POST'])
def login():
    user=User()
    if request.method == 'GET':
        return render_template('HH.HTML')
    user.username = request.form['username']
    user.password = request.form['password']
    signedup_user = user.query.filter_by(username=username,password=password).first()
    render_template('homepage.HTML')
    if signedup_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('/'))
    

# def get_user_id(username): 
#     ok  = User.query.filter_by(username="username").first()
#     if ok  is not None: 
#        return ok
#     return None

# @app.route('/log_in/<username>/<password>')
# def log_in():
#     old_user=User("username","password")
#     old_user.username = User.query.filter_by(username="username").first_or_404()
#     old_user.password = if password == User.query.filter_by(username)
   
# @app.route('/signin', methods = ['GET',])

# def show_user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('show_user.html', user=user)


if __name__ == "__main__":
	app.run(debug=True)
