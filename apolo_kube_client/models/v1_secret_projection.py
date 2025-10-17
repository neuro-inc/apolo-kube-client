from pydantic import BaseModel
from .v1_key_to_path import V1KeyToPath

__all__ = ("V1SecretProjection",)


class V1SecretProjection(BaseModel):
    items: list[V1KeyToPath] = []

    name: str | None = None

    optional: bool | None = None
