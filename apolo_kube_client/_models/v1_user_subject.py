from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1UserSubject",)


class V1UserSubject(BaseModel):
    """UserSubject holds detailed information for user-kind subject."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.flowcontrol.v1.UserSubject"

    name: Annotated[
        str,
        Field(
            description="""`name` is the username that matches, or "*" to match all usernames. Required."""
        ),
    ]
