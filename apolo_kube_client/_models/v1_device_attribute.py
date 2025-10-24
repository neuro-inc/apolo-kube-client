from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1DeviceAttribute",)


class V1DeviceAttribute(BaseModel):
    """DeviceAttribute must have exactly one field set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1.DeviceAttribute"

    bool_: Annotated[
        bool | None,
        Field(
            alias="bool",
            description="""BoolValue is a true/false value.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    int_: Annotated[
        int | None,
        Field(
            alias="int",
            description="""IntValue is a number.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    string: Annotated[
        str | None,
        Field(
            description="""StringValue is a string. Must not be longer than 64 characters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    version: Annotated[
        str | None,
        Field(
            description="""VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer than 64 characters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
