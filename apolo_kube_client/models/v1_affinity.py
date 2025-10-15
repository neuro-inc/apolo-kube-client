from pydantic import BaseModel, Field

from .v1_node_affinity import V1NodeAffinity
from .v1_pod_affinity import V1PodAffinity
from .v1_pod_anti_affinity import V1PodAntiAffinity


class V1Affinity(BaseModel):
    node_affinity: V1NodeAffinity | None = Field(None, alias="nodeAffinity")

    pod_affinity: V1PodAffinity | None = Field(None, alias="podAffinity")

    pod_anti_affinity: V1PodAntiAffinity | None = Field(None, alias="podAntiAffinity")
