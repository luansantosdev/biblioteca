
from sqlalchemy.orm import Session

from app.models.livro import Livro
from app.repositories.avaliacao_repository import AvaliacaoRepository
from app.dtos.avaliacao_dto import AvaliacaoCreate, AvaliacaoUpdate


class AvaliacaoService:

    @staticmethod
    def criar(db: Session, dados: AvaliacaoCreate):
        livro = db.get(Livro, dados.livro_id)

        if not livro:
            raise LookupError("Livro não encontrado.")

        return AvaliacaoRepository.criar(db, dados)

    @staticmethod
    def listar(db: Session):
        return AvaliacaoRepository.listar(db)

    @staticmethod
    def buscar_por_id(db: Session, avaliacao_id: int):
        avaliacao = AvaliacaoRepository.buscar_por_id(db, avaliacao_id)

        if not avaliacao:
            raise LookupError("Avaliação não encontrada.")

        return avaliacao

    @staticmethod
    def atualizar(db: Session, avaliacao_id: int, dados: AvaliacaoUpdate):
        avaliacao = AvaliacaoService.buscar_por_id(db, avaliacao_id)
        return AvaliacaoRepository.atualizar(db, avaliacao, dados)

    @staticmethod
    def excluir(db: Session, avaliacao_id: int):
        avaliacao = AvaliacaoService.buscar_por_id(db, avaliacao_id)
        AvaliacaoRepository.excluir(db, avaliacao)

    @staticmethod
    def calcular_media(db: Session, livro_id: int):
        livro = db.get(Livro, livro_id)

        if not livro:
            raise LookupError("Livro não encontrado.")

        return AvaliacaoRepository.calcular_media(db, livro_id)
