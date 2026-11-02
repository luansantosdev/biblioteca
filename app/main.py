
from fastapi import FastAPI

app = FastAPI(
    title="Biblioteca API",
    description="API REST para gerenciamento de biblioteca",
    version="1.0.0",
)


@app.get("/", tags=["Sistema"])
def inicio():
    return {
        "mensagem": "API da Biblioteca funcionando!"
    }


@app.get("/health", tags=["Sistema"])
def health():
    return {
        "status": "ok"
    }
