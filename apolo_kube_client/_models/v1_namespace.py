from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_namespace_spec import V1NamespaceSpec
from .v1_namespace_status import V1NamespaceStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Namespace",)


class V1Namespace(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1NamespaceSpec, BeforeValidator(_default_if_none(V1NamespaceSpec))
    ] = Field(default_factory=lambda: V1NamespaceSpec(), exclude_if=_exclude_if)

    status: Annotated[
        V1NamespaceStatus, BeforeValidator(_default_if_none(V1NamespaceStatus))
    ] = Field(default_factory=lambda: V1NamespaceStatus(), exclude_if=_exclude_if)
