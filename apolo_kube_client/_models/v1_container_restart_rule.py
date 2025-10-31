from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_container_restart_rule_on_exit_codes import V1ContainerRestartRuleOnExitCodes

__all__ = ("V1ContainerRestartRule",)


class V1ContainerRestartRule(BaseModel):
    """ContainerRestartRule describes how a container exit is handled."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerRestartRule"

    action: Annotated[
        str,
        Field(
            description="""Specifies the action taken on a container exit if the requirements are satisfied. The only possible value is "Restart" to restart the container."""
        ),
    ]

    exit_codes: Annotated[
        V1ContainerRestartRuleOnExitCodes | None,
        Field(
            alias="exitCodes",
            description="""Represents the exit codes to check on container exits.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
