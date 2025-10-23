from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_preconditions import V1Preconditions
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeleteOptions",)


class V1DeleteOptions(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    dry_run: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[],
        serialization_alias="dryRun",
        validation_alias=AliasChoices("dry_run", "dryRun"),
        exclude_if=_exclude_if,
    )

    grace_period_seconds: int | None = Field(
        default=None,
        serialization_alias="gracePeriodSeconds",
        validation_alias=AliasChoices("grace_period_seconds", "gracePeriodSeconds"),
        exclude_if=_exclude_if,
    )

    ignore_store_read_error_with_cluster_breaking_potential: bool | None = Field(
        default=None,
        serialization_alias="ignoreStoreReadErrorWithClusterBreakingPotential",
        validation_alias=AliasChoices(
            "ignore_store_read_error_with_cluster_breaking_potential",
            "ignoreStoreReadErrorWithClusterBreakingPotential",
        ),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    orphan_dependents: bool | None = Field(
        default=None,
        serialization_alias="orphanDependents",
        validation_alias=AliasChoices("orphan_dependents", "orphanDependents"),
        exclude_if=_exclude_if,
    )

    preconditions: Annotated[
        V1Preconditions, BeforeValidator(_default_if_none(V1Preconditions))
    ] = Field(default_factory=lambda: V1Preconditions(), exclude_if=_exclude_if)

    propagation_policy: str | None = Field(
        default=None,
        serialization_alias="propagationPolicy",
        validation_alias=AliasChoices("propagation_policy", "propagationPolicy"),
        exclude_if=_exclude_if,
    )
