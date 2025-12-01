from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, BeforeValidator, Field

from .utils import _collection_if_none


__all__ = ("V1ServiceCIDRSpec",)


class V1ServiceCIDRSpec(BaseModel):
    """ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.ServiceCIDRSpec"

    cidrs: Annotated[
        list[str],
        Field(
            description="""CIDRs defines the IP blocks in CIDR notation (e.g. "192.168.0.0/24" or "2001:db8::/64") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
