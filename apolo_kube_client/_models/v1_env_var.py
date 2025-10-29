from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_env_var_source import V1EnvVarSource
from pydantic import BeforeValidator

__all__ = ("V1EnvVar",)


class V1EnvVar(BaseModel):
    """EnvVar represents an environment variable present in a Container."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EnvVar"

    name: Annotated[
        str,
        Field(
            description="""Name of the environment variable. May consist of any printable ASCII characters except '='."""
        ),
    ]

    value: Annotated[
        str | None,
        Field(
            description="""Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "$$(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    value_from: Annotated[
        V1EnvVarSource,
        Field(
            alias="valueFrom",
            description="""Source for the environment variable's value. Cannot be used if value is not empty.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1EnvVarSource)),
    ] = V1EnvVarSource()
