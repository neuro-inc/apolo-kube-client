from __future__ import annotations
from pydantic import BaseModel, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1NetworkPolicyPort",)


class V1NetworkPolicyPort(BaseModel):
    end_port: int | None = Field(default_factory=lambda: None, alias="endPort")

    port: JsonType = Field(default_factory=lambda: {})

    protocol: str | None = Field(default_factory=lambda: None)
