from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_preconditions import V1Preconditions
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeleteOptions",)


class V1DeleteOptions(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    dry_run: list[str] = Field(
        default=[],
        serialization_alias="dryRun",
        validation_alias=AliasChoices("dry_run", "dryRun"),
    )

    grace_period_seconds: int | None = Field(
        default=None,
        serialization_alias="gracePeriodSeconds",
        validation_alias=AliasChoices("grace_period_seconds", "gracePeriodSeconds"),
    )

    ignore_store_read_error_with_cluster_breaking_potential: bool | None = Field(
        default=None,
        serialization_alias="ignoreStoreReadErrorWithClusterBreakingPotential",
        validation_alias=AliasChoices(
            "ignore_store_read_error_with_cluster_breaking_potential",
            "ignoreStoreReadErrorWithClusterBreakingPotential",
        ),
    )

    kind: str | None = None

    orphan_dependents: bool | None = Field(
        default=None,
        serialization_alias="orphanDependents",
        validation_alias=AliasChoices("orphan_dependents", "orphanDependents"),
    )

    preconditions: Annotated[
        V1Preconditions, BeforeValidator(_default_if_none(V1Preconditions))
    ] = Field(default_factory=lambda: V1Preconditions())

    propagation_policy: str | None = Field(
        default=None,
        serialization_alias="propagationPolicy",
        validation_alias=AliasChoices("propagation_policy", "propagationPolicy"),
    )
