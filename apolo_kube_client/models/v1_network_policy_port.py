from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1NetworkPolicyPort",)


class V1NetworkPolicyPort(BaseModel):
    end_port: int | None = Field(
        default=None,
        serialization_alias="endPort",
        validation_alias=AliasChoices("end_port", "endPort"),
    )

    port: JsonType = Field(default={})

    protocol: str | None = Field(default=None)
