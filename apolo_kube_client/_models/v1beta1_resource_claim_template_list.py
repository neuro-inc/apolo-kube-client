from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ListModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_list_meta import V1ListMeta
from .v1beta1_resource_claim_template import V1beta1ResourceClaimTemplate
from pydantic import BeforeValidator

__all__ = ("V1beta1ResourceClaimTemplateList",)


class V1beta1ResourceClaimTemplateList(ListModel):
    """ResourceClaimTemplateList is a collection of claim templates."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta1.ResourceClaimTemplateList"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="resource.k8s.io", kind="ResourceClaimTemplateList", version="v1beta1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "resource.k8s.io/v1beta1"

    items: Annotated[
        list[V1beta1ResourceClaimTemplate],
        Field(description="""Items is the list of resource claim templates."""),
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "ResourceClaimTemplateList"

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""Standard list metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
