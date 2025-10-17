from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_stateful_set_spec import V1StatefulSetSpec
from .v1_stateful_set_status import V1StatefulSetStatus

__all__ = ("V1StatefulSet",)


class V1StatefulSet(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1StatefulSetSpec = Field(default_factory=lambda: V1StatefulSetSpec())

    status: V1StatefulSetStatus = Field(default_factory=lambda: V1StatefulSetStatus())
