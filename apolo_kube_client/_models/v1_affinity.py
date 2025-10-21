from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_node_affinity import V1NodeAffinity
from .v1_pod_affinity import V1PodAffinity
from .v1_pod_anti_affinity import V1PodAntiAffinity
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Affinity",)


class V1Affinity(BaseModel):
    node_affinity: Annotated[
        V1NodeAffinity, BeforeValidator(_default_if_none(V1NodeAffinity))
    ] = Field(
        default_factory=lambda: V1NodeAffinity(),
        serialization_alias="nodeAffinity",
        validation_alias=AliasChoices("node_affinity", "nodeAffinity"),
    )

    pod_affinity: Annotated[
        V1PodAffinity, BeforeValidator(_default_if_none(V1PodAffinity))
    ] = Field(
        default_factory=lambda: V1PodAffinity(),
        serialization_alias="podAffinity",
        validation_alias=AliasChoices("pod_affinity", "podAffinity"),
    )

    pod_anti_affinity: Annotated[
        V1PodAntiAffinity, BeforeValidator(_default_if_none(V1PodAntiAffinity))
    ] = Field(
        default_factory=lambda: V1PodAntiAffinity(),
        serialization_alias="podAntiAffinity",
        validation_alias=AliasChoices("pod_anti_affinity", "podAntiAffinity"),
    )
