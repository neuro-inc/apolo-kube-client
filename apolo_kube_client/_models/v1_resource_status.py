from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_resource_health import V1ResourceHealth
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceStatus",)


class V1ResourceStatus(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    resources: Annotated[
        list[V1ResourceHealth], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
