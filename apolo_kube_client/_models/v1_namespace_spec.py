from pydantic import BaseModel


__all__ = ("V1NamespaceSpec",)


class V1NamespaceSpec(BaseModel):
    finalizers: list[str] = []
