from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_scale_spec import V1ScaleSpec
from .v1_scale_status import V1ScaleStatus
from pydantic import BeforeValidator

__all__ = ("V1Scale",)


class V1Scale(ResourceModel):
    """Scale represents a scaling request for a resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v1.Scale"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="autoscaling", kind="Scale", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "autoscaling/v1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "Scale"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1ScaleSpec,
        Field(
            description="""spec defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ScaleSpec)),
    ] = V1ScaleSpec()

    status: Annotated[
        V1ScaleStatus | None,
        Field(
            description="""status is the current status of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. Read-only.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
