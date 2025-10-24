from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ExternalDocumentation",)


class V1ExternalDocumentation(BaseModel):
    """ExternalDocumentation allows referencing an external resource for extended documentation."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.ExternalDocumentation"
    )

    description: Annotated[str | None, Field(exclude_if=lambda v: v is None)] = None

    url: Annotated[str | None, Field(exclude_if=lambda v: v is None)] = None
