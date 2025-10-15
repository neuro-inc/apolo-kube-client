from pydantic import BaseModel, Field

from .v1_node_selector import V1NodeSelector


class V1VolumeNodeAffinity(BaseModel):
    required: V1NodeSelector | None = Field(None, alias="required")
