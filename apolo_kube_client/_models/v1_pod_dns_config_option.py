from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PodDNSConfigOption",)


class V1PodDNSConfigOption(BaseModel):
    """PodDNSConfigOption defines DNS resolver options of a pod."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

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
