from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
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
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[V1NodeSpec, BeforeValidator(_default_if_none(V1NodeSpec))] = Field(
        default_factory=lambda: V1NodeSpec()
    )

    status: Annotated[V1NodeStatus, BeforeValidator(_default_if_none(V1NodeStatus))] = (
        Field(default_factory=lambda: V1NodeStatus())
    )
