from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_replication_controller_spec import V1ReplicationControllerSpec
from .v1_replication_controller_status import V1ReplicationControllerStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ReplicationController",)


class V1ReplicationController(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1ReplicationControllerSpec,
        BeforeValidator(_default_if_none(V1ReplicationControllerSpec)),
    ] = Field(default_factory=lambda: V1ReplicationControllerSpec())

    status: Annotated[
        V1ReplicationControllerStatus,
        BeforeValidator(_default_if_none(V1ReplicationControllerStatus)),
    ] = Field(default_factory=lambda: V1ReplicationControllerStatus())
