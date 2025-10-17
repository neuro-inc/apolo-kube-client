from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_container_restart_rule_on_exit_codes import V1ContainerRestartRuleOnExitCodes

__all__ = ("V1ContainerRestartRule",)


class V1ContainerRestartRule(BaseModel):
    action: str | None = Field(default=None)

    exit_codes: V1ContainerRestartRuleOnExitCodes = Field(
        default_factory=lambda: V1ContainerRestartRuleOnExitCodes(),
        serialization_alias="exitCodes",
        validation_alias=AliasChoices("exit_codes", "exitCodes"),
    )
