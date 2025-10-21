from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_label_selector import V1LabelSelector
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CSIStorageCapacity",)


class V1CSIStorageCapacity(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    capacity: str | None = None

    kind: str | None = None

    maximum_volume_size: str | None = Field(
        default=None,
        serialization_alias="maximumVolumeSize",
        validation_alias=AliasChoices("maximum_volume_size", "maximumVolumeSize"),
    )

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    node_topology: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="nodeTopology",
        validation_alias=AliasChoices("node_topology", "nodeTopology"),
    )

    storage_class_name: str | None = Field(
        default=None,
        serialization_alias="storageClassName",
        validation_alias=AliasChoices("storage_class_name", "storageClassName"),
    )
