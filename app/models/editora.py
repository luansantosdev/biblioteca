from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Editora(Base):
    __tablename__ = "editoras"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    pais: Mapped[str | None] = mapped_column(String(60), nullable=True)
    site: Mapped[str | None] = mapped_column(String(200), nullable=True)

    livros = relationship("Livro", back_populates="editora_obj")
