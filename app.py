from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal_animes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição da tabela de usuários
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    apelido = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    animes_preferidos = db.relationship('Anime', secondary='usuario_anime', backref=db.backref('usuarios', lazy=True))

# Definição da tabela de animes
class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)

# Tabela de associação entre usuários e animes preferidos
usuario_anime = db.Table('usuario_anime',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True),
    db.Column('anime_id', db.Integer, db.ForeignKey('anime.id'), primary_key=True)
)
@app.route('/')
def initial():

    return '''<h2>API construída para o projeto integrador 4</h2>
    <h2>"Desenvolvimento de Sistemas"</h2>
    <h3>Documentação dos Endpoints:</h3>
    <h4>Endpoints de Usuários:</h4>
    <ul>
        <li><strong>POST /usuarios</strong>: Cria um novo usuário</li>
        <li><strong>GET /usuarios</strong>: Obter todos os usuários</li>
        <li><strong>GET /usuarios/{id}</strong>: Obter um usuário por ID</li>
        <li><strong>GET /usuarios/nome_usuario/{nome_usuario}</strong>: Buscar usuário por nome de usuário</li>
        <li><strong>GET /usuarios/email/{email}</strong>: Buscar usuário por email</li>
        <li><strong>POST /verificar-login</strong>: Verificar login</li>
        <li><strong>PUT /usuarios/atualizar/{id}</strong>: Atualiza um usuário existente.</li>
        <li><strong>DELETE /usuarios/{id}</strong>: Exclui um usuário existente.</li>
    </ul>
    <h4>Endpoints de Animes:</h4>
    <ul>
        <li><strong>GET /animes</strong>: Obter todos os animes</li>
        <li><strong>GET /animes/{id}</strong>: Obter um anime por ID</li>
        <li><strong>PUT /animes/{id}</strong>: Atualiza um anime existente</li>
        <li><strong>DELETE /animes/{id}</strong>: Exclui um anime existente</li>
    </ul>
    <div>
        <h2>A API Like a Anime oferece endpoints para gerenciar usuários e animes.</h2>

<h3>Endpoints de Usuários:</h3>

<h4>Criar um novo usuário</h4>
<ul>
    <li><strong>Método:</strong> POST</li>
    <li><strong>Rota:</strong> /usuarios</li>
    <li><strong>Descrição:</strong> Cria um novo usuário com os dados fornecidos.</li>
    <li><strong>Parâmetros de entrada:</strong>
        <ul>
            <li>nome (obrigatório): Nome do usuário.</li>
            <li>apelido (obrigatório): Apelido do usuário.</li>
            <li>email (obrigatório): Email do usuário.</li>
            <li>senha (obrigatório): Senha do usuário.</li>
            <li>animes_preferidos (opcional): Lista de animes preferidos do usuário.</li>
        </ul>
    </li>
    <li><strong>Resposta de sucesso:</strong> 200 OK</li>
    <li><strong>Resposta de erro:</strong> 409 Conflict se o email já estiver registrado.</li>
</ul>

<h4>Obter todos os usuários</h4>
<ul>
    <li><strong>Método:</strong> GET</li>
    <li><strong>Rota:</strong> /usuarios</li>
    <li><strong>Descrição:</strong> Retorna uma lista de todos os usuários registrados.</li>
    <li><strong>Parâmetros de entrada:</strong> Nenhum.</li>
    <li><strong>Resposta de sucesso:</strong> 200 OK com a lista de usuários.</li>
</ul>

<h4>Obter um usuário por ID</h4>
<ul>
    <li><strong>Método:</strong> GET</li>
    <li><strong>Rota:</strong> /usuarios/{id}</li>
    <li><strong>Descrição:</strong> Retorna os detalhes de um usuário específico com base no ID fornecido.</li>
    <li><strong>Parâmetros de entrada:</strong>
        <ul>
            <li>id (obrigatório): ID do usuário.</li>
        </ul>
    </li>
    <li><strong>Resposta de sucesso:</strong> 200 OK com os detalhes do usuário.</li>
    <li><strong>Resposta de erro:</strong> 404 Not Found se o usuário não for encontrado.</li>
</ul>

<h4>Buscar usuário por nome de usuário</h4>
<ul>
    <li><strong>Método:</strong> GET</li>
    <li><strong>Rota:</strong> /usuarios/nome_usuario/{nome_usuario}</li>
    <li><strong>Descrição:</strong> Retorna os detalhes de um usuário específico com base no nome de usuário fornecido.</li>
    <li><strong>Parâmetros de entrada:</strong>
        <ul>
            <li>nome_usuario (obrigatório): Nome de usuário do usuário.</li>
        </ul>
    </li>
    <li><strong>Resposta de sucesso:</strong> 200 OK com os detalhes do usuário.</li>
    <li><strong>Resposta de erro:</strong> 404 Not Found se o usuário não for encontrado.</li>
</ul>

<h4>Buscar usuário por email</h4>
<ul>
    <li><strong>Método:</strong> GET

</li>
    <li><strong>Rota:</strong> /usuarios/email/{email}</li>
    <li><strong>Descrição:</strong> Retorna os detalhes de um usuário específico com base no email fornecido.</li>
    <li><strong>Parâmetros de entrada:</strong>
        <ul>
            <li>email (obrigatório): Email do usuário.</li>
        </ul>
    </li>
    <li><strong>Resposta de sucesso:</strong> 200 OK com os detalhes do usuário.</li>
    <li><strong>Resposta de erro:</strong> 404 Not Found se o usuário não for encontrado.</li>
</ul>

<h4>Verificar login</h4>
<ul>
    <li><strong>Método:</strong> POST</li>
    <li><strong>Rota:</strong> /verificar-login</li>
    <li><strong>Descrição:</strong> Verifica as credenciais de login fornecidas e retorna uma mensagem de sucesso ou erro.</li>
    <li><strong>Parâmetros de entrada:</strong>
        <ul>
            <li>email (opcional): Email do usuário.</li>
            <li>apelido (opcional): Apelido do usuário.</li>
            <li>senha (obrigatório): Senha do usuário.</li>
        </ul>
        <li><strong>Resposta de sucesso:</strong> 200 Login efetuado com sucesso.</li>
        <li><strong>Resposta de erro 1:</strong> 400 Por favor, forneça um email ou um apelido.</li>
        <li><strong>Resposta de erro 2:</strong> 401 Usuário ou senha incorretos.</li>
    </li>
</ul>

<h3>Endpoints de Animes:</h3>

<h4>Obter todos os animes</h4>
<ul>
    <li><strong>Método:</strong> GET</li>
    <li><strong>Rota:</strong> /animes</li>
    <li><strong>Descrição:</strong> Obtém todos os animes disponíveis.</li>
    <li><strong>Parâmetros de entrada:</strong> Nenhum.</li>
    <li><strong>Resposta de sucesso:</strong> 200 OK com a lista de todos os animes disponíveis.</li>
</ul>

<h4>Obter um anime por ID</h4>
<ul>
    <li><strong>Método:</strong> GET</li>
    <li><strong>Rota:</strong> /animes/{id}</li>
    <li><strong>Descrição:</strong> Obtém um anime por ID.</li>
    <li><strong>Parâmetros de entrada:</strong>
        <ul>
            <li>id (obrigatório): O ID do anime.</li>
        </ul>
    </li>
    <li><strong>Resposta de sucesso:</strong> 200 OK com os detalhes do anime correspondente.</li>
    <li><strong>Resposta de erro:</strong> 404 Not Found se o anime não for encontrado.</li>
</ul>

<h4>Atualizar um anime existente</h4>
<ul>
    <li><strong>Método:</strong> PUT</li>
    <li><strong>Rota:</strong> /animes/{id}</li>
    <li><strong>Descrição:</strong> Atualiza um anime existente.</li>
    <li><strong>Parâmetros de entrada:</strong>
        <ul>
            <li>id (obrigatório): O ID do anime a ser atualizado.</li>
            <li>Dados atualizados (opcional): JSON contendo os campos a serem atualizados (ex: {"nome": "Novo nome", "categoria": "Nova categoria"}).</li>
        </ul>
    </li>
    <li><strong>Resposta de

 sucesso:</strong> 200 OK com uma mensagem indicando que o anime foi atualizado com sucesso.</li>
    <li><strong>Resposta de erro:</strong> 404 Not Found se o anime não for encontrado.</li>
</ul>

<h4>Excluir um anime existente</h4>
<ul>
    <li><strong>Método:</strong> DELETE</li>
    <li><strong>Rota:</strong> /animes/{id}</li>
    <li><strong>Descrição:</strong> Exclui um anime existente.</li>
    <li><strong>Parâmetros de entrada:</strong>
        <ul>
            <li>id (obrigatório): O ID do anime a ser excluído.</li>
        </ul>
    </li>
    <li><strong>Resposta de sucesso:</strong> 200 OK com uma mensagem indicando que o anime foi excluído com sucesso.</li>
    <li><strong>Resposta de erro:</strong> 404 Not Found se o anime não for encontrado.</li>
</ul>
</div>

    '''

