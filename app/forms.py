from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import Veiculo, User
from app import db, bcrypt

class UserForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha=PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit=SubmitField('Salvar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Error: Usuário já cadastrado')


    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user = User(username=self.username.data, senha=senha)

        db.session.add(user)
        db.session.commit()

class LoginForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired()])
    senha=PasswordField('Senha', validators=[DataRequired()])
    btnSubmit=SubmitField('Login')

    def login(self):
        user = User.query.filter_by(username = self.username.data).first()

        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                return user
            else:
                raise Exception("Senha incorreta!!")
        else:
             raise Exception("Usuário não encontrado!!")

class VeiculoForm(FlaskForm):
    numero_ordem=IntegerField('Veículo', validators=[DataRequired()])
    motor=StringField('Motor', validators=[DataRequired()])
    oleo_motor=StringField('Óleo de motor', validators=[DataRequired()])
    caixa=StringField('Caixa de Marcha/Mudança', validators=[DataRequired()])
    oleo_caixa=StringField('Óleo da Caixa', validators=[DataRequired()])
    btnSubmit=SubmitField('Salvar')
  

    def save(self):
        veiculo= Veiculo(numero_ordem=self.numero_ordem.data, 
                        motor=self.motor.data, 
                        caixa=self.caixa.data, 
                        oleo_motor=self.oleo_motor.data,
                        oleo_caixa=self.oleo_caixa.data)

        db.session.add(veiculo)
        db.session.commit()

class VeiculoFormDelete(FlaskForm):
    numero_ordem=IntegerField('Veículo', validators=[DataRequired()])
    btnSubmitdelete=SubmitField('deletar')

    def delete(self):
        
        veiculo_delete = Veiculo.query.filter_by(numero_ordem=self.numero_ordem.data).first()
        if veiculo_delete==None:
            flash('Error: Veículo não encontrado')
        else:
            db.session.delete(veiculo_delete)
            db.session.commit()

class VeiculoFormUpdate(FlaskForm):
    numero_ordem=IntegerField('Veículo', validators=[DataRequired()])
    motor=StringField('Motor', validators=[DataRequired()])
    oleo_motor=StringField('Óleo de motor', validators=[DataRequired()])
    caixa=StringField('Caixa de Marcha/Mudança', validators=[DataRequired()])
    oleo_caixa=StringField('Óleo da Caixa', validators=[DataRequired()])
    btnSubmit=SubmitField('Salvar')
  

    def update(self):
        veiculo = Veiculo.query.filter_by(numero_ordem = self.numero_ordem.data).first()
        if veiculo:
            veiculo.motor = self.motor.data
            veiculo.oleo_motor = self.oleo_motor.data
            veiculo.caixa = self.caixa.data
            veiculo.oleo_caixa = self.oleo_caixa.data

            db.session.commit()
