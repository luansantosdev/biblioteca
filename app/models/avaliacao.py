
from sqlalchemy import Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Avaliacao(Base):

    __tablename__ = "avaliacoes"

    __table_args__ = (
        CheckConstraint(
            "nota >= 1 AND nota <= 5",
            name="ck_avaliacoes_nota"
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    livro_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("livros.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    nota: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    comentario: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )
