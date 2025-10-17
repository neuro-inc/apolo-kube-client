from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_group_subject import V1GroupSubject
from .v1_service_account_subject import V1ServiceAccountSubject
from .v1_user_subject import V1UserSubject

__all__ = ("FlowcontrolV1Subject",)


class FlowcontrolV1Subject(BaseModel):
    group: V1GroupSubject = Field(default_factory=lambda: V1GroupSubject())

    kind: str | None = Field(default=None)

    service_account: V1ServiceAccountSubject = Field(
        default_factory=lambda: V1ServiceAccountSubject(),
        serialization_alias="serviceAccount",
        validation_alias=AliasChoices("service_account", "serviceAccount"),
    )

    user: V1UserSubject = Field(default_factory=lambda: V1UserSubject())
