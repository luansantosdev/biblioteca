
from datetime import date

from sqlalchemy import String, Integer, Date, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    nacionalidade: Mapped[str | None] = mapped_column(
        String(60),
        nullable=True
    )

    data_nascimento: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    biografia: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    livros = relationship(
        "Livro",
        back_populates="autor_obj"
    )
