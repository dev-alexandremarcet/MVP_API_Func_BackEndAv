from pydantic import BaseModel
from typing import Optional, List
from model.funcionarios import Funcionario



class FuncionarioSchema(BaseModel):
    """ Define como deve ser representado um funcionário que será cadastrado.
    """
    matricula: str = "DIR001"
    nome: str = "Francisco"
    cpf: str = "12345678911"
    telefone: str = "21999999988"
    endereco: str = "Av Raul Veiga, 25 - Centro"
    cidade: str = "Cordeiro"
    cep: str = "28540000"
    cargo: str = "Diretor(a)"
    unidade_escolar: str = "Cordeiro"


class BuscaFuncionarioSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca, que será
        feita apenas com base na matrícula do funcionário.
    """
    matricula: str = "DIR001"


class ListagemFuncionariosSchema(BaseModel):
    """ Define como uma listagem de professores cadastrados será retornada.
    """
    list_funcionarios:List[FuncionarioSchema]


def exibe_funcionarios(funcionarios: List[Funcionario]):
    """ Retorna uma representação da listagem de funcionários cadastrados seguindo o schema definido em
        FuncionarioViewSchema.
    """
    result = []
    for funcionario in funcionarios:
        result.append({
            "matricula": funcionario.matricula,
            "nome": funcionario.nome,
            "cpf": funcionario.cpf,
            "telefone": funcionario.telefone,
            "endereco": funcionario.endereco,
            "cidade": funcionario.cidade,
            "cep": funcionario.cep,
            "cargo": funcionario.cargo,
            "unidade_escolar": funcionario.unidade_escolar
        })

    return {"funcionarios": result}


class FuncionarioViewSchema(BaseModel):
    """ Define como um funcionario cadastrado será retornado.
    """
    id: int = 1
    matricula: str = "DIR001"
    nome: str = "Francisco"
    cpf: str = "12345678911"
    telefone: str = "21999999988"
    endereco: str = "Av Raul Veiga, 25 - Centro"
    cidade: str = "Cordeiro"
    cep: str = "28540000"
    cargo: str = "Diretor(a)"
    unidade_escolar: str = "Cordeiro"


class RemoveFuncionarioSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção de um funcionário.
    """
    mensagem_remove_funcionario: str
    nome_remove_funcionario: str


def exibe_funcionario(funcionario: Funcionario):
    """ Retorna uma representação do funcionário seguindo o schema definido em
        FuncionarioViewSchema.
    """
    return {
        "matricula": funcionario.matricula,
        "nome": funcionario.nome,
        "cpf": funcionario.cpf,
        "telefone": funcionario.telefone,
        "endereco": funcionario.endereco,
        "cidade": funcionario.cidade,
        "cep": funcionario.cep,
        "cargo": funcionario.cargo,
        "unidade_escolar": funcionario.unidade_escolar
    }
