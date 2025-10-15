from pydantic import BaseModel, Field

from .v1_config_map_key_selector import V1ConfigMapKeySelector
from .v1_object_field_selector import V1ObjectFieldSelector
from .v1_resource_field_selector import V1ResourceFieldSelector
from .v1_secret_key_selector import V1SecretKeySelector


class V1EnvVarSource(BaseModel):
    config_map_key_ref: V1ConfigMapKeySelector | None = Field(
        None, alias="configMapKeyRef"
    )

    field_ref: V1ObjectFieldSelector | None = Field(None, alias="fieldRef")

    resource_field_ref: V1ResourceFieldSelector | None = Field(
        None, alias="resourceFieldRef"
    )

    secret_key_ref: V1SecretKeySelector | None = Field(None, alias="secretKeyRef")
