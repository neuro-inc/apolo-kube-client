from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_config_map_env_source import V1ConfigMapEnvSource
from .v1_secret_env_source import V1SecretEnvSource
from pydantic import BeforeValidator

__all__ = ("V1EnvFromSource",)


class V1EnvFromSource(BaseModel):
    """EnvFromSource represents the source of a set of ConfigMaps or Secrets"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EnvFromSource"

    config_map_ref: Annotated[
        V1ConfigMapEnvSource,
        Field(
            alias="configMapRef",
            description="""The ConfigMap to select from""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ConfigMapEnvSource)),
    ] = V1ConfigMapEnvSource()

    prefix: Annotated[
        str | None,
        Field(
            description="""Optional text to prepend to the name of each environment variable. May consist of any printable ASCII characters except '='.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret_ref: Annotated[
        V1SecretEnvSource,
        Field(
            alias="secretRef",
            description="""The Secret to select from""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretEnvSource)),
    ] = V1SecretEnvSource()
