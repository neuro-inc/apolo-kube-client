from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_json_schema_props import V1JSONSchemaProps

__all__ = ("V1CustomResourceValidation",)


class V1CustomResourceValidation(BaseModel):
    open_apiv3_schema: V1JSONSchemaProps = Field(
        default_factory=lambda: V1JSONSchemaProps(), alias="openAPIV3Schema"
    )
