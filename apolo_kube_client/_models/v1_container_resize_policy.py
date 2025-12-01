from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1ContainerResizePolicy",)


class V1ContainerResizePolicy(BaseModel):
    """ContainerResizePolicy represents resource resize policy for the container."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerResizePolicy"

    resource_name: Annotated[
        str,
        Field(
            alias="resourceName",
            description="""Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.""",
        ),
    ]

    restart_policy: Annotated[
        str,
        Field(
            alias="restartPolicy",
            description="""Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.""",
        ),
    ]
