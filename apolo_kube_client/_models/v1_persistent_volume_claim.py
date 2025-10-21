from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from .v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PersistentVolumeClaim",)


class V1PersistentVolumeClaim(ResourceModel):
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
        V1PersistentVolumeClaimSpec,
        BeforeValidator(_default_if_none(V1PersistentVolumeClaimSpec)),
    ] = Field(default_factory=lambda: V1PersistentVolumeClaimSpec())

    status: Annotated[
        V1PersistentVolumeClaimStatus,
        BeforeValidator(_default_if_none(V1PersistentVolumeClaimStatus)),
    ] = Field(default_factory=lambda: V1PersistentVolumeClaimStatus())
