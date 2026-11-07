
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.categoria import Categoria
from app.dtos.categoria_dto import CategoriaCreate, CategoriaUpdate


class CategoriaRepository:

    @staticmethod
    def criar(db: Session, dados: CategoriaCreate):
        nova_categoria = Categoria(**dados.model_dump())

        db.add(nova_categoria)
        db.commit()
        db.refresh(nova_categoria)

        return nova_categoria

    @staticmethod
    def listar(db: Session):
        return db.scalars(
            select(Categoria).order_by(Categoria.id)
        ).all()

    @staticmethod
    def buscar_por_id(db: Session, categoria_id: int):
        return db.get(Categoria, categoria_id)

    @staticmethod
    def buscar_por_nome(db: Session, nome: str):
        return db.scalar(
            select(Categoria).where(Categoria.nome == nome)
        )

    @staticmethod
    def atualizar(
        db: Session,
        categoria: Categoria,
        dados: CategoriaUpdate
    ):
        dados_atualizados = dados.model_dump(exclude_unset=True)

        for campo, valor in dados_atualizados.items():
            setattr(categoria, campo, valor)

        db.commit()
        db.refresh(categoria)

        return categoria

    @staticmethod
    def excluir(db: Session, categoria: Categoria):
        db.delete(categoria)
        db.commit()

        return True
