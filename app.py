import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
db_url = os.environ.get('DATABASE_URL','sqlite:///motoristas.db')
if db_url.startswith('postgres://'):
    db_url = db_url.replace('postgres://','postgresql://',1)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Motorista(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nome=db.Column(db.String(100))
    telefone=db.Column(db.String(20))
    categoria=db.Column(db.String(10))
    comprovativo=db.Column(db.String(100))
    status=db.Column(db.String(20), default='pendente')
    data=db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html', iban='AO06.0040.0000.7034.7306.1019.0')

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run()
