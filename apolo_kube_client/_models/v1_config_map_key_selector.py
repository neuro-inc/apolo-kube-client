from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ConfigMapKeySelector",)


class V1ConfigMapKeySelector(BaseModel):
    """Selects a key from a ConfigMap."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ConfigMapKeySelector"

    key: Annotated[str, Field(description="""The key to select.""")]

    name: Annotated[
        str | None,
        Field(
            description="""Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    optional: Annotated[
        bool | None,
        Field(
            description="""Specify whether the ConfigMap or its key must be defined""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
