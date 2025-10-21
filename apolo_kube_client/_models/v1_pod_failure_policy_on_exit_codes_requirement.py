from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodFailurePolicyOnExitCodesRequirement",)


class V1PodFailurePolicyOnExitCodesRequirement(BaseModel):
    container_name: str | None = Field(
        default=None,
        serialization_alias="containerName",
        validation_alias=AliasChoices("container_name", "containerName"),
    )

    operator: str | None = None

    values: Annotated[list[int], BeforeValidator(_collection_if_none("[]"))] = []
