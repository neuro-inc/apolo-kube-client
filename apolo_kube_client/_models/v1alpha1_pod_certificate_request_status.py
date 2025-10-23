from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_condition import V1Condition
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1PodCertificateRequestStatus",)


class V1alpha1PodCertificateRequestStatus(BaseModel):
    begin_refresh_at: datetime | None = Field(
        default=None,
        serialization_alias="beginRefreshAt",
        validation_alias=AliasChoices("begin_refresh_at", "beginRefreshAt"),
        exclude_if=_exclude_if,
    )

    certificate_chain: str | None = Field(
        default=None,
        serialization_alias="certificateChain",
        validation_alias=AliasChoices("certificate_chain", "certificateChain"),
        exclude_if=_exclude_if,
    )

    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    not_after: datetime | None = Field(
        default=None,
        serialization_alias="notAfter",
        validation_alias=AliasChoices("not_after", "notAfter"),
        exclude_if=_exclude_if,
    )

    not_before: datetime | None = Field(
        default=None,
        serialization_alias="notBefore",
        validation_alias=AliasChoices("not_before", "notBefore"),
        exclude_if=_exclude_if,
    )
