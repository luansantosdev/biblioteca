from sqlalchemy.orm import Session

from app.dtos.editora_dto import EditoraCreate, EditoraUpdate
from app.repositories.editora_repository import EditoraRepository


class EditoraService:

    @staticmethod
    def criar(db: Session, dados: EditoraCreate):
        return EditoraRepository.criar(db, dados)

    @staticmethod
    def listar(db: Session):
        return EditoraRepository.listar(db)

    @staticmethod
    def buscar_por_id(db: Session, editora_id: int):
        editora = EditoraRepository.buscar_por_id(db, editora_id)

        if editora is None:
            raise LookupError("Editora não encontrada.")

        return editora

    @staticmethod
    def atualizar(db: Session, editora_id: int, dados: EditoraUpdate):
        editora = EditoraService.buscar_por_id(db, editora_id)

        return EditoraRepository.atualizar(db, editora, dados)

    @staticmethod
    def excluir(db: Session, editora_id: int):
        editora = EditoraService.buscar_por_id(db, editora_id)

        EditoraRepository.excluir(db, editora)

        return {"mensagem": "Editora excluída com sucesso."}