 #impotando o flask para a aplicação
from flask import render_template,request

# Criando a função principal para inicializar as rotas:

def init_app(app):
    listaConsole = ['Playstation 5','Xbox one','Super Nintendo','Atari','3Ds','GameBoy','Playstation 2','Nintendo Switch 2','Playstation 3','Playstation 4','Xbox 360','Xbox Series X']
 
 
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
                             
                             
    @app.route('/consoles', methods=['GET','POST']) 
    def consoles():
    #criando um objeto
    
        console = {"Nome": "Playstation 2",
                "Fabricante":"Sony",
                "Ano": 2000} 
       
        
        #Recebendo o valor do formulario
        if request.method == 'POST':
            if request.form.get('novoConsole'):
             listaConsole.append(request.form.get('novoConsole'))
        
    
        return render_template('consoles.html',
                            console = console,
                            listaConsole = listaConsole)
        
