from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1TopologySelectorLabelRequirement",)


class V1TopologySelectorLabelRequirement(BaseModel):
    """A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

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
