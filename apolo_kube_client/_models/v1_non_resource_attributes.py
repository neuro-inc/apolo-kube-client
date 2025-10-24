from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1NonResourceAttributes",)


class V1NonResourceAttributes(BaseModel):
    """NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.authorization.v1.NonResourceAttributes"
    )

    path: Annotated[
        str | None,
        Field(
            description="""Path is the URL path of the request""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    verb: Annotated[
        str | None,
        Field(
            description="""Verb is the standard HTTP verb""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
