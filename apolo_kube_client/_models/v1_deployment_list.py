from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ListModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_deployment import V1Deployment
from .v1_list_meta import V1ListMeta
from pydantic import BeforeValidator

__all__ = ("V1DeploymentList",)


class V1DeploymentList(ListModel):
    """DeploymentList is a list of Deployments."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.DeploymentList"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="apps", kind="DeploymentList", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "apps/v1"

    items: Annotated[
        list[V1Deployment], Field(description="""Items is the list of Deployments.""")
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "DeploymentList"

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""Standard list metadata.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
