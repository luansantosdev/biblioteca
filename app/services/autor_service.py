from sqlalchemy.orm import Session

from app.dtos.autor_dto import AutorCreate, AutorUpdate
from app.repositories.autor_repository import AutorRepository


class AutorService:

    @staticmethod
    def criar(db: Session, dados: AutorCreate):
        return AutorRepository.criar(db, dados)

    @staticmethod
    def listar(db: Session):
        return AutorRepository.listar(db)

    @staticmethod
    def buscar_por_id(db: Session, autor_id: int):
        autor = AutorRepository.buscar_por_id(db, autor_id)

        if autor is None:
            raise LookupError("Autor não encontrado.")

        return autor

    @staticmethod
    def atualizar(db: Session, autor_id: int, dados: AutorUpdate):
        autor = AutorService.buscar_por_id(db, autor_id)

        return AutorRepository.atualizar(db, autor, dados)

    @staticmethod
    def excluir(db: Session, autor_id: int):
        autor = AutorService.buscar_por_id(db, autor_id)

        AutorRepository.excluir(db, autor)

        return {"mensagem": "Autor excluído com sucesso."}