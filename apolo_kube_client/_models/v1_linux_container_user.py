from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LinuxContainerUser",)


class V1LinuxContainerUser(BaseModel):
    gid: int | None = None

    supplemental_groups: Annotated[
        list[int], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="supplementalGroups",
        validation_alias=AliasChoices("supplemental_groups", "supplementalGroups"),
    )

    uid: int | None = None
