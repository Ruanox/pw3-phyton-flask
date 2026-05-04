
 #impotando o flask para a aplicação
from flask import Flask, render_template    #1 ° é o pacote e o 2° é a classe
#IMPORTAR PYMYSQL
import pymysql 

#IMPORTAR O SQLALLCHEMY E O MODEL
from models.database import db,Game

#DEFINIR NOME DO BANCO

DB_NAME = "thegames"



#Importando o controller

from controllers import routes 



 #carregando o flask na variavel na variavel"app"
 #declarando variavel no phyton
app = Flask(__name__, template_folder='views') 

#PASSAR O NOME DO BANCO PARA O FLASK
app.config['DATABESE_NAME'] = DB_NAME
#PASSAR O ENDEREÇO DO BANCO PARA O FLASK-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

routes.init_app(app)
 # Variaveis com __ são variaveis de ambiente no phyton
 # __name__ representa o nome da aplicação
 
 #CRIANDO A ROTA PRINCIPAL DO SITE
  
 #Iniciando o servidor na porta 5000
if __name__=='__main__':

 #o metodo run inicia o servidor
 
    #CONECTAR O MYSQL PARA CRIAR O BANCO DE DADOS
    #PASSAR OS DADOS DE CONEXAO
    connection = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    #FAZENDO A CONEXÃO
    try:
        with connection.cursor() as cursor:
            #ENVIAR A QUERY PARA CRIAR O BANCO
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
            
    except Exception as error:
        print(f"Ocorreu um erro ao criar o banco de dados!{error}")
        #FECHAR CONEXÃO
    finally:
        connection.close()
        
        #INICIAR O FLASK-SQLALCHEMY
        db.init_app(app=app)
        
        with app.test_request_context():
            db.create_all()
            
    app.run(port=5000, debug=True)
            
    
    