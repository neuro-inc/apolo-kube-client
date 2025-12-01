from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base import CollectionModel
from .utils import KubeMeta, _default_if_none
from .v1_csi_driver import V1CSIDriver
from .v1_list_meta import V1ListMeta


__all__ = ("V1CSIDriverList",)


class V1CSIDriverList(CollectionModel[V1CSIDriver]):
    """CSIDriverList is a collection of CSIDriver objects."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.storage.v1.CSIDriverList"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="storage.k8s.io", kind="CSIDriverList", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "storage.k8s.io/v1"

    items: Annotated[
        list[V1CSIDriver], Field(description="""items is the list of CSIDriver""")
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "CSIDriverList"

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""Standard list metadata More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
