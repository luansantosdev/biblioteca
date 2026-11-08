from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.autor import Autor
from app.dtos.autor_dto import AutorCreate, AutorUpdate


class AutorRepository:

    @staticmethod
    def criar(db: Session, dados: AutorCreate):
        novo_autor = Autor(**dados.model_dump())

        db.add(novo_autor)
        db.commit()
        db.refresh(novo_autor)

        return novo_autor

    @staticmethod
    def listar(db: Session):
        resultado = db.scalars(
            select(Autor).order_by(Autor.id)
        ).all()

        return resultado

    @staticmethod
    def buscar_por_id(db: Session, autor_id: int):
        return db.get(Autor, autor_id)

    @staticmethod
    def atualizar(db: Session, autor: Autor, dados: AutorUpdate):
        dados_atualizados = dados.model_dump(exclude_unset=True)

        for campo, valor in dados_atualizados.items():
            setattr(autor, campo, valor)

        db.commit()
        db.refresh(autor)

        return autor

    @staticmethod
    def excluir(db: Session, autor: Autor):
        db.delete(autor)
        db.commit()

        return True