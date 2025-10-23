from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_node_spec import V1NodeSpec
from .v1_node_status import V1NodeStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Node",)


class V1Node(ResourceModel):
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

    spec: Annotated[V1NodeSpec, BeforeValidator(_default_if_none(V1NodeSpec))] = Field(
        default_factory=lambda: V1NodeSpec(), exclude_if=_exclude_if
    )

    status: Annotated[V1NodeStatus, BeforeValidator(_default_if_none(V1NodeStatus))] = (
        Field(default_factory=lambda: V1NodeStatus(), exclude_if=_exclude_if)
    )
