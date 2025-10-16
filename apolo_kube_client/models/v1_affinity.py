from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_affinity import V1NodeAffinity
from .v1_pod_affinity import V1PodAffinity
from .v1_pod_anti_affinity import V1PodAntiAffinity

__all__ = ("V1Affinity",)


class V1Affinity(BaseModel):
    node_affinity: V1NodeAffinity = Field(
        default_factory=lambda: V1NodeAffinity(), alias="nodeAffinity"
    )

    pod_affinity: V1PodAffinity = Field(
        default_factory=lambda: V1PodAffinity(), alias="podAffinity"
    )

    pod_anti_affinity: V1PodAntiAffinity = Field(
        default_factory=lambda: V1PodAntiAffinity(), alias="podAntiAffinity"
    )
