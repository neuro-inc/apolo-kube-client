from pydantic import BaseModel, Field

from .v1_j_s_o_n_schema_props import V1JSONSchemaProps


class V1CustomResourceValidation(BaseModel):
    open_apiv3_schema: V1JSONSchemaProps | None = Field(None, alias="openAPIV3Schema")
