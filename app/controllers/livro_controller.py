
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dtos.livro_dto import LivroCreate, LivroUpdate, LivroResponse
from app.services.livro_service import LivroService


router = APIRouter(
    prefix="/livros",
    tags=["Livros"]
)


# CADASTRAR LIVRO
@router.post(
    "/",
    response_model=LivroResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_livro(
    dados: LivroCreate,
    db: Session = Depends(get_db)
):
    try:
        return LivroService.criar(db, dados)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))
    except ValueError as erro:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(erro)
        )


# LISTAR TODOS OS LIVROS
@router.get(
    "/",
    response_model=list[LivroResponse]
)
def listar_livros(
    db: Session = Depends(get_db)
):
    return LivroService.listar(db)


# BUSCAR LIVRO POR ID
@router.get(
    "/{livro_id}",
    response_model=LivroResponse
)
def buscar_livro(
    livro_id: int,
    db: Session = Depends(get_db)
):
    try:
        return LivroService.buscar_por_id(db, livro_id)
    except LookupError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )


# ATUALIZAR LIVRO
@router.put(
    "/{livro_id}",
    response_model=LivroResponse
)
def atualizar_livro(
    livro_id: int,
    dados: LivroUpdate,
    db: Session = Depends(get_db)
):
    try:
        return LivroService.atualizar(db, livro_id, dados)
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


# EXCLUIR LIVRO
@router.delete("/{livro_id}")
def excluir_livro(
    livro_id: int,
    db: Session = Depends(get_db)
):
    try:
        return LivroService.excluir(db, livro_id)
    except LookupError as erro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(erro)
        )
