from pydantic import AliasChoices, BaseModel, Field
from .v1_csi_driver_spec import V1CSIDriverSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CSIDriver",)


class V1CSIDriver(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1CSIDriverSpec = Field(default_factory=lambda: V1CSIDriverSpec())
