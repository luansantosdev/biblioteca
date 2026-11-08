
from fastapi import FastAPI

from app.controllers.livro_controller import router as livro_router
from app.controllers.categoria_controller import router as categoria_router
from app.controllers.avaliacao_controller import router as avaliacao_router
from app.controllers.autor_controller import router as autor_router
from app.controllers.editora_controller import router as editora_router

app = FastAPI(
    title="API Biblioteca",
    description="API para gerenciamento da biblioteca escolar",
    version="1.0.0"
)


# Registrar as rotas
app.include_router(livro_router)
app.include_router(categoria_router)
app.include_router(avaliacao_router)
app.include_router(autor_router)
app.include_router(editora_router)

@app.get("/")
def inicio():
    return {
        "mensagem": "API Biblioteca funcionando!",
        "documentacao": "/docs"
    }
