from pydantic import AliasChoices, BaseModel, Field
from .v1_env_var_source import V1EnvVarSource

__all__ = ("V1EnvVar",)


class V1EnvVar(BaseModel):
    name: str | None = None

    value: str | None = None

    value_from: V1EnvVarSource = Field(
        default_factory=lambda: V1EnvVarSource(),
        serialization_alias="valueFrom",
        validation_alias=AliasChoices("value_from", "valueFrom"),
    )
