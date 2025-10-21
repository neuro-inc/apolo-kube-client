from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1CapacityRequirements",)


class V1beta1CapacityRequirements(BaseModel):
    requests: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}
