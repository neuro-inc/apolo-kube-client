from pydantic import BaseModel


__all__ = ("V1KeyToPath",)


class V1KeyToPath(BaseModel):
    key: str | None = None

    mode: int | None = None

    path: str | None = None
