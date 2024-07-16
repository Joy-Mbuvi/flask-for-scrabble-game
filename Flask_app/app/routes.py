#routes -end points
#1.game
#2. log in
#3 create account
#the home page

#authentication routes : login and create account routes
from flask import request, jsonify
from Flask_app.app import app, db
from Flask_app.models import User, Game


def create_tables():
    db.create_all()

@app.route('/')
def home():
    return '<h1> WELCOME TO OUR VERSION OF SCRABBLE </h1>'

@app.route('/create_account', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added', 'username': username}), 201

#@app.route('/login', methods=['POST'])
#def login():
#    username = request.json['username']
#    email = request.json['email']
#    return jsonify({'message': 'Login ', 'username': username}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'username': user.username, 'email': user.email} for user in users])

