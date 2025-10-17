from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_condition import V1Condition
from datetime import datetime

__all__ = ("V1alpha1PodCertificateRequestStatus",)


class V1alpha1PodCertificateRequestStatus(BaseModel):
    begin_refresh_at: datetime | None = Field(
        default=None,
        serialization_alias="beginRefreshAt",
        validation_alias=AliasChoices("begin_refresh_at", "beginRefreshAt"),
    )

    certificate_chain: str | None = Field(
        default=None,
        serialization_alias="certificateChain",
        validation_alias=AliasChoices("certificate_chain", "certificateChain"),
    )

    conditions: list[V1Condition] = Field(default=[])

    not_after: datetime | None = Field(
        default=None,
        serialization_alias="notAfter",
        validation_alias=AliasChoices("not_after", "notAfter"),
    )

    not_before: datetime | None = Field(
        default=None,
        serialization_alias="notBefore",
        validation_alias=AliasChoices("not_before", "notBefore"),
    )
