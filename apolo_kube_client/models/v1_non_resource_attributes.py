from pydantic import BaseModel


__all__ = ("V1NonResourceAttributes",)


class V1NonResourceAttributes(BaseModel):
    path: str | None = None

    verb: str | None = None
