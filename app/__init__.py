from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import secrets 
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'#configurando e criando caminho do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #desablitando checagem(aumentar a produção)
app.config['SECRET_KEY']=secrets.token_hex(16)

db= SQLAlchemy(app)#criando banco de dados
migrate=Migrate(app, db)#configurand migrate(utilizado para realizar as modificações no db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)
from app.routes import homepage
from app.models import Veiculo