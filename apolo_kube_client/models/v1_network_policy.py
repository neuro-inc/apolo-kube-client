from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_network_policy_spec import V1NetworkPolicySpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1NetworkPolicy",)


class V1NetworkPolicy(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1NetworkPolicySpec = Field(default_factory=lambda: V1NetworkPolicySpec())
