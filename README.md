# API Biblioteca Virtual

Projeto desenvolvido para a avaliação NP2 da disciplina de desenvolvimento de APIs, utilizando Python, FastAPI e PostgreSQL.

## Objetivo

Desenvolver uma API REST para gerenciamento de uma biblioteca virtual escolar, permitindo cadastrar, consultar, atualizar e excluir informações.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- Swagger UI

## Funcionalidades

O sistema possui cinco módulos CRUD:

1. **Livros:** gerenciamento do acervo.
2. **Autores:** cadastro e gerenciamento de autores.
3. **Editoras:** cadastro e gerenciamento de editoras.
4. **Categorias:** cadastro e gerenciamento de categorias.
5. **Avaliações:** registro e gerenciamento de avaliações dos livros.

**Funcionalidade extra:** cálculo da média das avaliações de um livro, disponível na rota `GET /livros/{livro_id}/media-avaliacoes`.

## Como executar

### 1. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 2. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

### 4. Configurar o PostgreSQL

Criar um banco de dados chamado `biblioteca`.

Copiar o arquivo `.env.exemplo` para `.env` e preencher os dados de conexão conforme o ambiente local.

### 5. Executar as migrations

```powershell
python -m alembic upgrade head
```

### 6. Iniciar a API

```powershell
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8081
```

### 7. Acessar o Swagger

Abrir no navegador:

http://127.0.0.1:8081/docs

## Organização do projeto

O projeto utiliza uma arquitetura dividida em:

- `controllers/`: definição dos endpoints HTTP.
- `services/`: regras de negócio.
- `repositories/`: operações no banco de dados.
- `models/`: entidades SQLAlchemy.
- `dtos/`: validação e transferência de dados.
- `core/`: configuração e conexão com o banco.
- `migrations/`: versionamento da estrutura do banco.

## Integrantes e contribuições

**Eduardo Vasconcelos Andrade — GitHub: @dudu-jpg**
- Desenvolvimento do CRUD de Categorias.
- Desenvolvimento do CRUD de Avaliações.
- Implementação da funcionalidade extra de média das avaliações por livro.
- Validações, testes e integração dos módulos.

**Luan Santos — GitHub: @luansantosdev**
- Configuração inicial do projeto e banco de dados.
- Desenvolvimento do CRUD de Livros.
- Desenvolvimento do CRUD de Autores.
- Desenvolvimento do CRUD de Editoras.

## Uso de inteligência artificial

Foi utilizado o ChatGPT como ferramenta de apoio durante o desenvolvimento, principalmente para orientação sobre FastAPI, SQLAlchemy, Alembic, resolução de conflitos Git, integração de módulos e testes.

O código foi executado e validado pela equipe.

## Repositório

https://github.com/luansantosdev/biblioteca

**Branch integrada:** `feature/categorias-emprestimos`

**Commit de referência:** atualizar após finalizar a documentação.