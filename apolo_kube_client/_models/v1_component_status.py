from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_component_condition import V1ComponentCondition
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator

__all__ = ("V1ComponentStatus",)


class V1ComponentStatus(ResourceModel):
    """ComponentStatus (and ComponentStatusList) holds the cluster validation info. Deprecated: This API is deprecated in v1.19+"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ComponentStatus"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="", kind="ComponentStatus", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "v1"

    conditions: Annotated[
        list[V1ComponentCondition],
        Field(
            description="""List of component conditions observed""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "ComponentStatus"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()
