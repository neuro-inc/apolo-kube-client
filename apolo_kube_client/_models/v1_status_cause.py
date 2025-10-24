from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1StatusCause",)


class V1StatusCause(BaseModel):
    """StatusCause provides more information about an api.Status failure, including cases when multiple errors are encountered."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.StatusCause"
    )

    field: Annotated[
        str | None,
        Field(
            description='''The field of the resource that has caused this error, as named by its JSON serialization. May include dot and postfix notation for nested attributes. Arrays are zero-indexed.  Fields may appear more than once in an array of causes due to fields having multiple errors. Optional.

Examples:
  "name" - the field "name" on the current resource
  "items[0].name" - the field "name" on the first array entry in "items"''',
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""A human-readable description of the cause of the error.  This field may be presented as-is to a reader.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""A machine-readable description of the cause of the error. If this value is empty there is no information available.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
