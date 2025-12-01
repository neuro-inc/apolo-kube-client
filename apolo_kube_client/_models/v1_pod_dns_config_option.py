from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1PodDNSConfigOption",)


class V1PodDNSConfigOption(BaseConfiguredModel):
    """PodDNSConfigOption defines DNS resolver options of a pod."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodDNSConfigOption"

    name: Annotated[
        str | None,
        Field(
            description="""Name is this DNS resolver option's name. Required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    value: Annotated[
        str | None,
        Field(
            description="""Value is this DNS resolver option's value.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
