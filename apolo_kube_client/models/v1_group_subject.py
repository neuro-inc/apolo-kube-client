from pydantic import BaseModel


__all__ = ("V1GroupSubject",)


class V1GroupSubject(BaseModel):
    name: str | None = None
