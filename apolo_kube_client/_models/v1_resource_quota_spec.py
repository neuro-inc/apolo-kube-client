from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_scope_selector import V1ScopeSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceQuotaSpec",)


class V1ResourceQuotaSpec(BaseModel):
    hard: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    scope_selector: Annotated[
        V1ScopeSelector, BeforeValidator(_default_if_none(V1ScopeSelector))
    ] = Field(
        default_factory=lambda: V1ScopeSelector(),
        serialization_alias="scopeSelector",
        validation_alias=AliasChoices("scope_selector", "scopeSelector"),
    )

    scopes: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
