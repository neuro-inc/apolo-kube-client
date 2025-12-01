from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1LocalObjectReference",)


class V1LocalObjectReference(BaseConfiguredModel):
    """LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.LocalObjectReference"

    name: Annotated[
        str | None,
        Field(
            description="""Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
