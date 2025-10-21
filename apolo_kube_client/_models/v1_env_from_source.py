from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_config_map_env_source import V1ConfigMapEnvSource
from .v1_secret_env_source import V1SecretEnvSource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EnvFromSource",)


class V1EnvFromSource(BaseModel):
    config_map_ref: Annotated[
        V1ConfigMapEnvSource, BeforeValidator(_default_if_none(V1ConfigMapEnvSource))
    ] = Field(
        default_factory=lambda: V1ConfigMapEnvSource(),
        serialization_alias="configMapRef",
        validation_alias=AliasChoices("config_map_ref", "configMapRef"),
    )

    prefix: str | None = None

    secret_ref: Annotated[
        V1SecretEnvSource, BeforeValidator(_default_if_none(V1SecretEnvSource))
    ] = Field(
        default_factory=lambda: V1SecretEnvSource(),
        serialization_alias="secretRef",
        validation_alias=AliasChoices("secret_ref", "secretRef"),
    )
