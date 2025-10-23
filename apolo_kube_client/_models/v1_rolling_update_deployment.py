from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1RollingUpdateDeployment",)


class V1RollingUpdateDeployment(BaseModel):
    max_surge: JsonType = Field(
        default={},
        serialization_alias="maxSurge",
        validation_alias=AliasChoices("max_surge", "maxSurge"),
        exclude_if=_exclude_if,
    )

    max_unavailable: JsonType = Field(
        default={},
        serialization_alias="maxUnavailable",
        validation_alias=AliasChoices("max_unavailable", "maxUnavailable"),
        exclude_if=_exclude_if,
    )
