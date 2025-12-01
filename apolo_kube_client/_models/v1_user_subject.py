from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1UserSubject",)


class V1UserSubject(BaseConfiguredModel):
    """UserSubject holds detailed information for user-kind subject."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.flowcontrol.v1.UserSubject"

    name: Annotated[
        str,
        Field(
            description="""`name` is the username that matches, or "*" to match all usernames. Required."""
        ),
    ]
