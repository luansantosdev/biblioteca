from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dtos.editora_dto import EditoraCreate, EditoraUpdate, EditoraResponse
from app.services.editora_service import EditoraService


router = APIRouter(prefix="/editoras", tags=["Editoras"])


@router.post("/", response_model=EditoraResponse, status_code=status.HTTP_201_CREATED)
def criar_editora(dados: EditoraCreate, db: Session = Depends(get_db)):
    return EditoraService.criar(db, dados)


@router.get("/", response_model=list[EditoraResponse])
def listar_editoras(db: Session = Depends(get_db)):
    return EditoraService.listar(db)


@router.get("/{editora_id}", response_model=EditoraResponse)
def buscar_editora(editora_id: int, db: Session = Depends(get_db)):
    try:
        return EditoraService.buscar_por_id(db, editora_id)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@router.put("/{editora_id}", response_model=EditoraResponse)
def atualizar_editora(
    editora_id: int,
    dados: EditoraUpdate,
    db: Session = Depends(get_db)
):
    try:
        return EditoraService.atualizar(db, editora_id, dados)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))


@router.delete("/{editora_id}")
def excluir_editora(editora_id: int, db: Session = Depends(get_db)):
    try:
        return EditoraService.excluir(db, editora_id)
    except LookupError as erro:
        raise HTTPException(status_code=404, detail=str(erro))