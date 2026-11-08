from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class AutorCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    nacionalidade: Optional[str] = Field(default=None, max_length=60)
    data_nascimento: Optional[date] = None
    biografia: Optional[str] = None


class AutorUpdate(BaseModel):
    nome: Optional[str] = Field(default=None, min_length=1, max_length=100)
    nacionalidade: Optional[str] = Field(default=None, max_length=60)
    data_nascimento: Optional[date] = None
    biografia: Optional[str] = None


class AutorResponse(BaseModel):
    id: int
    nome: str
    nacionalidade: Optional[str]
    data_nascimento: Optional[date]
    biografia: Optional[str]

    model_config = ConfigDict(from_attributes=True)