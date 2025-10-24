from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ObjectFieldSelector",)


class V1ObjectFieldSelector(BaseModel):
    """ObjectFieldSelector selects an APIVersioned field of an object."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ObjectFieldSelector"

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""Version of the schema the FieldPath is written in terms of, defaults to "v1".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    field_path: Annotated[
        str,
        Field(
            alias="fieldPath",
            description="""Path of the field to select in the specified API version.""",
        ),
    ]
