from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1VolumeNodeResources",)


class V1VolumeNodeResources(BaseModel):
    """VolumeNodeResources is a set of resource limits for scheduling of volumes."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.storage.v1.VolumeNodeResources"

    count: Annotated[
        int | None,
        Field(
            description="""count indicates the maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
