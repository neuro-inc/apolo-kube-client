from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_horizontal_pod_autoscaler_spec import V1HorizontalPodAutoscalerSpec
from .v1_horizontal_pod_autoscaler_status import V1HorizontalPodAutoscalerStatus
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator

__all__ = ("V1HorizontalPodAutoscaler",)


class V1HorizontalPodAutoscaler(ResourceModel):
    """configuration of a horizontal pod autoscaler."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v1.HorizontalPodAutoscaler"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="autoscaling", kind="HorizontalPodAutoscaler", version="v1"
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
    ] = "HorizontalPodAutoscaler"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1HorizontalPodAutoscalerSpec | None,
        Field(
            description="""spec defines the behaviour of autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        V1HorizontalPodAutoscalerStatus | None,
        Field(
            description="""status is the current information about the autoscaler.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
