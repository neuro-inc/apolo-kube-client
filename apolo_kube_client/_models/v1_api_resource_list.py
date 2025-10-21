from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_api_resource import V1APIResource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1APIResourceList",)


class V1APIResourceList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    group_version: str | None = Field(
        default=None,
        serialization_alias="groupVersion",
        validation_alias=AliasChoices("group_version", "groupVersion"),
    )

    kind: str | None = None

    resources: Annotated[
        list[V1APIResource], BeforeValidator(_collection_if_none("[]"))
    ] = []
