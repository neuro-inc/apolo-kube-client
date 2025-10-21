from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_persistent_volume_claim_template import V1PersistentVolumeClaimTemplate
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EphemeralVolumeSource",)


class V1EphemeralVolumeSource(BaseModel):
    volume_claim_template: Annotated[
        V1PersistentVolumeClaimTemplate,
        BeforeValidator(_default_if_none(V1PersistentVolumeClaimTemplate)),
    ] = Field(
        default_factory=lambda: V1PersistentVolumeClaimTemplate(),
        serialization_alias="volumeClaimTemplate",
        validation_alias=AliasChoices("volume_claim_template", "volumeClaimTemplate"),
    )
