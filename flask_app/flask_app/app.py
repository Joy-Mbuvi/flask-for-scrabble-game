from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.ekiqftvfqjfcfvfbdfkq:tomandjerryare24@aws-0-eu-west-1.pooler.supabase.com:6543/postgres'


db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate


from routes import *



if __name__ == '__main__':
    app.run(debug=True)