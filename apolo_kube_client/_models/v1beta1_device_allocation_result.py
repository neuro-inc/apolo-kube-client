from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base_model import BaseConfiguredModel
from .utils import _collection_if_none
from .v1beta1_device_allocation_configuration import (
    V1beta1DeviceAllocationConfiguration,
)
from .v1beta1_device_request_allocation_result import (
    V1beta1DeviceRequestAllocationResult,
)


__all__ = ("V1beta1DeviceAllocationResult",)


class V1beta1DeviceAllocationResult(BaseConfiguredModel):
    """DeviceAllocationResult is the result of allocating devices."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta1.DeviceAllocationResult"
    )

    config: Annotated[
        list[V1beta1DeviceAllocationConfiguration],
        Field(
            description="""This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.

This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    results: Annotated[
        list[V1beta1DeviceRequestAllocationResult],
        Field(
            description="""Results lists all allocated devices.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
