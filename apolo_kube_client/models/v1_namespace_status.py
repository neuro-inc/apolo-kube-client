from pydantic import BaseModel
from .v1_namespace_condition import V1NamespaceCondition

__all__ = ("V1NamespaceStatus",)


class V1NamespaceStatus(BaseModel):
    conditions: list[V1NamespaceCondition] = []

    phase: str | None = None
