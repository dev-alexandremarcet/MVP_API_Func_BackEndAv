from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mensagem_erro: str
