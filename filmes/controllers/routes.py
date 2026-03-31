from flask import Flask, render_template, request, redirect, url_for


def init_app(app):
    listaUsuario = [
        {'nome': 'Ruan', 'email': 'ruangmlima@gmail.com', 'telefone': '13-98211-8507'}]

    listaFilmes = [
        {'titulo': 'Inception', 'ano': 2010, 'genero': 'Sci-Fi'},
        {'titulo': 'The Dark Knight', 'ano': 2008, 'genero': 'Ação'}
    ]

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/filmes', methods=['GET', 'POST'])
    def filmes():
        if request.method == 'POST':
            titulo = request.form.get('titulo')
            ano = request.form.get('ano')
            genero = request.form.get('genero')
            if titulo and ano and genero:
                listaFilmes.append({
                    'titulo': titulo,
                    'ano': ano,
                    'genero': genero
                })
            return redirect(url_for('filmes'))

        # Importante
        return render_template('filmes.html', listaFilmes=listaFilmes)

    @app.route('/cadfilmes', methods=['GET', 'POST'])
    def cadfilme():
        if request.method == 'POST':
            titulo = request.form.get('titulo')
            ano = request.form.get('ano')
            genero = request.form.get('genero')
            if titulo and ano and genero:
                listaFilmes.append({
                    'titulo': titulo,
                    'ano': ano,
                    'genero': genero
                })
            return redirect(url_for('filmes'))
        return render_template('cadfilmes.html')

    @app.route('/usuario', methods=['GET', 'POST'])
    def usuario():
        if request.method == 'POST':
            nome = request.form.get('nome'),
            email = request.form.get('email')
            telefone = request.form.get('telefone')

            if nome and email and telefone:
                listaUsuario.append(
                    {'nome': nome, 'email': email, 'telefone': telefone})
                return redirect(url_for('usuario'))
        return render_template('cadusuario.html')

    @app.route('/cadusuario', methods=['GET', 'POST'])
    def cadusuario():
        if request.method == 'POST':
            nome = request.form.get('nome'),
            email = request.form.get('email')
            telefone = request.form.get('telefone')

            if nome and email and telefone:
                listaUsuario.append(
                    {'nome': nome, 'email': email, 'telefone': telefone})
                return redirect(url_for('usuario'))
        return render_template('cadusuario.html')
