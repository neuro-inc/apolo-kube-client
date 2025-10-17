from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_config_map_key_selector import V1ConfigMapKeySelector
from .v1_file_key_selector import V1FileKeySelector
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector
from .v1_secret_key_selector import V1SecretKeySelector

__all__ = ("V1EnvVarSource",)


class V1EnvVarSource(BaseModel):
    config_map_key_ref: V1ConfigMapKeySelector = Field(
        default_factory=lambda: V1ConfigMapKeySelector(),
        serialization_alias="configMapKeyRef",
        validation_alias=AliasChoices("config_map_key_ref", "configMapKeyRef"),
    )

    field_ref: V1ObjectFieldSelector = Field(
        default_factory=lambda: V1ObjectFieldSelector(),
        serialization_alias="fieldRef",
        validation_alias=AliasChoices("field_ref", "fieldRef"),
    )

    file_key_ref: V1FileKeySelector = Field(
        default_factory=lambda: V1FileKeySelector(),
        serialization_alias="fileKeyRef",
        validation_alias=AliasChoices("file_key_ref", "fileKeyRef"),
    )

    resource_field_ref: V1ResourceFieldSelector = Field(
        default_factory=lambda: V1ResourceFieldSelector(),
        serialization_alias="resourceFieldRef",
        validation_alias=AliasChoices("resource_field_ref", "resourceFieldRef"),
    )

    secret_key_ref: V1SecretKeySelector = Field(
        default_factory=lambda: V1SecretKeySelector(),
        serialization_alias="secretKeyRef",
        validation_alias=AliasChoices("secret_key_ref", "secretKeyRef"),
    )
