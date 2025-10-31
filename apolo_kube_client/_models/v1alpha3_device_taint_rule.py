from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1alpha3_device_taint_rule_spec import V1alpha3DeviceTaintRuleSpec
from pydantic import BeforeValidator

__all__ = ("V1alpha3DeviceTaintRule",)


class V1alpha3DeviceTaintRule(ResourceModel):
    """DeviceTaintRule adds one taint to all devices which match the selector. This has the same effect as if the taint was specified directly in the ResourceSlice by the DRA driver."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1alpha3.DeviceTaintRule"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="resource.k8s.io", kind="DeviceTaintRule", version="v1alpha3"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "resource.k8s.io/v1alpha3"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "DeviceTaintRule"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1alpha3DeviceTaintRuleSpec,
        Field(
            description="""Spec specifies the selector and one taint.

Changing the spec automatically increments the metadata.generation number."""
        ),
    ]
