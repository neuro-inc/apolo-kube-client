from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_volume_attachment_source import V1VolumeAttachmentSource

__all__ = ("V1VolumeAttachmentSpec",)


class V1VolumeAttachmentSpec(BaseModel):
    """VolumeAttachmentSpec is the specification of a VolumeAttachment request."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.storage.v1.VolumeAttachmentSpec"

    attacher: Annotated[
        str,
        Field(
            description="""attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName()."""
        ),
    ]

    node_name: Annotated[
        str,
        Field(
            alias="nodeName",
            description="""nodeName represents the node that the volume should be attached to.""",
        ),
    ]

    source: Annotated[
        V1VolumeAttachmentSource,
        Field(description="""source represents the volume that should be attached."""),
    ]
