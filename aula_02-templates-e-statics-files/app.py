
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
#criando variaveis ára a rota de gmaes

def games():
    titulo = "portal 2"
    ano = 2011
    categoria = "Puzze"
    jogadores = ['Marcos','Richard','Miguel','Renato','Pedro']
    #Enviando as variaveis para o HTML
    return render_template('games.html',
                        titulo =titulo,
                        ano =ano,
                        categoria =categoria,
                        jogadores = jogadores)
                             
@app.route('/consoles') 

def consoles():
    #criando um objeto
    
    console = {"Nome": "Playstation 2",
             "Fabricante":"Sony",
             "Ano": 2000} 
 
    return render_template('consoles.html',
                        console = console)
 
 
 
 
 
 #Iniciando o servidor na porta 5000
if __name__=='__main__':
    app.run(port=5000, debug=True)
 #o metodo run inicia o servidor