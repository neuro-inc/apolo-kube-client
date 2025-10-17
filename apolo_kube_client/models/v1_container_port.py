from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ContainerPort",)


class V1ContainerPort(BaseModel):
    container_port: int | None = Field(
        default=None,
        serialization_alias="containerPort",
        validation_alias=AliasChoices("container_port", "containerPort"),
    )

    host_ip: str | None = Field(
        default=None,
        serialization_alias="hostIP",
        validation_alias=AliasChoices("host_ip", "hostIP"),
    )

    host_port: int | None = Field(
        default=None,
        serialization_alias="hostPort",
        validation_alias=AliasChoices("host_port", "hostPort"),
    )

    name: str | None = Field(default=None)

    protocol: str | None = Field(default=None)
