from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ListModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_list_meta import V1ListMeta
from .v2_horizontal_pod_autoscaler import V2HorizontalPodAutoscaler
from pydantic import BeforeValidator

__all__ = ("V2HorizontalPodAutoscalerList",)


class V2HorizontalPodAutoscalerList(ListModel):
    """HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects."""

    model_config = ConfigDict(
        extra="forbid", validate_by_alias=True, validate_by_name=True
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerList"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="autoscaling", kind="HorizontalPodAutoscalerList", version="v2"
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    items: Annotated[
        list[V2HorizontalPodAutoscaler],
        Field(
            description="""items is the list of horizontal pod autoscaler objects."""
        ),
    ]

    kind: Annotated[
        str | None,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""metadata is the standard list metadata.""",
            exclude_if=lambda v: v == V1ListMeta(),
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
