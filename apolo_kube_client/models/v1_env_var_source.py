from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_config_map_key_selector import V1ConfigMapKeySelector
from .v1_file_key_selector import V1FileKeySelector
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector
from .v1_secret_key_selector import V1SecretKeySelector

__all__ = ("V1EnvVarSource",)


class V1EnvVarSource(BaseModel):
    config_map_key_ref: V1ConfigMapKeySelector = Field(
        default_factory=lambda: V1ConfigMapKeySelector(), alias="configMapKeyRef"
    )

    field_ref: V1ObjectFieldSelector = Field(
        default_factory=lambda: V1ObjectFieldSelector(), alias="fieldRef"
    )

    file_key_ref: V1FileKeySelector = Field(
        default_factory=lambda: V1FileKeySelector(), alias="fileKeyRef"
    )

    resource_field_ref: V1ResourceFieldSelector = Field(
        default_factory=lambda: V1ResourceFieldSelector(), alias="resourceFieldRef"
    )

    secret_key_ref: V1SecretKeySelector = Field(
        default_factory=lambda: V1SecretKeySelector(), alias="secretKeyRef"
    )
