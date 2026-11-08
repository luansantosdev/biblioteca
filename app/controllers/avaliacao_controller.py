
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dtos.avaliacao_dto import (
    AvaliacaoCreate,
    AvaliacaoUpdate,
    AvaliacaoResponse,
    MediaAvaliacoesResponse
)
from app.services.avaliacao_service import AvaliacaoService


router = APIRouter(tags=["Avaliações"])


@router.post(
    "/avaliacoes/",
    response_model=AvaliacaoResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_avaliacao(dados: AvaliacaoCreate, db: Session = Depends(get_db)):
    try:
        return AvaliacaoService.criar(db, dados)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@router.get("/avaliacoes/", response_model=list[AvaliacaoResponse])
def listar_avaliacoes(db: Session = Depends(get_db)):
    return AvaliacaoService.listar(db)


@router.get("/avaliacoes/{avaliacao_id}", response_model=AvaliacaoResponse)
def buscar_avaliacao(avaliacao_id: int, db: Session = Depends(get_db)):
    try:
        return AvaliacaoService.buscar_por_id(db, avaliacao_id)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@router.put("/avaliacoes/{avaliacao_id}", response_model=AvaliacaoResponse)
def atualizar_avaliacao(
    avaliacao_id: int,
    dados: AvaliacaoUpdate,
    db: Session = Depends(get_db)
):
    try:
        return AvaliacaoService.atualizar(db, avaliacao_id, dados)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@router.delete("/avaliacoes/{avaliacao_id}")
def excluir_avaliacao(avaliacao_id: int, db: Session = Depends(get_db)):
    try:
        AvaliacaoService.excluir(db, avaliacao_id)
        return {"mensagem": "Avaliação excluída com sucesso."}
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@router.get(
    "/livros/{livro_id}/media-avaliacoes",
    response_model=MediaAvaliacoesResponse
)
def media_avaliacoes(livro_id: int, db: Session = Depends(get_db)):
    try:
        return AvaliacaoService.calcular_media(db, livro_id)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))
