
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# DTO para cadastrar um livro
class LivroCreate(BaseModel):
    titulo: str = Field(min_length=1, max_length=150)
    autor: str = Field(min_length=1, max_length=100)
    isbn: str = Field(min_length=1, max_length=20)
    ano_publicacao: int = Field(gt=0)
    quantidade_disponivel: int = Field(ge=0)


# DTO para atualizar um livro
class LivroUpdate(BaseModel):
    titulo: Optional[str] = Field(default=None, min_length=1, max_length=150)
    autor: Optional[str] = Field(default=None, min_length=1, max_length=100)
    isbn: Optional[str] = Field(default=None, min_length=1, max_length=20)
    ano_publicacao: Optional[int] = Field(default=None, gt=0)
    quantidade_disponivel: Optional[int] = Field(default=None, ge=0)


# DTO para retornar os dados do livro
class LivroResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    isbn: str
    ano_publicacao: int
    quantidade_disponivel: int

    model_config = ConfigDict(from_attributes=True)
