
from sqlalchemy.orm import Session

from app.dtos.livro_dto import LivroCreate, LivroUpdate
from app.repositories.livro_repository import LivroRepository


class LivroService:

    @staticmethod
    def criar(db: Session, dados: LivroCreate):
        # Verifica se já existe um livro com esse ISBN
        livro_existente = LivroRepository.buscar_por_isbn(
            db, dados.isbn
        )

        if livro_existente:
            raise ValueError("Já existe um livro cadastrado com esse ISBN.")

        return LivroRepository.criar(db, dados)

    @staticmethod
    def listar(db: Session):
        return LivroRepository.listar(db)

    @staticmethod
    def buscar_por_id(db: Session, livro_id: int):
        livro = LivroRepository.buscar_por_id(db, livro_id)

        if livro is None:
            raise LookupError("Livro não encontrado.")

        return livro

    @staticmethod
    def atualizar(
        db: Session,
        livro_id: int,
        dados: LivroUpdate
    ):
        livro = LivroService.buscar_por_id(db, livro_id)

        dados_atualizados = dados.model_dump(exclude_unset=True)

        # Verifica ISBN duplicado somente se ele foi enviado
        novo_isbn = dados_atualizados.get("isbn")

        if novo_isbn is not None and novo_isbn != livro.isbn:
            livro_existente = LivroRepository.buscar_por_isbn(
                db, novo_isbn
            )

            if livro_existente:
                raise ValueError("Já existe outro livro cadastrado com esse ISBN.")

        return LivroRepository.atualizar(db, livro, dados)

    @staticmethod
    def excluir(db: Session, livro_id: int):
        livro = LivroService.buscar_por_id(db, livro_id)

        LivroRepository.excluir(db, livro)

        return {"mensagem": "Livro excluído com sucesso."}
