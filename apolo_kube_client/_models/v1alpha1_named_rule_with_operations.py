from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1NamedRuleWithOperations",)


class V1alpha1NamedRuleWithOperations(BaseModel):
    api_groups: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="apiGroups",
            validation_alias=AliasChoices("api_groups", "apiGroups"),
            exclude_if=_exclude_if,
        )
    )

    api_versions: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="apiVersions",
            validation_alias=AliasChoices("api_versions", "apiVersions"),
            exclude_if=_exclude_if,
        )
    )

    operations: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    resource_names: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="resourceNames",
            validation_alias=AliasChoices("resource_names", "resourceNames"),
            exclude_if=_exclude_if,
        )
    )

    resources: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    scope: str | None = Field(default=None, exclude_if=_exclude_if)
