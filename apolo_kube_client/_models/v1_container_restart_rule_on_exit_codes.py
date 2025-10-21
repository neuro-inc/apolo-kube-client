from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ContainerRestartRuleOnExitCodes",)


class V1ContainerRestartRuleOnExitCodes(BaseModel):
    operator: str | None = None

    values: Annotated[list[int], BeforeValidator(_collection_if_none("[]"))] = []
