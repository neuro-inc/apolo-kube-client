from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_network_policy_spec import V1NetworkPolicySpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1NetworkPolicy",)


class V1NetworkPolicy(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1NetworkPolicySpec | None = Field(None, alias="spec")
