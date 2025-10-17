from pydantic import AliasChoices, BaseModel, Field
from .v1_component_condition import V1ComponentCondition
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1ComponentStatus",)


class V1ComponentStatus(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    conditions: list[V1ComponentCondition] = []

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())
