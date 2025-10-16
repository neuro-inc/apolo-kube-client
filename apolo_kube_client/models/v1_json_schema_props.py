from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_external_documentation import V1ExternalDocumentation
from .v1_validation_rule import V1ValidationRule
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1JSONSchemaProps",)


class V1JSONSchemaProps(BaseModel):
    ref: str | None = Field(default_factory=lambda: None, alias="$ref")

    schema_: str | None = Field(default_factory=lambda: None, alias="$schema")

    additional_items: JsonType = Field(
        default_factory=lambda: {}, alias="additionalItems"
    )

    additional_properties: JsonType = Field(
        default_factory=lambda: {}, alias="additionalProperties"
    )

    all_of: list[V1JSONSchemaProps] = Field(default_factory=lambda: [], alias="allOf")

    any_of: list[V1JSONSchemaProps] = Field(default_factory=lambda: [], alias="anyOf")

    default: JsonType = Field(default_factory=lambda: {}, alias="default")

    definitions: dict[str, V1JSONSchemaProps] = Field(
        default_factory=lambda: {}, alias="definitions"
    )

    dependencies: dict[str, JsonType] = Field(
        default_factory=lambda: {}, alias="dependencies"
    )

    description: str | None = Field(default_factory=lambda: None, alias="description")

    enum: list[JsonType] = Field(default_factory=lambda: [], alias="enum")

    example: JsonType = Field(default_factory=lambda: {}, alias="example")

    exclusive_maximum: bool | None = Field(
        default_factory=lambda: None, alias="exclusiveMaximum"
    )

    exclusive_minimum: bool | None = Field(
        default_factory=lambda: None, alias="exclusiveMinimum"
    )

    external_docs: V1ExternalDocumentation = Field(
        default_factory=lambda: V1ExternalDocumentation(), alias="externalDocs"
    )

    format: str | None = Field(default_factory=lambda: None, alias="format")

    id: str | None = Field(default_factory=lambda: None, alias="id")

    items: JsonType = Field(default_factory=lambda: {}, alias="items")

    max_items: int | None = Field(default_factory=lambda: None, alias="maxItems")

    max_length: int | None = Field(default_factory=lambda: None, alias="maxLength")

    max_properties: int | None = Field(
        default_factory=lambda: None, alias="maxProperties"
    )

    maximum: float | None = Field(default_factory=lambda: None, alias="maximum")

    min_items: int | None = Field(default_factory=lambda: None, alias="minItems")

    min_length: int | None = Field(default_factory=lambda: None, alias="minLength")

    min_properties: int | None = Field(
        default_factory=lambda: None, alias="minProperties"
    )

    minimum: float | None = Field(default_factory=lambda: None, alias="minimum")

    multiple_of: float | None = Field(default_factory=lambda: None, alias="multipleOf")

    not_: V1JSONSchemaProps = Field(
        default_factory=lambda: V1JSONSchemaProps(), alias="not"
    )

    nullable: bool | None = Field(default_factory=lambda: None, alias="nullable")

    one_of: list[V1JSONSchemaProps] = Field(default_factory=lambda: [], alias="oneOf")

    pattern: str | None = Field(default_factory=lambda: None, alias="pattern")

    pattern_properties: dict[str, V1JSONSchemaProps] = Field(
        default_factory=lambda: {}, alias="patternProperties"
    )

    properties: dict[str, V1JSONSchemaProps] = Field(
        default_factory=lambda: {}, alias="properties"
    )

    required: list[str] = Field(default_factory=lambda: [], alias="required")

    title: str | None = Field(default_factory=lambda: None, alias="title")

    type: str | None = Field(default_factory=lambda: None, alias="type")

    unique_items: bool | None = Field(default_factory=lambda: None, alias="uniqueItems")

    x_kubernetes_embedded_resource: bool | None = Field(
        default_factory=lambda: None, alias="x-kubernetes-embedded-resource"
    )

    x_kubernetes_int_or_string: bool | None = Field(
        default_factory=lambda: None, alias="x-kubernetes-int-or-string"
    )

    x_kubernetes_list_map_keys: list[str] = Field(
        default_factory=lambda: [], alias="x-kubernetes-list-map-keys"
    )

    x_kubernetes_list_type: str | None = Field(
        default_factory=lambda: None, alias="x-kubernetes-list-type"
    )

    x_kubernetes_map_type: str | None = Field(
        default_factory=lambda: None, alias="x-kubernetes-map-type"
    )

    x_kubernetes_preserve_unknown_fields: bool | None = Field(
        default_factory=lambda: None, alias="x-kubernetes-preserve-unknown-fields"
    )

    x_kubernetes_validations: list[V1ValidationRule] = Field(
        default_factory=lambda: [], alias="x-kubernetes-validations"
    )
