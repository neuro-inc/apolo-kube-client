from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1beta2_device_claim import V1beta2DeviceClaim
from pydantic import BeforeValidator

__all__ = ("V1beta2ResourceClaimSpec",)


class V1beta2ResourceClaimSpec(BaseModel):
    """ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta2.ResourceClaimSpec"
    )

    devices: Annotated[
        V1beta2DeviceClaim,
        Field(
            description="""Devices defines how to request devices.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1beta2DeviceClaim)),
    ] = V1beta2DeviceClaim()
