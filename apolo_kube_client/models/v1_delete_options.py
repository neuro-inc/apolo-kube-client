from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_preconditions import V1Preconditions

__all__ = ("V1DeleteOptions",)


class V1DeleteOptions(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    dry_run: list[str] = Field(default_factory=lambda: [], alias="dryRun")

    grace_period_seconds: int | None = Field(
        default_factory=lambda: None, alias="gracePeriodSeconds"
    )

    ignore_store_read_error_with_cluster_breaking_potential: bool | None = Field(
        default_factory=lambda: None,
        alias="ignoreStoreReadErrorWithClusterBreakingPotential",
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    orphan_dependents: bool | None = Field(
        default_factory=lambda: None, alias="orphanDependents"
    )

    preconditions: V1Preconditions = Field(
        default_factory=lambda: V1Preconditions(), alias="preconditions"
    )

    propagation_policy: str | None = Field(
        default_factory=lambda: None, alias="propagationPolicy"
    )
