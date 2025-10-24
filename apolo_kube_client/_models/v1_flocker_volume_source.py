from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1FlockerVolumeSource",)


class V1FlockerVolumeSource(BaseModel):
    """Represents a Flocker volume mounted by the Flocker agent. One and only one of datasetName and datasetUUID should be set. Flocker volumes do not support ownership management or SELinux relabeling."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.FlockerVolumeSource"

    dataset_name: Annotated[
        str | None,
        Field(
            alias="datasetName",
            description="""datasetName is Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    dataset_uuid: Annotated[
        str | None,
        Field(
            alias="datasetUUID",
            description="""datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
