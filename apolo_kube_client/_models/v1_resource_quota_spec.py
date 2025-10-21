from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_scope_selector import V1ScopeSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceQuotaSpec",)


class V1ResourceQuotaSpec(BaseModel):
    hard: dict[str, str] = {}

    scope_selector: Annotated[
        V1ScopeSelector, BeforeValidator(_default_if_none(V1ScopeSelector))
    ] = Field(
        default_factory=lambda: V1ScopeSelector(),
        serialization_alias="scopeSelector",
        validation_alias=AliasChoices("scope_selector", "scopeSelector"),
    )

    scopes: list[str] = []
