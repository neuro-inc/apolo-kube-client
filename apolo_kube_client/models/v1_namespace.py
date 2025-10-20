from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_namespace_spec import V1NamespaceSpec
from .v1_namespace_status import V1NamespaceStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Namespace",)


class V1Namespace(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1NamespaceSpec = Field(default_factory=lambda: V1NamespaceSpec())

    status: V1NamespaceStatus = Field(default_factory=lambda: V1NamespaceStatus())
