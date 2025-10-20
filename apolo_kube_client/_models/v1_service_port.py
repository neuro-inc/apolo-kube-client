from pydantic import AliasChoices, BaseModel, Field
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1ServicePort",)


class V1ServicePort(BaseModel):
    app_protocol: str | None = Field(
        default=None,
        serialization_alias="appProtocol",
        validation_alias=AliasChoices("app_protocol", "appProtocol"),
    )

    name: str | None = None

    node_port: int | None = Field(
        default=None,
        serialization_alias="nodePort",
        validation_alias=AliasChoices("node_port", "nodePort"),
    )

    port: int | None = None

    protocol: str | None = None

    target_port: JsonType = Field(
        default={},
        serialization_alias="targetPort",
        validation_alias=AliasChoices("target_port", "targetPort"),
    )
