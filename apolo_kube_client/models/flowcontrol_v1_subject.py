from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_group_subject import V1GroupSubject
from .v1_service_account_subject import V1ServiceAccountSubject
from .v1_user_subject import V1UserSubject

__all__ = ("FlowcontrolV1Subject",)


class FlowcontrolV1Subject(BaseModel):
    group: V1GroupSubject = Field(
        default_factory=lambda: V1GroupSubject(), alias="group"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    service_account: V1ServiceAccountSubject = Field(
        default_factory=lambda: V1ServiceAccountSubject(), alias="serviceAccount"
    )

    user: V1UserSubject = Field(default_factory=lambda: V1UserSubject(), alias="user")
