from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _default_if_none
from .v1_device_claim import V1DeviceClaim


__all__ = ("V1ResourceClaimSpec",)


class V1ResourceClaimSpec(BaseConfiguredModel):
    """ResourceClaimSpec defines what is being requested in a ResourceClaim and how to configure it."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.ResourceClaimSpec"

    devices: Annotated[
        V1DeviceClaim,
        Field(
            description="""Devices defines how to request devices.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1DeviceClaim)),
    ] = V1DeviceClaim()
