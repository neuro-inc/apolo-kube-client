from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from pydantic import BeforeValidator

__all__ = ("V1PersistentVolumeClaimTemplate",)


class V1PersistentVolumeClaimTemplate(ResourceModel):
    """PersistentVolumeClaimTemplate is used to produce PersistentVolumeClaim objects as part of an EphemeralVolumeSource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.PersistentVolumeClaimTemplate"
    )

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1PersistentVolumeClaimSpec,
        Field(
            description="""The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here."""
        ),
    ]
