from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1LinuxContainerUser",)


class V1LinuxContainerUser(BaseModel):
    """LinuxContainerUser represents user identity information in Linux containers"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.LinuxContainerUser"

    gid: Annotated[
        int,
        Field(
            description="""GID is the primary gid initially attached to the first process in the container"""
        ),
    ]

    supplemental_groups: Annotated[
        list[int],
        Field(
            alias="supplementalGroups",
            description="""SupplementalGroups are the supplemental groups initially attached to the first process in the container""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    uid: Annotated[
        int,
        Field(
            description="""UID is the primary uid initially attached to the first process in the container"""
        ),
    ]
