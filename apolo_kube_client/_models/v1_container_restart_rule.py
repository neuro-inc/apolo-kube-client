from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_container_restart_rule_on_exit_codes import V1ContainerRestartRuleOnExitCodes
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ContainerRestartRule",)


class V1ContainerRestartRule(BaseModel):
    action: str | None = None

    exit_codes: Annotated[
        V1ContainerRestartRuleOnExitCodes,
        BeforeValidator(_default_if_none(V1ContainerRestartRuleOnExitCodes)),
    ] = Field(
        default_factory=lambda: V1ContainerRestartRuleOnExitCodes(),
        serialization_alias="exitCodes",
        validation_alias=AliasChoices("exit_codes", "exitCodes"),
    )
