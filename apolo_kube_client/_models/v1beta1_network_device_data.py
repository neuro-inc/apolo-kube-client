from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1beta1NetworkDeviceData",)


class V1beta1NetworkDeviceData(BaseModel):
    """NetworkDeviceData provides network-related details for the allocated device. This information may be filled by drivers or other components to configure or identify the device within a network context."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta1.NetworkDeviceData"
    )

    hardware_address: Annotated[
        str | None,
        Field(
            alias="hardwareAddress",
            description="""HardwareAddress represents the hardware address (e.g. MAC Address) of the device's network interface.

Must not be longer than 128 characters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    interface_name: Annotated[
        str | None,
        Field(
            alias="interfaceName",
            description="""InterfaceName specifies the name of the network interface associated with the allocated device. This might be the name of a physical or virtual network interface being configured in the pod.

Must not be longer than 256 characters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    ips: Annotated[
        list[str],
        Field(
            description="""IPs lists the network addresses assigned to the device's network interface. This can include both IPv4 and IPv6 addresses. The IPs are in the CIDR notation, which includes both the address and the associated subnet mask. e.g.: "192.0.2.5/24" for IPv4 and "2001:db8::5/64" for IPv6.

Must not contain more than 16 entries.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
