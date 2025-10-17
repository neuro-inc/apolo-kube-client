from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_condition import V1Condition
from datetime import datetime

__all__ = ("V1alpha1PodCertificateRequestStatus",)


class V1alpha1PodCertificateRequestStatus(BaseModel):
    begin_refresh_at: datetime | None = Field(
        default_factory=lambda: None, alias="beginRefreshAt"
    )

    certificate_chain: str | None = Field(
        default_factory=lambda: None, alias="certificateChain"
    )

    conditions: list[V1Condition] = Field(default_factory=lambda: [])

    not_after: datetime | None = Field(default_factory=lambda: None, alias="notAfter")

    not_before: datetime | None = Field(default_factory=lambda: None, alias="notBefore")
