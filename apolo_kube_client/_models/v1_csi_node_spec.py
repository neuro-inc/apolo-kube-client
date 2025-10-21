from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_csi_node_driver import V1CSINodeDriver
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CSINodeSpec",)


class V1CSINodeSpec(BaseModel):
    drivers: Annotated[
        list[V1CSINodeDriver], BeforeValidator(_collection_if_none("[]"))
    ] = []
