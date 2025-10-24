from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1VolumeResourceRequirements",)


class V1VolumeResourceRequirements(BaseModel):
    """VolumeResourceRequirements describes the storage resource requirements for a volume."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.VolumeResourceRequirements"
    )

    limits: Annotated[
        dict[str, str],
        Field(
            description="""Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}

    requests: Annotated[
        dict[str, str],
        Field(
            description="""Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/""",
            exclude_if=lambda v: v == {},
        ),
        BeforeValidator(_collection_if_none("{}")),
    ] = {}
