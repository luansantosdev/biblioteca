
from fastapi import FastAPI

from app.controllers.livro_controller import router as livro_router
from app.controllers.autor_controller import router as autor_router
from app.controllers.editora_controller import router as editora_router

app = FastAPI(
    title="API Biblioteca",
    description="API para gerenciamento de livros",
    version="1.0.0"
)


# Registrar as rotas de livros
app.include_router(livro_router)
app.include_router(autor_router)
app.include_router(editora_router)

@app.get("/")
def inicio():
    return {
        "mensagem": "API Biblioteca funcionando!",
        "documentacao": "/docs"
    }
