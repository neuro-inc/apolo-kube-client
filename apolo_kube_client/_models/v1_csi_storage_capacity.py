from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    capacity: str | None = Field(default=None, exclude_if=_exclude_if)

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    maximum_volume_size: str | None = Field(
        default=None,
        serialization_alias="maximumVolumeSize",
        validation_alias=AliasChoices("maximum_volume_size", "maximumVolumeSize"),
        exclude_if=_exclude_if,
    )

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    node_topology: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="nodeTopology",
        validation_alias=AliasChoices("node_topology", "nodeTopology"),
        exclude_if=_exclude_if,
    )

    storage_class_name: str | None = Field(
        default=None,
        serialization_alias="storageClassName",
        validation_alias=AliasChoices("storage_class_name", "storageClassName"),
        exclude_if=_exclude_if,
    )
