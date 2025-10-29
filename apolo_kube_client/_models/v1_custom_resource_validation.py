from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_json_schema_props import V1JSONSchemaProps
from pydantic import BeforeValidator

__all__ = ("V1CustomResourceValidation",)


class V1CustomResourceValidation(BaseModel):
    """CustomResourceValidation is a list of validation methods for CustomResources."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceValidation"
    )

    open_apiv3_schema: Annotated[
        V1JSONSchemaProps,
        Field(
            alias="openAPIV3Schema",
            description="""openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1JSONSchemaProps)),
    ] = V1JSONSchemaProps()
