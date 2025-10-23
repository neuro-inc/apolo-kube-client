from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1ServicePort",)


class V1ServicePort(BaseModel):
    app_protocol: str | None = Field(
        default=None,
        serialization_alias="appProtocol",
        validation_alias=AliasChoices("app_protocol", "appProtocol"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    node_port: int | None = Field(
        default=None,
        serialization_alias="nodePort",
        validation_alias=AliasChoices("node_port", "nodePort"),
        exclude_if=_exclude_if,
    )

    port: int | None = Field(default=None, exclude_if=_exclude_if)

    protocol: str | None = Field(default=None, exclude_if=_exclude_if)

    target_port: JsonType = Field(
        default={},
        serialization_alias="targetPort",
        validation_alias=AliasChoices("target_port", "targetPort"),
        exclude_if=_exclude_if,
    )
