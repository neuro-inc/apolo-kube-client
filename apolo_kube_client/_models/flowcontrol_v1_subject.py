from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_group_subject import V1GroupSubject
from .v1_service_account_subject import V1ServiceAccountSubject
from .v1_user_subject import V1UserSubject
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("FlowcontrolV1Subject",)


class FlowcontrolV1Subject(BaseModel):
    group: Annotated[
        V1GroupSubject, BeforeValidator(_default_if_none(V1GroupSubject))
    ] = Field(default_factory=lambda: V1GroupSubject())

    kind: str | None = None

    service_account: Annotated[
        V1ServiceAccountSubject,
        BeforeValidator(_default_if_none(V1ServiceAccountSubject)),
    ] = Field(
        default_factory=lambda: V1ServiceAccountSubject(),
        serialization_alias="serviceAccount",
        validation_alias=AliasChoices("service_account", "serviceAccount"),
    )

    user: Annotated[V1UserSubject, BeforeValidator(_default_if_none(V1UserSubject))] = (
        Field(default_factory=lambda: V1UserSubject())
    )
