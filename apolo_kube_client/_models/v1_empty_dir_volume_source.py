from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1EmptyDirVolumeSource",)


class V1EmptyDirVolumeSource(BaseModel):
    """Represents an empty directory for a pod. Empty directory volumes support ownership management and SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.EmptyDirVolumeSource"

    medium: Annotated[
        str | None,
        Field(
            description="""medium represents what type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    size_limit: Annotated[
        str | None,
        Field(
            alias="sizeLimit",
            description="""sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
