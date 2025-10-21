from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1_linux_container_user import V1LinuxContainerUser
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ContainerUser",)


class V1ContainerUser(BaseModel):
    linux: Annotated[
        V1LinuxContainerUser, BeforeValidator(_default_if_none(V1LinuxContainerUser))
    ] = Field(default_factory=lambda: V1LinuxContainerUser())
