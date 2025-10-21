from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1RuleWithOperations",)


class V1RuleWithOperations(BaseModel):
    api_groups: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="apiGroups",
            validation_alias=AliasChoices("api_groups", "apiGroups"),
        )
    )

    api_versions: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="apiVersions",
            validation_alias=AliasChoices("api_versions", "apiVersions"),
        )
    )

    operations: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    resources: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    scope: str | None = None
