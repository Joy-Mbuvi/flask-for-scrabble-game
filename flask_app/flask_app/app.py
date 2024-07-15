from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.ekiqftvfqjfcfvfbdfkq:tomandjerryare24@aws-0-eu-west-1.pooler.supabase.com:6543/postgres'


db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate
bcrypt=Bcrypt(app) #created a bcrypt object that passes our flask app as an argument

from routes import *



if __name__ == '__main__':
    app.run(debug=True)