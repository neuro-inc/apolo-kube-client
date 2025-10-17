from pydantic import BaseModel


__all__ = ("V1ServiceAccountSubject",)


class V1ServiceAccountSubject(BaseModel):
    name: str | None = None

    namespace: str | None = None