# Rota para criar um novo usuário
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo_usuario = request.json
    usuario = Usuario(nome=novo_usuario['nome'], apelido=novo_usuario['apelido'],
                      email=novo_usuario['email'], senha=novo_usuario['senha'])
    if 'animes_preferidos' in novo_usuario:
        animes_preferidos = novo_usuario['animes_preferidos']
        usuario.animes_preferidos = animes_preferidos
    try:
        db.session.add(usuario)
        db.session.commit()
        return jsonify({'message': 'Usuário criado com sucesso.'})
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Este email já está registrado.'}), 409

# Rota para obter todos os usuários
@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    usuarios = Usuario.query.all()
    resultado = []
    for usuario in usuarios:
        resultado.append({'id': usuario.id, 'nome': usuario.nome, 'apelido': usuario.apelido,
                          'email': usuario.email, 'animes_preferidos': [anime.nome for anime in usuario.animes_preferidos]})
    return jsonify(resultado)

# Rota para obter um usuário por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario_por_id(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado.'}), 404
    resultado = {'id': usuario.id, 'nome': usuario.nome, 'apelido': usuario.apelido,
                 'email': usuario.email, 'animes_preferidos': [anime.nome for anime in usuario.animes_preferidos]}
    return jsonify(resultado)

# Rota para obter um usuário por nome de usuário
@app.route('/usuarios/nome_usuario/<string:nome_usuario>', methods=['GET'])
def buscar_usuario_por_nome_usuario(nome_usuario):
    usuario = Usuario.query.filter_by(apelido=nome_usuario).first()
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado.'}), 404
    return jsonify({
        'id': usuario.id,
        'nome': usuario.nome,
        'apelido': usuario.apelido,
        'email': usuario.email,
        'senha': usuario.senha,
        'animes_preferidos': [anime.nome for anime in usuario.animes_preferidos]
    })
