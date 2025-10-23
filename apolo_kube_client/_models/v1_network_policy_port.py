from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1NetworkPolicyPort",)


class V1NetworkPolicyPort(BaseModel):
    end_port: int | None = Field(
        default=None,
        serialization_alias="endPort",
        validation_alias=AliasChoices("end_port", "endPort"),
        exclude_if=_exclude_if,
    )

    port: JsonType = Field(default={}, exclude_if=_exclude_if)

    protocol: str | None = Field(default=None, exclude_if=_exclude_if)
