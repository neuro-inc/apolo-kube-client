from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1Preconditions",)


class V1Preconditions(BaseConfiguredModel):
    """Preconditions must be fulfilled before an operation (update, delete, etc.) is carried out."""

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
