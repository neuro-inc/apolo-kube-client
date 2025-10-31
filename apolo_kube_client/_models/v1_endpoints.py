from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_endpoint_subset import V1EndpointSubset
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator

__all__ = ("V1Endpoints",)


class V1Endpoints(ResourceModel):
    """Endpoints is a collection of endpoints that implement the actual service. Example:

             Name: "mysvc",
             Subsets: [
               {
                 Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
                 Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
               },
               {
                 Addresses: [{"ip": "10.10.3.3"}],
                 Ports: [{"name": "a", "port": 93}, {"name": "b", "port": 76}]
               },
            ]

    Endpoints is a legacy API and does not contain information about all Service features. Use discoveryv1.EndpointSlice for complete information about Service endpoints.

    Deprecated: This API is deprecated in v1.33+. Use discoveryv1.EndpointSlice."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Endpoints"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="", kind="Endpoints", version="v1"
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
    ] = "Endpoints"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    subsets: Annotated[
        list[V1EndpointSubset],
        Field(
            description="""The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
