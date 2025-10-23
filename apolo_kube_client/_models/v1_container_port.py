from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1ContainerPort",)


class V1ContainerPort(BaseModel):
    container_port: int | None = Field(
        default=None,
        serialization_alias="containerPort",
        validation_alias=AliasChoices("container_port", "containerPort"),
        exclude_if=_exclude_if,
    )

    host_ip: str | None = Field(
        default=None,
        serialization_alias="hostIP",
        validation_alias=AliasChoices("host_ip", "hostIP"),
        exclude_if=_exclude_if,
    )

    host_port: int | None = Field(
        default=None,
        serialization_alias="hostPort",
        validation_alias=AliasChoices("host_port", "hostPort"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    protocol: str | None = Field(default=None, exclude_if=_exclude_if)
