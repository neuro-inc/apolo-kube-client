from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_scope_selector import V1ScopeSelector
from pydantic import BeforeValidator

__all__ = ("V1ResourceQuotaSpec",)


class V1ResourceQuotaSpec(BaseModel):
    """ResourceQuotaSpec defines the desired hard limits to enforce for Quota."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ResourceQuotaSpec"

    hard: Annotated[
        dict[str, str],
        Field(
            description="""hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    scope_selector: Annotated[
        V1ScopeSelector,
        Field(
            alias="scopeSelector",
            description="""scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ScopeSelector)),
    ] = V1ScopeSelector()

    scopes: Annotated[
        list[str],
        Field(
            description="""A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
