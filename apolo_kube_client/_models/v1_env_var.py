from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_env_var_source import V1EnvVarSource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EnvVar",)


class V1EnvVar(BaseModel):
    name: str | None = Field(default=None, exclude_if=_exclude_if)

    value: str | None = Field(default=None, exclude_if=_exclude_if)

    value_from: Annotated[
        V1EnvVarSource, BeforeValidator(_default_if_none(V1EnvVarSource))
    ] = Field(
        default_factory=lambda: V1EnvVarSource(),
        serialization_alias="valueFrom",
        validation_alias=AliasChoices("value_from", "valueFrom"),
        exclude_if=_exclude_if,
    )
