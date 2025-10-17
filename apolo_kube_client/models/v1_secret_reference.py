from pydantic import BaseModel


__all__ = ("V1SecretReference",)


class V1SecretReference(BaseModel):
    name: str | None = None

    namespace: str | None = None
