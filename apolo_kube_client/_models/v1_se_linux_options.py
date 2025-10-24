from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1SELinuxOptions",)


class V1SELinuxOptions(BaseModel):
    """SELinuxOptions are the labels to be applied to the container"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.SELinuxOptions"

    level: Annotated[
        str | None,
        Field(
            description="""Level is SELinux level label that applies to the container.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    role: Annotated[
        str | None,
        Field(
            description="""Role is a SELinux role label that applies to the container.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str | None,
        Field(
            description="""Type is a SELinux type label that applies to the container.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    user: Annotated[
        str | None,
        Field(
            description="""User is a SELinux user label that applies to the container.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
