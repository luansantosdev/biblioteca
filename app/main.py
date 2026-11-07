
from fastapi import FastAPI

from app.controllers.livro_controller import router as livro_router
from app.controllers.categoria_controller import router as categoria_router


app = FastAPI(
    title="API Biblioteca",
    description="API para gerenciamento da biblioteca escolar",
    version="1.0.0"
)


# Registrar as rotas
app.include_router(livro_router)
app.include_router(categoria_router)


@app.get("/")
def inicio():
    return {
        "mensagem": "API Biblioteca funcionando!",
        "documentacao": "/docs"
    }
