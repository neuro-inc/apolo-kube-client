from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_custom_resource_definition_spec import V1CustomResourceDefinitionSpec
from .v1_custom_resource_definition_status import V1CustomResourceDefinitionStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceDefinition",)


class V1CustomResourceDefinition(ResourceModel):
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
        V1CustomResourceDefinitionSpec,
        BeforeValidator(_default_if_none(V1CustomResourceDefinitionSpec)),
    ] = Field(
        default_factory=lambda: V1CustomResourceDefinitionSpec(), exclude_if=_exclude_if
    )

    status: Annotated[
        V1CustomResourceDefinitionStatus,
        BeforeValidator(_default_if_none(V1CustomResourceDefinitionStatus)),
    ] = Field(
        default_factory=lambda: V1CustomResourceDefinitionStatus(),
        exclude_if=_exclude_if,
    )
