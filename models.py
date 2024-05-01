from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.app_context().push()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone_no = db.Column(db.String(15))
    password = db.Column(db.String(100))
    current_year = db.Column(db.String(50))
    current_semester = db.Column(db.String(50))
    branch = db.Column(db.String(100))
    father_name = db.Column(db.String(100))
    address = db.Column(db.String(200))

