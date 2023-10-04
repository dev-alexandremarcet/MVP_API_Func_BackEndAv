from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Funcionario(Base):
    __tablename__ = 'tbl_funcionarios'

    id = Column("pk_funcionario", Integer, primary_key = True)
    matricula = Column(String(6), unique = True)
    nome = Column(String(100))
    cpf = Column(String(11))
    telefone = Column(String(11))
    endereco = Column(String(100))
    cidade = Column(String(30))
    cep = Column(String(8))
    cargo = Column(String(30))
    unidade_escolar = Column(String(30))
    data_insercao = Column(DateTime, default = datetime.now())

    def __init__(self, matricula: str, nome: str, cpf: str, telefone: str, endereco: str,
                 cidade: str, cep: str, cargo: str, unidade_escolar: str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um registro para um funcionário com os seguintes argumentos:
            matricula: matrícula do funcionário.
            nome: nome do funcionário.
            cpf: cpf do funcionário.
            telefone: telefone do funcionário.
            endereco: endereço do funcionário.
            cidade: cidade onde o funcionário reside.
            cep: cep do endereço do funcionário.
            cargo: cargo/função do funcionário.
            unidade_escolar: unidade escolar onde o funcionário trabalha.
            data_insercao: data na qual o funcionário foi cadastrado.
        """
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.cep = cep
        self.cargo = cargo
        self.unidade_escolar = unidade_escolar

        # se não for informada, será a data do cadastro do funcionário
        if data_insercao:
            self.data_insercao = data_insercao