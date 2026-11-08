
from sqlalchemy import String, Integer, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Livro(Base):

    __tablename__ = "livros"

    __table_args__ = (
        CheckConstraint(
            "quantidade_disponivel >= 0",
            name="ck_livros_quantidade"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    titulo: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    autor: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    isbn: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    ano_publicacao: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    quantidade_disponivel: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )
    autor_id: Mapped[int | None] = mapped_column(
    ForeignKey("autores.id"),
    nullable=True
)

    autor_obj = relationship(
        "Autor",
        back_populates="livros"
)   

    editora_id: Mapped[int | None] = mapped_column(
        ForeignKey("editoras.id", name="fk_livros_editoras", ondelete="SET NULL"),
        nullable=True
    )

    editora_obj = relationship("Editora", back_populates="livros")
