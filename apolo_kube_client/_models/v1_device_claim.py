from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_device_claim_configuration import V1DeviceClaimConfiguration
from .v1_device_constraint import V1DeviceConstraint
from .v1_device_request import V1DeviceRequest
from pydantic import BeforeValidator

__all__ = ("V1DeviceClaim",)


class V1DeviceClaim(BaseModel):
    """DeviceClaim defines how to request devices with a ResourceClaim."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.DeviceClaim"

    config: Annotated[
        list[V1DeviceClaimConfiguration],
        Field(
            description="""This field holds configuration for multiple potential drivers which could satisfy requests in this claim. It is ignored while allocating the claim.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    constraints: Annotated[
        list[V1DeviceConstraint],
        Field(
            description="""These constraints must be satisfied by the set of devices that get allocated for the claim.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    requests: Annotated[
        list[V1DeviceRequest],
        Field(
            description="""Requests represent individual requests for distinct devices which must all be satisfied. If empty, nothing needs to be allocated.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
