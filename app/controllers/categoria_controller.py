
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dtos.categoria_dto import (
    CategoriaCreate,
    CategoriaUpdate,
    CategoriaResponse
)
from app.services.categoria_service import CategoriaService


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


# CADASTRAR CATEGORIA
@router.post(
    "/",
    response_model=CategoriaResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_categoria(
    dados: CategoriaCreate,
    db: Session = Depends(get_db)
):
    try:
        return CategoriaService.criar(db, dados)
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )


# LISTAR TODAS AS CATEGORIAS
@router.get(
    "/",
    response_model=list[CategoriaResponse]
)
def listar_categorias(
    db: Session = Depends(get_db)
):
    return CategoriaService.listar(db)


# BUSCAR CATEGORIA POR ID
@router.get(
    "/{categoria_id}",
    response_model=CategoriaResponse
)
def buscar_categoria(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    try:
        return CategoriaService.buscar_por_id(db, categoria_id)
    except LookupError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )


# ATUALIZAR CATEGORIA
@router.put(
    "/{categoria_id}",
    response_model=CategoriaResponse
)
def atualizar_categoria(
    categoria_id: int,
    dados: CategoriaUpdate,
    db: Session = Depends(get_db)
):
    try:
        return CategoriaService.atualizar(db, categoria_id, dados)
    except LookupError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )


# EXCLUIR CATEGORIA
@router.delete("/{categoria_id}")
def excluir_categoria(
    categoria_id: int,
    db: Session = Depends(get_db)
):
    try:
        return CategoriaService.excluir(db, categoria_id)
    except LookupError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )
