
 #impotando o flask para a aplicação
from flask import Flask, render_template    #1 ° é o pacote e depois a classe
 #carregando o flask na variavel na variavel"app"
 #declarando variavel no phyton
app = Flask(__name__, template_folder='views') 
 # Variaveis com __ são variaveis de ambiente no phyton
 # __name__ representa o nome da aplicação
 
 #CRIANOD A ROTA PRINCIPAL DO SITE
 
@app.route('/')       

#def cria funções no python
def home():
    return render_template('index.html')
    

@app.route('/games')

def games():
    return render_template('games.html')

@app.route('/consoles') 

def consoles():
    return render_template('consoles.html')
 
 
 
 
 
 #Iniciando o servidor na porta 5000
if __name__=='__main__':
    app.run(port=5000, debug=True)
 #o metodo run inicia o servidor