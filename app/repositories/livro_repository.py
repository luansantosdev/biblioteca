
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.livro import Livro
from app.dtos.livro_dto import LivroCreate, LivroUpdate


class LivroRepository:

    # Cadastrar um livro
    @staticmethod
    def criar(db: Session, dados: LivroCreate):
        novo_livro = Livro(**dados.model_dump())

        db.add(novo_livro)
        db.commit()
        db.refresh(novo_livro)

        return novo_livro

    # Listar todos os livros
    @staticmethod
    def listar(db: Session):
        resultado = db.scalars(
            select(Livro).order_by(Livro.id)
        ).all()

        return resultado

    # Buscar livro pelo ID
    @staticmethod
    def buscar_por_id(db: Session, livro_id: int):
        return db.get(Livro, livro_id)

    # Atualizar um livro
    @staticmethod
    def atualizar(
        db: Session,
        livro: Livro,
        dados: LivroUpdate
    ):
        dados_atualizados = dados.model_dump(exclude_unset=True)

        for campo, valor in dados_atualizados.items():
            setattr(livro, campo, valor)

        db.commit()
        db.refresh(livro)

        return livro

    # Excluir um livro
    @staticmethod
    def excluir(db: Session, livro: Livro):
        db.delete(livro)
        db.commit()

        return True


    # Buscar livro pelo ISBN
    @staticmethod
    def buscar_por_isbn(db: Session, isbn: str):
        return db.scalar(
            select(Livro).where(Livro.isbn == isbn)
        )
