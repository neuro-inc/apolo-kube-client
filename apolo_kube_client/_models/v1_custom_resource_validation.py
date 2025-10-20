from pydantic import AliasChoices, BaseModel, Field
from .v1_json_schema_props import V1JSONSchemaProps

__all__ = ("V1CustomResourceValidation",)


class V1CustomResourceValidation(BaseModel):
    open_apiv3_schema: V1JSONSchemaProps = Field(
        default_factory=lambda: V1JSONSchemaProps(),
        serialization_alias="openAPIV3Schema",
        validation_alias=AliasChoices("open_apiv3_schema", "openAPIV3Schema"),
    )
