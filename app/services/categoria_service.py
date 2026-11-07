
from sqlalchemy.orm import Session

from app.dtos.categoria_dto import CategoriaCreate, CategoriaUpdate
from app.repositories.categoria_repository import CategoriaRepository


class CategoriaService:

    @staticmethod
    def criar(db: Session, dados: CategoriaCreate):
        categoria_existente = CategoriaRepository.buscar_por_nome(
            db, dados.nome
        )

        if categoria_existente:
            raise ValueError(
                "Já existe uma categoria cadastrada com esse nome."
            )

        return CategoriaRepository.criar(db, dados)

    @staticmethod
    def listar(db: Session):
        return CategoriaRepository.listar(db)

    @staticmethod
    def buscar_por_id(db: Session, categoria_id: int):
        categoria = CategoriaRepository.buscar_por_id(
            db, categoria_id
        )

        if categoria is None:
            raise LookupError("Categoria não encontrada.")

        return categoria

    @staticmethod
    def atualizar(
        db: Session,
        categoria_id: int,
        dados: CategoriaUpdate
    ):
        categoria = CategoriaService.buscar_por_id(
            db, categoria_id
        )

        dados_atualizados = dados.model_dump(exclude_unset=True)
        novo_nome = dados_atualizados.get("nome")

        if novo_nome is not None and novo_nome != categoria.nome:
            categoria_existente = CategoriaRepository.buscar_por_nome(
                db, novo_nome
            )

            if categoria_existente:
                raise ValueError(
                    "Já existe outra categoria com esse nome."
                )

        return CategoriaRepository.atualizar(
            db, categoria, dados
        )

    @staticmethod
    def excluir(db: Session, categoria_id: int):
        categoria = CategoriaService.buscar_por_id(
            db, categoria_id
        )

        CategoriaRepository.excluir(db, categoria)

        return {
            "mensagem": "Categoria excluída com sucesso."
        }
