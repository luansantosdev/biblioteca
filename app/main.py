
from fastapi import FastAPI

from app.controllers.livro_controller import router as livro_router


app = FastAPI(
    title="API Biblioteca",
    description="API para gerenciamento de livros",
    version="1.0.0"
)


# Registrar as rotas de livros
app.include_router(livro_router)


@app.get("/")
def inicio():
    return {
        "mensagem": "API Biblioteca funcionando!",
        "documentacao": "/docs"
    }
