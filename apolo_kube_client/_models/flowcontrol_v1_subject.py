from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_group_subject import V1GroupSubject
from .v1_service_account_subject import V1ServiceAccountSubject
from .v1_user_subject import V1UserSubject

__all__ = ("FlowcontrolV1Subject",)


class FlowcontrolV1Subject(BaseModel):
    """Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.flowcontrol.v1.Subject"

    group: Annotated[
        V1GroupSubject | None,
        Field(
            description="""`group` matches based on user group name.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str,
        Field(
            description="""`kind` indicates which one of the other fields is non-empty. Required"""
        ),
    ]

    service_account: Annotated[
        V1ServiceAccountSubject | None,
        Field(
            alias="serviceAccount",
            description="""`serviceAccount` matches ServiceAccounts.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    user: Annotated[
        V1UserSubject | None,
        Field(
            description="""`user` matches based on username.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
