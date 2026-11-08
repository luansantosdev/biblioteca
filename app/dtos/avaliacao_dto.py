
from pydantic import BaseModel, ConfigDict, Field


class AvaliacaoCreate(BaseModel):
    livro_id: int = Field(gt=0)
    nota: int = Field(ge=1, le=5)
    comentario: str | None = Field(default=None, max_length=500)


class AvaliacaoUpdate(BaseModel):
    nota: int | None = Field(default=None, ge=1, le=5)
    comentario: str | None = Field(default=None, max_length=500)


class AvaliacaoResponse(BaseModel):
    id: int
    livro_id: int
    nota: int
    comentario: str | None

    model_config = ConfigDict(from_attributes=True)


class MediaAvaliacoesResponse(BaseModel):
    livro_id: int
    media: float | None
    total_avaliacoes: int
