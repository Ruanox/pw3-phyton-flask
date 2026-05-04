# IMPORTAÇÃO DO FLASK-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
#PARA RODAR ESSE SQL PRECISA CRIAR UMA INSTÂNCIA
db = SQLAlchemy()
#CRIANDO A CLASSE GAME
class Game(db.Model):
    id =  db.Column(db.Integer, primary_key = True)                #O PADRÃO É: "NOME" "=" "NOME DA INSTÂNCIA" "." "COLUMN" "(NOME DA INSTÂNTICIA.TIPO DE DADO)"
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    preco = db.Column(db.Float)
    qtd = db.Column(db.Integer)
    
    #INICIALIZANDO AS VARIAVEIS NA CLASSE (MÉTODO CONSTRUTOR)
    def __init__(self,ano,titulo,anol,categoria,plataforma,preco,qtd):
        self.ano = ano
        self.categoria = categoria
        self.plataforma = plataforma                              #ISSO SE CHAMA MODELO
        self.preco = preco
        self.qtd = qtd
        self.titulo = titulo
        
        
# class Console(db.Model):
#     id =  db.Column(db.Integer, primary_key = True)              
#     ano = db.Column(db.Integer)
#     fabricante = db.Column(db.String(150))
#     plataforma = db.Column(db.String(150))
#     preco = db.Column(db.Float)
#     qtd = db.Column(db.Integer)
    
#     #INICIALIZANDO AS VARIAVEIS NA CLASSE (MÉTODO CONSTRUTOR)
#     def __init__(self,ano,titulo,anol,categoria,plataforma,preco,qtd):
#         self.ano = ano
#         self.categoria = categoria
#         self.plataforma = plataforma                              
#         self.qtd = qtd
#         self.titulo = titulo