from pydantic import BaseModel, Field

from .v1_c_s_i_node_driver import V1CSINodeDriver


class V1CSINodeSpec(BaseModel):
    drivers: list[V1CSINodeDriver] | None = Field(None, alias="drivers")
