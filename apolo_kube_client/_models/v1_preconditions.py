from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1Preconditions",)


class V1Preconditions(BaseModel):
    """Preconditions must be fulfilled before an operation (update, delete, etc.) is carried out."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apimachinery.pkg.apis.meta.v1.Preconditions"
    )

    resource_version: Annotated[
        str | None,
        Field(
            alias="resourceVersion",
            description="""Specifies the target ResourceVersion""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    uid: Annotated[
        str | None,
        Field(
            description="""Specifies the target UID.""", exclude_if=lambda v: v is None
        ),
    ] = None
