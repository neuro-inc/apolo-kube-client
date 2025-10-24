from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1UserInfo",)


class V1UserInfo(BaseModel):
    """UserInfo holds the information about the user needed to implement the user.Info interface."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.authentication.v1.UserInfo"

    extra: Annotated[
        dict[str, list[str]],
        Field(
            description="""Any additional information provided by the authenticator.""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    groups: Annotated[
        list[str],
        Field(
            description="""The names of groups this user is a part of.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    uid: Annotated[
        str | None,
        Field(
            description="""A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    username: Annotated[
        str | None,
        Field(
            description="""The name that uniquely identifies this user among all active users.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
