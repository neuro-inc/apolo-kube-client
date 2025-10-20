from pydantic import BaseModel
from .v1_csi_node_driver import V1CSINodeDriver

__all__ = ("V1CSINodeSpec",)


class V1CSINodeSpec(BaseModel):
    drivers: list[V1CSINodeDriver] = []
