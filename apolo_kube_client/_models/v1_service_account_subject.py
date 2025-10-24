from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ServiceAccountSubject",)


class V1ServiceAccountSubject(BaseModel):
    """ServiceAccountSubject holds detailed information for service-account-kind subject."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.flowcontrol.v1.ServiceAccountSubject"
    )

    name: Annotated[
        str,
        Field(
            description="""`name` is the name of matching ServiceAccount objects, or "*" to match regardless of name. Required."""
        ),
    ]

    namespace: Annotated[
        str,
        Field(
            description="""`namespace` is the namespace of matching ServiceAccount objects. Required."""
        ),
    ]
