from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1CustomResourceColumnDefinition",)


class V1CustomResourceColumnDefinition(BaseModel):
    """CustomResourceColumnDefinition specifies a column for server side printing."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceColumnDefinition"
    )

    description: Annotated[
        str | None,
        Field(
            description="""description is a human readable description of this column.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    format: Annotated[
        str | None,
        Field(
            description="""format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    json_path: Annotated[
        str,
        Field(
            alias="jsonPath",
            description="""jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column.""",
        ),
    ]

    name: Annotated[
        str, Field(description="""name is a human readable name for the column.""")
    ]

    priority: Annotated[
        int | None,
        Field(
            description="""priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str,
        Field(
            description="""type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details."""
        ),
    ]
