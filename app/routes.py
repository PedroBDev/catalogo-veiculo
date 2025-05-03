from app import app, db
from flask import render_template, url_for, request, redirect, flash
from app.models import Veiculo
from app.forms import VeiculoForm, VeiculoFormDelete, VeiculoFormUpdate, UserForm, LoginForm
from flask_login import current_user, login_user, logout_user

@app.route("/", methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        try:
            user = form.login()
            login_user(user)
            return redirect(url_for('homepage'))
        except Exception as e:
            flash(str(e), 'danger')
    

    return render_template('login.html', forms=form)

@app.route("/homepage/", methods=('GET', 'POST'))
def homepage():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        flash('Necessário fazer login!')
        return redirect(url_for('login'))

@app.route("/user/", methods=('GET', 'POST'))
def __cadastro_user():
    form = UserForm()

    if form.validate_on_submit():
        if form.validate_username(form.username.data):
            flash('Usuário já Cadastrado!!')
            return redirect(url_for('user'))
        else:
            form.save()
            flash('Usuário cadastrado com sucesso!')
            return redirect(url_for('login'))

    return render_template('cadastro_user.html', forms=form) 

@app.route("/Cadastro", methods=('GET', 'POST'))
def cadastro():
    form = VeiculoForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    
    return render_template('cadastro.html', forms=form)

@app.route('/lista', methods=['GET'])
def lista():
    
    if request.method=='GET':
        pesquisa=request.args.get('pesquisa')
    
    if pesquisa:
        dados=Veiculo.query.filter_by(numero_ordem=pesquisa).order_by(Veiculo.numero_ordem)
    else:
        dados = Veiculo.query.order_by(Veiculo.numero_ordem).all()

    context={'dados': dados}

    return render_template('lista.html', context=context)

@app.route('/delete', methods=('GET', 'POST'))
def delete():
    form = VeiculoFormDelete()
    if form.validate_on_submit():
        form.delete()
        return redirect(url_for('homepage'))


    return render_template('delete.html', forms=form)

@app.route('/veiculo/editar/:<int:numero_ordem>', methods = ('GET', 'POST'))
def update(numero_ordem):
    veiculo = Veiculo.query.filter_by(numero_ordem = numero_ordem).first_or_404()

    form = VeiculoFormUpdate(obj=veiculo)

    if form.validate_on_submit():
        form.update()
        return redirect(url_for('lista'))

    return render_template('update.html', form=form, veiculo=veiculo)

        
@app.route('/logout/', methods=('GET', 'POST'))
def logout():
    logout_user()
    return redirect(url_for('login'))