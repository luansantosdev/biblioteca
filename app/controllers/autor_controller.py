from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dtos.autor_dto import AutorCreate, AutorUpdate, AutorResponse
from app.services.autor_service import AutorService


router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post("/", response_model=AutorResponse, status_code=status.HTTP_201_CREATED)
def criar_autor(dados: AutorCreate, db: Session = Depends(get_db)):
    return AutorService.criar(db, dados)


@router.get("/", response_model=list[AutorResponse])
def listar_autores(db: Session = Depends(get_db)):
    return AutorService.listar(db)


@router.get("/{autor_id}", response_model=AutorResponse)
def buscar_autor(autor_id: int, db: Session = Depends(get_db)):
    try:
        return AutorService.buscar_por_id(db, autor_id)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@router.put("/{autor_id}", response_model=AutorResponse)
def atualizar_autor(
    autor_id: int,
    dados: AutorUpdate,
    db: Session = Depends(get_db)
):
    try:
        return AutorService.atualizar(db, autor_id, dados)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@router.delete("/{autor_id}")
def excluir_autor(autor_id: int, db: Session = Depends(get_db)):
    try:
        return AutorService.excluir(db, autor_id)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))