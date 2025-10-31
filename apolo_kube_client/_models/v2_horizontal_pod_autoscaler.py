from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v2_horizontal_pod_autoscaler_spec import V2HorizontalPodAutoscalerSpec
from .v2_horizontal_pod_autoscaler_status import V2HorizontalPodAutoscalerStatus
from pydantic import BeforeValidator

__all__ = ("V2HorizontalPodAutoscaler",)


class V2HorizontalPodAutoscaler(ResourceModel):
    """HorizontalPodAutoscaler is the configuration for a horizontal pod autoscaler, which automatically manages the replica count of any resource implementing the scale subresource based on the metrics specified."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.HorizontalPodAutoscaler"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="autoscaling", kind="HorizontalPodAutoscaler", version="v2"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "autoscaling/v2"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "HorizontalPodAutoscaler"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V2HorizontalPodAutoscalerSpec | None,
        Field(
            description="""spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    status: Annotated[
        V2HorizontalPodAutoscalerStatus | None,
        Field(
            description="""status is the current information about the autoscaler.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
