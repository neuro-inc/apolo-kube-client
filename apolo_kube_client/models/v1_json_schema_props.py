from pydantic import BaseModel, Field

from .object import object
from .v1_external_documentation import V1ExternalDocumentation
from .v1_j_s_o_n_schema_props import V1JSONSchemaProps
from .v1_validation_rule import V1ValidationRule


class V1JSONSchemaProps(BaseModel):
    ref: str | None = Field(None, alias="$ref")

    schema: str | None = Field(None, alias="$schema")

    additional_items: object | None = Field(None, alias="additionalItems")

    additional_properties: object | None = Field(None, alias="additionalProperties")

    all_of: list[V1JSONSchemaProps] | None = Field(None, alias="allOf")

    any_of: list[V1JSONSchemaProps] | None = Field(None, alias="anyOf")

    default: object | None = Field(None, alias="default")

    definitions: dict(str, V1JSONSchemaProps) | None = Field(None, alias="definitions")

    dependencies: dict(str, object) | None = Field(None, alias="dependencies")

    description: str | None = Field(None, alias="description")

    enum: list[object] | None = Field(None, alias="enum")

    example: object | None = Field(None, alias="example")

    exclusive_maximum: bool | None = Field(None, alias="exclusiveMaximum")

    exclusive_minimum: bool | None = Field(None, alias="exclusiveMinimum")

    external_docs: V1ExternalDocumentation | None = Field(None, alias="externalDocs")

    format: str | None = Field(None, alias="format")

    id: str | None = Field(None, alias="id")

    items: object | None = Field(None, alias="items")

    max_items: int | None = Field(None, alias="maxItems")

    max_length: int | None = Field(None, alias="maxLength")

    max_properties: int | None = Field(None, alias="maxProperties")

    maximum: float | None = Field(None, alias="maximum")

    min_items: int | None = Field(None, alias="minItems")

    min_length: int | None = Field(None, alias="minLength")

    min_properties: int | None = Field(None, alias="minProperties")

    minimum: float | None = Field(None, alias="minimum")

    multiple_of: float | None = Field(None, alias="multipleOf")

    _not: V1JSONSchemaProps | None = Field(None, alias="not")

    nullable: bool | None = Field(None, alias="nullable")

    one_of: list[V1JSONSchemaProps] | None = Field(None, alias="oneOf")

    pattern: str | None = Field(None, alias="pattern")

    pattern_properties: dict(str, V1JSONSchemaProps) | None = Field(
        None, alias="patternProperties"
    )

    properties: dict(str, V1JSONSchemaProps) | None = Field(None, alias="properties")

    required: list[str] | None = Field(None, alias="required")

    title: str | None = Field(None, alias="title")

    type: str | None = Field(None, alias="type")

    unique_items: bool | None = Field(None, alias="uniqueItems")

    x_kubernetes_embedded_resource: bool | None = Field(
        None, alias="x-kubernetes-embedded-resource"
    )

    x_kubernetes_int_or_string: bool | None = Field(
        None, alias="x-kubernetes-int-or-string"
    )

    x_kubernetes_list_map_keys: list[str] | None = Field(
        None, alias="x-kubernetes-list-map-keys"
    )

    x_kubernetes_list_type: str | None = Field(None, alias="x-kubernetes-list-type")

    x_kubernetes_map_type: str | None = Field(None, alias="x-kubernetes-map-type")

    x_kubernetes_preserve_unknown_fields: bool | None = Field(
        None, alias="x-kubernetes-preserve-unknown-fields"
    )

    x_kubernetes_validations: list[V1ValidationRule] | None = Field(
        None, alias="x-kubernetes-validations"
    )
