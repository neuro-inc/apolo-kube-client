from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Overhead",)


class V1Overhead(BaseModel):
    pod_fixed: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = (
        Field(
            default={},
            serialization_alias="podFixed",
            validation_alias=AliasChoices("pod_fixed", "podFixed"),
        )
    )
