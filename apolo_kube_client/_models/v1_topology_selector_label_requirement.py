from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1TopologySelectorLabelRequirement",)


class V1TopologySelectorLabelRequirement(BaseConfiguredModel):
    """A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.TopologySelectorLabelRequirement"
    )

    key: Annotated[
        str, Field(description="""The label key that the selector applies to.""")
    ]

    values: Annotated[
        list[str],
        Field(
            description="""An array of string values. One value must match the label to be selected. Each entry in Values is ORed."""
        ),
    ]
