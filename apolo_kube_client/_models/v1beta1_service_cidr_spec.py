from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1ServiceCIDRSpec",)


class V1beta1ServiceCIDRSpec(BaseModel):
    cidrs: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
