
 #impotando o flask para a aplicação
from flask import Flask, render_template    #1 ° é o pacote e o 2° é a classe

#Importando o controller

from controllers import routes 



 #carregando o flask na variavel na variavel"app"
 #declarando variavel no phyton
app = Flask(__name__, template_folder='views') 


routes.init_app(app)
 # Variaveis com __ são variaveis de ambiente no phyton
 # __name__ representa o nome da aplicação
 
 #CRIANOD A ROTA PRINCIPAL DO SITE
 

 
 
 
 
 
 #Iniciando o servidor na porta 5000
if __name__=='__main__':
    app.run(port=5000, debug=True)
 #o metodo run inicia o servidor