from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator

__all__ = ("V1PriorityClass",)


class V1PriorityClass(ResourceModel):
    """PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.scheduling.v1.PriorityClass"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="scheduling.k8s.io", kind="PriorityClass", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "scheduling.k8s.io/v1"

    description: Annotated[
        str | None,
        Field(
            description="""description is an arbitrary string that usually provides guidelines on when this priority class should be used.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    global_default: Annotated[
        bool | None,
        Field(
            alias="globalDefault",
            description="""globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "PriorityClass"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    preemption_policy: Annotated[
        str | None,
        Field(
            alias="preemptionPolicy",
            description="""preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    value: Annotated[
        int,
        Field(
            description="""value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec."""
        ),
    ]
