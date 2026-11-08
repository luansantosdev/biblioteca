
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.models.avaliacao import Avaliacao
from app.dtos.avaliacao_dto import AvaliacaoCreate, AvaliacaoUpdate


class AvaliacaoRepository:

    @staticmethod
    def criar(db: Session, dados: AvaliacaoCreate):
        avaliacao = Avaliacao(**dados.model_dump())
        db.add(avaliacao)
        db.commit()
        db.refresh(avaliacao)
        return avaliacao

    @staticmethod
    def listar(db: Session):
        return db.scalars(select(Avaliacao)).all()

    @staticmethod
    def buscar_por_id(db: Session, avaliacao_id: int):
        return db.get(Avaliacao, avaliacao_id)

    @staticmethod
    def atualizar(db: Session, avaliacao: Avaliacao, dados: AvaliacaoUpdate):
        for campo, valor in dados.model_dump(exclude_unset=True).items():
            setattr(avaliacao, campo, valor)

        db.commit()
        db.refresh(avaliacao)
        return avaliacao

    @staticmethod
    def excluir(db: Session, avaliacao: Avaliacao):
        db.delete(avaliacao)
        db.commit()

    @staticmethod
    def calcular_media(db: Session, livro_id: int):
        resultado = db.execute(
            select(
                func.avg(Avaliacao.nota),
                func.count(Avaliacao.id)
            ).where(Avaliacao.livro_id == livro_id)
        ).one()

        media, total = resultado

        return {
            "livro_id": livro_id,
            "media": round(float(media), 2) if media is not None else None,
            "total_avaliacoes": total
        }
