from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_device_sub_request import V1DeviceSubRequest
from .v1_exact_device_request import V1ExactDeviceRequest
from pydantic import BeforeValidator

__all__ = ("V1DeviceRequest",)


class V1DeviceRequest(BaseModel):
    """DeviceRequest is a request for devices required for a claim. This is typically a request for a single resource like a device, but can also ask for several identical devices. With FirstAvailable it is also possible to provide a prioritized list of requests."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.DeviceRequest"

    exactly: Annotated[
        V1ExactDeviceRequest | None,
        Field(
            description="""Exactly specifies the details for a single request that must be met exactly for the request to be satisfied.

One of Exactly or FirstAvailable must be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    first_available: Annotated[
        list[V1DeviceSubRequest],
        Field(
            alias="firstAvailable",
            description="""FirstAvailable contains subrequests, of which exactly one will be selected by the scheduler. It tries to satisfy them in the order in which they are listed here. So if there are two entries in the list, the scheduler will only check the second one if it determines that the first one can not be used.

DRA does not yet implement scoring, so the scheduler will select the first set of devices that satisfies all the requests in the claim. And if the requirements can be satisfied on more than one node, other scheduling features will determine which node is chosen. This means that the set of devices allocated to a claim might not be the optimal set available to the cluster. Scoring will be implemented later.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    name: Annotated[
        str,
        Field(
            description="""Name can be used to reference this request in a pod.spec.containers[].resources.claims entry and in a constraint of the claim.

References using the name in the DeviceRequest will uniquely identify a request when the Exactly field is set. When the FirstAvailable field is set, a reference to the name of the DeviceRequest will match whatever subrequest is chosen by the scheduler.

Must be a DNS label."""
        ),
    ]
