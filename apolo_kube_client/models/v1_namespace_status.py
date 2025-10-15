from pydantic import BaseModel, Field

from .v1_namespace_condition import V1NamespaceCondition


class V1NamespaceStatus(BaseModel):
    conditions: list[V1NamespaceCondition] | None = Field(None, alias="conditions")

    phase: str | None = Field(None, alias="phase")
