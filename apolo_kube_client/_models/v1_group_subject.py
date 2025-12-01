from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1GroupSubject",)


class V1GroupSubject(BaseConfiguredModel):
    """GroupSubject holds detailed information for group-kind subject."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.flowcontrol.v1.GroupSubject"

    name: Annotated[
        str,
        Field(
            description="""name is the user group that matches, or "*" to match all user groups. See https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go for some well-known group names. Required."""
        ),
    ]
