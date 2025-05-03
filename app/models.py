from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, nullable=True, unique=True)
    senha=db.Column(db.String, nullable=True)

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_ordem=db.Column(db.Integer, nullable=True)
    motor=db.Column(db.String, nullable=True)
    oleo_motor=db.Column(db.String, nullable=True)
    caixa=db.Column(db.String, nullable=True)
    oleo_caixa=db.Column(db.String, nullable=True)