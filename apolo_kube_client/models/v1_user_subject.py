from pydantic import BaseModel


__all__ = ("V1UserSubject",)


class V1UserSubject(BaseModel):
    name: str | None = None
