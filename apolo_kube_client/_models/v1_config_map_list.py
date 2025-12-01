from typing import Annotated, ClassVar, Final

from pydantic import BeforeValidator, Field

from .base import CollectionModel
from .utils import KubeMeta, _default_if_none
from .v1_config_map import V1ConfigMap
from .v1_list_meta import V1ListMeta


__all__ = ("V1ConfigMapList",)


class V1ConfigMapList(CollectionModel[V1ConfigMap]):
    """ConfigMapList is a resource containing a list of ConfigMap objects."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ConfigMapList"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="", kind="ConfigMapList", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "v1"

    items: Annotated[
        list[V1ConfigMap], Field(description="""Items is the list of ConfigMaps.""")
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "ConfigMapList"

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
