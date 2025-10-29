from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_persistent_volume_spec import V1PersistentVolumeSpec
from pydantic import BeforeValidator

__all__ = ("V1VolumeAttachmentSource",)


class V1VolumeAttachmentSource(BaseModel):
    """VolumeAttachmentSource represents a volume that should be attached. Right now only PersistentVolumes can be attached via external attacher, in the future we may allow also inline volumes in pods. Exactly one member can be set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.storage.v1.VolumeAttachmentSource"
    )

    inline_volume_spec: Annotated[
        V1PersistentVolumeSpec,
        Field(
            alias="inlineVolumeSpec",
            description="""inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is beta-level and is only honored by servers that enabled the CSIMigration feature.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1PersistentVolumeSpec)),
    ] = V1PersistentVolumeSpec()

    persistent_volume_name: Annotated[
        str | None,
        Field(
            alias="persistentVolumeName",
            description="""persistentVolumeName represents the name of the persistent volume to attach.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
