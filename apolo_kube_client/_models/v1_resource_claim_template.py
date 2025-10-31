from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_resource_claim_template_spec import V1ResourceClaimTemplateSpec
from pydantic import BeforeValidator

__all__ = ("V1ResourceClaimTemplate",)


class V1ResourceClaimTemplate(ResourceModel):
    """ResourceClaimTemplate is used to produce ResourceClaim objects.

    This is an alpha type and requires enabling the DynamicResourceAllocation feature gate."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1.ResourceClaimTemplate"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="resource.k8s.io", kind="ResourceClaimTemplate", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "resource.k8s.io/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "ResourceClaimTemplate"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1ResourceClaimTemplateSpec,
        Field(
            description="""Describes the ResourceClaim that is to be generated.

This field is immutable. A ResourceClaim will get created by the control plane for a Pod when needed and then not get updated anymore."""
        ),
    ]
