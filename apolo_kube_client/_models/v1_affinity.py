from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_node_affinity import V1NodeAffinity
from .v1_pod_affinity import V1PodAffinity
from .v1_pod_anti_affinity import V1PodAntiAffinity
from pydantic import BeforeValidator

__all__ = ("V1Affinity",)


class V1Affinity(BaseModel):
    """Affinity is a group of affinity scheduling rules."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Affinity"

    node_affinity: Annotated[
        V1NodeAffinity,
        Field(
            alias="nodeAffinity",
            description="""Describes node affinity scheduling rules for the pod.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1NodeAffinity)),
    ] = V1NodeAffinity()

    pod_affinity: Annotated[
        V1PodAffinity,
        Field(
            alias="podAffinity",
            description="""Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1PodAffinity)),
    ] = V1PodAffinity()

    pod_anti_affinity: Annotated[
        V1PodAntiAffinity,
        Field(
            alias="podAntiAffinity",
            description="""Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1PodAntiAffinity)),
    ] = V1PodAntiAffinity()
