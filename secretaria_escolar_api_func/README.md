# API Secretaria Escolar - Cadastro de Funcionários

## Como executar 


É necessário que todas as bibliotecas (libs) do python listadas no `requirements.txt` sejam instaladas.

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É recomendável o uso de ambientes virtuais do tipo [virtualenv]    
> Segue o link para instalação:(https://virtualenv.pypa.io/en/latest/installation.html).

Devemos executar o comando a seguir para a instalação das dependências/bibliotecas, descritas no arquivo `requirements.txt`.

```
(env)$ pip install -r requirements.txt
```

Devemos executar o comando a seguir para executarmos a API:

```
(env)$ flask run --host 0.0.0.0 --port 5002
```


```
Observações:
O teste da API via Swagger deverá considerar as características de cada um dos seguintes campos:
i) campo matricula: sequência de 3 letras maiúsculas seguida de 3 algarismos. (Ex.: DIR001, CPE002, SEC001);
(DIR = Diretor(a), CPE = Coordenador(a) Pedagógico(a), OED = Orientador(a) Educacional, SEC = Secretária) 
ii) campo CPF: 11 dígitos numéricos sem traço e sem pontos (Ex.:12345678901);
iii) campo telefone: 11 dígitos numéricos começando com DDD, sem hífen e sem parêntesis (Ex.:21987654321).
```
---
### Acesso no browser

Abra o [http://localhost:5002/#/](http://localhost:5002/#/) no navegador para verificar o status da API em execução.

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t secretaria_escolar_api_func .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5001:5001 secretaria_escolar_api_func
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5002/#/](http://localhost:5002/#/) no navegador.
