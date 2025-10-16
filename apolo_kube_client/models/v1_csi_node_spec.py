from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_csi_node_driver import V1CSINodeDriver

__all__ = ("V1CSINodeSpec",)


class V1CSINodeSpec(BaseModel):
    drivers: list[V1CSINodeDriver] = Field(default_factory=lambda: [], alias="drivers")
