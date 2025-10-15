from pydantic import BaseModel, Field


class V1ContainerPort(BaseModel):
    container_port: int | None = Field(None, alias="containerPort")

    host_ip: str | None = Field(None, alias="hostIP")

    host_port: int | None = Field(None, alias="hostPort")

    name: str | None = Field(None, alias="name")

    protocol: str | None = Field(None, alias="protocol")
