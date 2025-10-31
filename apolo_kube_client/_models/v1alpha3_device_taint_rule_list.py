from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ListModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_list_meta import V1ListMeta
from .v1alpha3_device_taint_rule import V1alpha3DeviceTaintRule
from pydantic import BeforeValidator

__all__ = ("V1alpha3DeviceTaintRuleList",)


class V1alpha3DeviceTaintRuleList(ListModel):
    """DeviceTaintRuleList is a collection of DeviceTaintRules."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1alpha3.DeviceTaintRuleList"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="resource.k8s.io", kind="DeviceTaintRuleList", version="v1alpha3"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "resource.k8s.io/v1alpha3"

    items: Annotated[
        list[V1alpha3DeviceTaintRule],
        Field(description="""Items is the list of DeviceTaintRules."""),
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "DeviceTaintRuleList"

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""Standard list metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
