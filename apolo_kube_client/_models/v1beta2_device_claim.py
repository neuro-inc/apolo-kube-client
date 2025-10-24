from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1beta2_device_claim_configuration import V1beta2DeviceClaimConfiguration
from .v1beta2_device_constraint import V1beta2DeviceConstraint
from .v1beta2_device_request import V1beta2DeviceRequest
from pydantic import BeforeValidator

__all__ = ("V1beta2DeviceClaim",)


class V1beta2DeviceClaim(BaseModel):
    """DeviceClaim defines how to request devices with a ResourceClaim."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta2.DeviceClaim"

    config: Annotated[
        list[V1beta2DeviceClaimConfiguration],
        Field(
            description="""This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    constraints: Annotated[
        list[V1beta2DeviceConstraint],
        Field(
            description="""These constraints must be satisfied by the set of devices that get allocated for the claim.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    requests: Annotated[
        list[V1beta2DeviceRequest],
        Field(
            description="""Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
