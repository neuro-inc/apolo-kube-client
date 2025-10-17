from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_namespace_spec import V1NamespaceSpec
from .v1_namespace_status import V1NamespaceStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Namespace",)


class V1Namespace(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1NamespaceSpec = Field(default_factory=lambda: V1NamespaceSpec())

    status: V1NamespaceStatus = Field(default_factory=lambda: V1NamespaceStatus())
