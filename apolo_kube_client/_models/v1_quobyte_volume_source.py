from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1QuobyteVolumeSource",)


class V1QuobyteVolumeSource(BaseModel):
    """Represents a Quobyte mount that lasts the lifetime of a pod. Quobyte volumes do not support ownership management or SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.QuobyteVolumeSource"

    group: Annotated[
        str | None,
        Field(
            description="""group to map volume access to Default is no group""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    read_only: Annotated[
        bool | None,
        Field(
            alias="readOnly",
            description="""readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    registry: Annotated[
        str,
        Field(
            description="""registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes"""
        ),
    ]

    tenant: Annotated[
        str | None,
        Field(
            description="""tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    user: Annotated[
        str | None,
        Field(
            description="""user to map volume access to Defaults to serivceaccount user""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    volume: Annotated[
        str,
        Field(
            description="""volume is a string that references an already created Quobyte volume by name."""
        ),
    ]
