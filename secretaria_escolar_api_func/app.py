from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from flask import redirect
from urllib.parse import unquote

from model import Session, Funcionario
from schemas import *


info = Info(title = "API Secretaria Escolar - Cadastro de Funcionários", version = "1.1.0")
app = OpenAPI(__name__, info = info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
funcionario_tag = Tag(name="Secretaria Escolar - Funcionarios", description="Adição, visualização, atualização e remoção de funcionários à base de dados")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/cadastra_funcionario', tags=[funcionario_tag],
          responses={"200": FuncionarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def insere_funcionario(form: FuncionarioSchema):
    """Cadastra um novo funcionário à base de dados

    Retorna uma representação do funcionário.
    """
    funcionario = Funcionario(
        matricula = form.matricula,
        nome = form.nome,
        cpf = form.cpf,
        telefone = form.telefone,
        endereco = form.endereco,
        cidade = form.cidade,
        cep = form.cep,
        cargo = form.cargo,
        unidade_escolar = form.unidade_escolar
        )

    try:
        # criando conexão com a base de dados
        session = Session()
        # adicionando um novo funcionário à base de dados
        session.add(funcionario)
        # efetivando o comando de adição de novo funcionário na tabela
        session.commit()
        return exibe_funcionario(funcionario), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Funcionário com a mesma matrícula existente na base de dados:/"
        return {"mensagem de erro de integridade": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível cadastrar um novo funcionário :/"
        return {"mensagem de erro": error_msg}, 400


@app.get('/listagem_funcionarios', tags=[funcionario_tag],
         responses={"200": ListagemFuncionariosSchema, "404": ErrorSchema})
def busca_funcionarios():
    """Faz a busca por todos os funcionários cadastrados na base de dados

    Retorna uma representação da listagem de funcionários.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    funcionarios = session.query(Funcionario).all()
    
    if not funcionarios:
        # se não há funcionarios cadastrados
        return {"funcionarios": []}, 200
    else:
        # retorna a representação da listagem de funcionarios
        return exibe_funcionarios(funcionarios), 200


@app.get('/busca_funcionario', tags=[funcionario_tag],
         responses={"200": FuncionarioViewSchema, "404": ErrorSchema})
def busca_funcionario(query: BuscaFuncionarioSchema):
    """Faz a busca por um funcionário a partir da matrícula do professor.

    Retorna uma representação do funcionário.
    """
    #matricula_func = query.matricula
    matricula_func = query.matricula
    # criando conexão com a base de dados
    session = Session()
    # fazendo a busca
    funcionario = session.query(Funcionario).filter(Funcionario.matricula == matricula_func).first()
    
    if not funcionario:
        # se o funcionario não foi encontrado
        error_msg = "Funcionário não encontrado na base de dados:/"
        return {"mensagem de erro": error_msg}, 404
    else:
        # retorna a representação de funcionario
        return exibe_funcionario(funcionario), 200


@app.delete('/remove_funcionario', tags=[funcionario_tag],
            responses={"200": RemoveFuncionarioSchema, "404": ErrorSchema})
def remove_funcionario(query: BuscaFuncionarioSchema):
    """Remove um funcionário a partir da matrícula informada

    Retorna uma mensagem de confirmação da remoção do funcionário.
    """
    
    #matricula_func = query.matricula
    matricula_func = query.matricula
    # criando conexão com a base de dados
    session = Session()
    # fazendo a remoção do funcionário da base de dados
    contador = session.query(Funcionario).filter(Funcionario.matricula == matricula_func).delete()
    session.commit()
    
    if contador:
        # se o funcionário foi removido da base de dados
        return {"mensagem": "Funcionário removido", "Matrícula": matricula_func}
    else:
        # se o funcionário não foi encontrado na base de dados
        error_msg = "Funcionário não encontrado na base de dados:/"
        return {"mensagem": error_msg}, 404