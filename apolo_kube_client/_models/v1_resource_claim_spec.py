from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_device_claim import V1DeviceClaim
from pydantic import BeforeValidator

__all__ = ("V1ResourceClaimSpec",)


class V1ResourceClaimSpec(BaseModel):
    """ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.ResourceClaimSpec"

    devices: Annotated[
        V1DeviceClaim,
        Field(
            description="""Devices defines how to request devices.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1DeviceClaim)),
    ] = V1DeviceClaim()
