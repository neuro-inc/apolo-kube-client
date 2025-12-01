from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1ExternalDocumentation",)


class V1ExternalDocumentation(BaseConfiguredModel):
    """ExternalDocumentation allows referencing an external resource for extended documentation."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.ExternalDocumentation"
    )

    description: Annotated[str | None, Field(exclude_if=lambda v: v is None)] = None

    url: Annotated[str | None, Field(exclude_if=lambda v: v is None)] = None
