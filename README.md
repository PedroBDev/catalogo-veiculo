# 🚗 Sistema de Cadastro e Edição de Veículos (Flask)

Este é um sistema simples de cadastro e edição de veículos desenvolvido com Flask, SQLAlchemy e WTForms.

## 🛠 Tecnologias utilizadas

- Python
- Flask
- Flask-WTF
- SQLAlchemy
- Bootstrap (no front-end)
- HTML e CSS3

---

## ⚙️ Como rodar o projeto:

1. **Clone o repositório:**

```bash
git clone https://github.com/PedroBDev/catalogo-veiculo.git
cd catalogo-veiculo

2. Crie e ative seu ambiente virtual:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

3. Instale as dependencias:

pip install -r requirements.txt

4. Configure o banco de dados, se necessário:

flask db init
flask db migrate
flask db upgrade

5. Execute a aplicação:

flask run

Acesse no navegador: http://localhost:5001
