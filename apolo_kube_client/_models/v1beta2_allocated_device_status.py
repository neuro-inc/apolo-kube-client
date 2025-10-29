from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_condition import V1Condition
from .v1beta2_network_device_data import V1beta2NetworkDeviceData
from apolo_kube_client._typedefs import JsonType
from pydantic import BeforeValidator

__all__ = ("V1beta2AllocatedDeviceStatus",)


class V1beta2AllocatedDeviceStatus(BaseModel):
    """AllocatedDeviceStatus contains the status of an allocated device, if the driver chooses to report it. This may include driver-specific information.

    The combination of Driver, Pool, Device, and ShareID must match the corresponding key in Status.Allocation.Devices."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta2.AllocatedDeviceStatus"
    )

    conditions: Annotated[
        list[V1Condition],
        Field(
            description="""Conditions contains the latest observation of the device's state. If the device has been configured according to the class and claim config references, the `Ready` condition should be True.

Must not contain more than 8 entries.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    data: Annotated[
        JsonType,
        Field(
            description="""Data contains arbitrary driver-specific data.

The length of the raw data must be smaller or equal to 10 Ki.""",
            exclude_if=lambda v: v == {},
        ),
    ] = {}

    device: Annotated[
        str,
        Field(
            description="""Device references one device instance via its name in the driver's resource pool. It must be a DNS label."""
        ),
    ]

    driver: Annotated[
        str,
        Field(
            description="""Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.

Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver."""
        ),
    ]

    network_data: Annotated[
        V1beta2NetworkDeviceData,
        Field(
            alias="networkData",
            description="""NetworkData contains network-related information specific to the device.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1beta2NetworkDeviceData)),
    ] = V1beta2NetworkDeviceData()

    pool: Annotated[
        str,
        Field(
            description="""This name together with the driver name and the device name field identify which device was allocated (`<driver name>/<pool name>/<device name>`).

Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes."""
        ),
    ]

    share_id: Annotated[
        str | None,
        Field(
            alias="shareID",
            description="""ShareID uniquely identifies an individual allocation share of the device.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
