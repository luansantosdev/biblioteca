
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# DTO para cadastrar uma categoria
class CategoriaCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    descricao: Optional[str] = Field(
        default=None,
        max_length=255
    )


# DTO para atualizar uma categoria
class CategoriaUpdate(BaseModel):
    nome: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=100
    )
    descricao: Optional[str] = Field(
        default=None,
        max_length=255
    )


# DTO para retornar uma categoria
class CategoriaResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
