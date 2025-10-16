from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_preconditions import V1Preconditions

__all__ = ("V1DeleteOptions",)


class V1DeleteOptions(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    dry_run: list[str] | None = Field(None, alias="dryRun")

    grace_period_seconds: int | None = Field(None, alias="gracePeriodSeconds")

    ignore_store_read_error_with_cluster_breaking_potential: bool | None = Field(
        None, alias="ignoreStoreReadErrorWithClusterBreakingPotential"
    )

    kind: str | None = Field(None, alias="kind")

    orphan_dependents: bool | None = Field(None, alias="orphanDependents")

    preconditions: V1Preconditions | None = Field(None, alias="preconditions")

    propagation_policy: str | None = Field(None, alias="propagationPolicy")
