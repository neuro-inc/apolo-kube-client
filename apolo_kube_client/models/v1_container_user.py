from pydantic import BaseModel, Field
from .v1_linux_container_user import V1LinuxContainerUser

__all__ = ("V1ContainerUser",)


class V1ContainerUser(BaseModel):
    linux: V1LinuxContainerUser = Field(default_factory=lambda: V1LinuxContainerUser())
