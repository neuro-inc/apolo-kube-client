from pydantic import BaseModel, Field

from .v1_env_var_source import V1EnvVarSource


class V1EnvVar(BaseModel):
    name: str | None = Field(None, alias="name")

    value: str | None = Field(None, alias="value")

    value_from: V1EnvVarSource | None = Field(None, alias="valueFrom")
