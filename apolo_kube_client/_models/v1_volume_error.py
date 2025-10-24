from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1VolumeError",)


class V1VolumeError(BaseModel):
    """VolumeError captures an error encountered during a volume operation."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.storage.v1.VolumeError"

    error_code: Annotated[
        int | None,
        Field(
            alias="errorCode",
            description="""errorCode is a numeric gRPC code representing the error encountered during Attach or Detach operations.

This is an optional, beta field that requires the MutableCSINodeAllocatableCount feature gate being enabled to be set.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""message represents the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    time: Annotated[
        datetime | None,
        Field(
            description="""time represents the time the error was encountered.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
