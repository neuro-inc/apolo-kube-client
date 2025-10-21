from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_resource_health import V1ResourceHealth
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceStatus",)


class V1ResourceStatus(BaseModel):
    name: str | None = None

    resources: Annotated[
        list[V1ResourceHealth], BeforeValidator(_collection_if_none("[]"))
    ] = []
