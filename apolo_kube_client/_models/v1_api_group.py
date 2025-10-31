from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import KubeMeta
from .utils import _collection_if_none
from .v1_group_version_for_discovery import V1GroupVersionForDiscovery
from .v1_server_address_by_client_cidr import V1ServerAddressByClientCIDR
from pydantic import BeforeValidator

__all__ = ("V1APIGroup",)


class V1APIGroup(BaseModel):
    """APIGroup contains the name, the supported versions, and the preferred version of a group."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.APIGroup"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="", kind="APIGroup", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "APIGroup"

    name: Annotated[str, Field(description="""name is the name of the group.""")]

    preferred_version: Annotated[
        V1GroupVersionForDiscovery | None,
        Field(
            alias="preferredVersion",
            description="""preferredVersion is the version preferred by the API server, which probably is the storage version.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    server_address_by_client_cid_rs: Annotated[
        list[V1ServerAddressByClientCIDR],
        Field(
            alias="serverAddressByClientCIDRs",
            description="""a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    versions: Annotated[
        list[V1GroupVersionForDiscovery],
        Field(description="""versions are the versions supported in this group."""),
    ]
