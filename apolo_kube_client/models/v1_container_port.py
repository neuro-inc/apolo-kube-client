from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ContainerPort",)


class V1ContainerPort(BaseModel):
    container_port: int | None = Field(
        default_factory=lambda: None, alias="containerPort"
    )

    host_ip: str | None = Field(default_factory=lambda: None, alias="hostIP")

    host_port: int | None = Field(default_factory=lambda: None, alias="hostPort")

    name: str | None = Field(default_factory=lambda: None)

    protocol: str | None = Field(default_factory=lambda: None)
