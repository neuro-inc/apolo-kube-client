from pydantic import Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PersistentVolumeClaimTemplate",)


class V1PersistentVolumeClaimTemplate(ResourceModel):
    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1PersistentVolumeClaimSpec,
        BeforeValidator(_default_if_none(V1PersistentVolumeClaimSpec)),
    ] = Field(default_factory=lambda: V1PersistentVolumeClaimSpec())
