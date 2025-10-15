from pydantic import BaseModel, Field

from .v1_config_map_env_source import V1ConfigMapEnvSource
from .v1_secret_env_source import V1SecretEnvSource


class V1EnvFromSource(BaseModel):
    config_map_ref: V1ConfigMapEnvSource | None = Field(None, alias="configMapRef")

    prefix: str | None = Field(None, alias="prefix")

    secret_ref: V1SecretEnvSource | None = Field(None, alias="secretRef")
