from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1HTTPHeader",)


class V1HTTPHeader(BaseModel):
    """HTTPHeader describes a custom header to be used in HTTP probes"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.HTTPHeader"

    name: Annotated[
        str,
        Field(
            description="""The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header."""
        ),
    ]

    value: Annotated[str, Field(description="""The header field value""")]
