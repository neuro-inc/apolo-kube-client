from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1AppArmorProfile",)


class V1AppArmorProfile(BaseConfiguredModel):
    """AppArmorProfile defines a pod or container's AppArmor settings."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.AppArmorProfile"

    localhost_profile: Annotated[
        str | None,
        Field(
            alias="localhostProfile",
            description="""localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str,
        Field(
            description="""type indicates which kind of AppArmor profile will be applied. Valid options are:
  Localhost - a profile pre-loaded on the node.
  RuntimeDefault - the container runtime's default profile.
  Unconfined - no AppArmor enforcement."""
        ),
    ]
