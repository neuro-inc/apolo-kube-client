from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1_linux_container_user import V1LinuxContainerUser


__all__ = ("V1ContainerUser",)


class V1ContainerUser(BaseConfiguredModel):
    """ContainerUser represents user identity information"""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerUser"

    linux: Annotated[
        V1LinuxContainerUser | None,
        Field(
            description="""Linux holds user identity information initially attached to the first process of the containers in Linux. Note that the actual running identity can be changed if the process has enough privilege to do so.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
