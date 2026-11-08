from typing import Optional

from pydantic import BaseModel, Field, ConfigDict, field_validator


class EditoraCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    pais: Optional[str] = Field(default=None, max_length=60)
    site: Optional[str] = Field(default=None, max_length=200)


class EditoraUpdate(BaseModel):
    nome: Optional[str] = Field(default=None, min_length=1, max_length=100)
    pais: Optional[str] = Field(default=None, max_length=60)
    site: Optional[str] = Field(default=None, max_length=200)

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, valor):
        if valor is None:
            raise ValueError("O nome da editora não pode ser nulo.")
        return valor


class EditoraResponse(BaseModel):
    id: int
    nome: str
    pais: Optional[str]
    site: Optional[str]

    model_config = ConfigDict(from_attributes=True)
