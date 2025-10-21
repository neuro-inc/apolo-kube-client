from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1VolumeResourceRequirements",)


class V1VolumeResourceRequirements(BaseModel):
    limits: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    requests: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}