# Rota para obter um usuário por email
@app.route('/usuarios/email/<string:email>', methods=['GET'])
def buscar_usuario_por_email(email):
    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado.'}), 404
    return jsonify({
        'id': usuario.id,
        'nome': usuario.nome,
        'apelido': usuario.apelido,
        'email': usuario.email,
        'senha': usuario.senha,
        'animes_preferidos': [anime.nome for anime in usuario.animes_preferidos]
    })
    # Verificação de login
@app.route('/verificar-login', methods=['POST'])
def verificar_login():
    dados_login = request.json
    email = dados_login.get('email')
    apelido = dados_login.get('apelido')
    senha = dados_login.get('senha')

    # Verifica se foi enviado um email ou um apelido
    if email:
        usuario = Usuario.query.filter_by(email=email).first()
    elif apelido:
        usuario = Usuario.query.filter_by(apelido=apelido).first()
    else:
        return jsonify({'message': 'Por favor, forneça um email ou um apelido.'}), 400

    # Verifica se o usuário foi encontrado e se a senha está correta
    if usuario and usuario.senha == senha:        
        return jsonify({'message': 'Login efetuado com sucesso'}), 200
    else:
        # Trata erro de login inválido
        return jsonify({'error': 'Usuário ou senha incorretos.'}), 401


# Rota para atualizar um usuário
@app.route('/usuarios/atualizar/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado.'}), 404

    dados_atualizados = request.json
    usuario.nome = dados_atualizados.get('nome', usuario.nome)
    usuario.apelido = dados_atualizados.get('apelido',usuario.apelido)
    usuario.email = dados_atualizados.get('email', usuario.email)
    usuario.senha = dados_atualizados.get('senha', usuario.senha)

    if 'animes_preferidos' in dados_atualizados:
        animes_preferidos = dados_atualizados['animes_preferidos']
        for anime_dados in animes_preferidos:
            anime = Anime(nome=anime_dados['nome'], categoria=anime_dados['categoria'])
            usuario.animes_preferidos.append(anime)

    db.session.commit()
    return jsonify({'message': 'Usuário atualizado com sucesso.'}), 200


# Rota para excluir um usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'message': 'Usuário não encontrado.'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuário excluído com sucesso.'})

# Rota para criar um novo anime
@app.route('/animes', methods=['POST'])
def criar_anime():
    novo_anime = request.json
    anime = Anime(nome=novo_anime['nome'], categoria=novo_anime['categoria'])
    db.session.add(anime)
    db.session.commit()
    return jsonify({'message': 'Anime criado com sucesso.'})

# Rota para obter todos os animes
@app.route('/animes', methods=['GET'])
def obter_animes():
    animes = Anime.query.all()
    resultado = []
    for anime in animes:
        resultado.append({'id': anime.id, 'nome': anime.nome, 'categoria': anime.categoria})
    return jsonify(resultado)

# Rota para obter um anime por ID
@app.route('/animes/int:id', methods=['GET'])
def obter_anime_por_id(id):
    anime = Anime.query.get(id)
    if not anime:
        return jsonify({'message': 'Anime não encontrado.'}), 404
    resultado = {'id': anime.id, 'nome': anime.nome, 'categoria': anime.categoria}
    return jsonify(resultado)

# Rota para atualizar um anime
@app.route('/animes/int:id', methods=['PUT'])
def atualizar_anime(id):
    anime = Anime.query.get(id)
    if not anime:
        return jsonify({'message': 'Anime não encontrado.'}), 404
    dados_atualizados = request.json
    anime.nome = dados_atualizados.get('nome', anime.nome)
    anime.categoria = dados_atualizados.get('categoria', anime.categoria)
    db.session.commit()
    return jsonify({'message': 'Anime atualizado com sucesso.'})

# Rota para excluir um anime
@app.route('/animes/int:id', methods=['DELETE'])
def excluir_anime(id):
    anime = Anime.query.get(id)
    if not anime:
        return jsonify({'message': 'Anime não encontrado.'}), 404
    db.session.delete(anime)
    db.session.commit()
    return jsonify({'message': 'Anime excluído com sucesso.'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)