from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.editora import Editora
from app.dtos.editora_dto import EditoraCreate, EditoraUpdate


class EditoraRepository:

    @staticmethod
    def criar(db: Session, dados: EditoraCreate):
        novo_editora = Editora(**dados.model_dump())

        db.add(novo_editora)
        db.commit()
        db.refresh(novo_editora)

        return novo_editora

    @staticmethod
    def listar(db: Session):
        resultado = db.scalars(
            select(Editora).order_by(Editora.id)
        ).all()

        return resultado

    @staticmethod
    def buscar_por_id(db: Session, editora_id: int):
        return db.get(Editora, editora_id)

    @staticmethod
    def atualizar(db: Session, editora: Editora, dados: EditoraUpdate):
        dados_atualizados = dados.model_dump(exclude_unset=True)

        for campo, valor in dados_atualizados.items():
            setattr(editora, campo, valor)

        db.commit()
        db.refresh(editora)

        return editora

    @staticmethod
    def excluir(db: Session, editora: Editora):
        db.delete(editora)
        db.commit()

        return True