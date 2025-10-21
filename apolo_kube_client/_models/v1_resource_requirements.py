from pydantic import BaseModel
from .core_v1_resource_claim import CoreV1ResourceClaim
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceRequirements",)


class V1ResourceRequirements(BaseModel):
    claims: Annotated[
        list[CoreV1ResourceClaim], BeforeValidator(_collection_if_none("[]"))
    ] = []

    limits: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    requests: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}
