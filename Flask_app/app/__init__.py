from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.ekiqftvfqjfcfvfbdfkq:tomandjerryare24@aws-0-eu-west-1.pooler.supabase.com:6543/postgres'
    app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .auth_route import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app