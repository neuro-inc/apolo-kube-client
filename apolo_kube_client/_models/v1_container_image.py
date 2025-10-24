from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator

__all__ = ("V1ContainerImage",)


class V1ContainerImage(BaseModel):
    """Describe a container image"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ContainerImage"

    names: Annotated[
        list[str],
        Field(
            description="""Names by which this image is known. e.g. ["kubernetes.example/hyperkube:v1.0.7", "cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7"]""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    size_bytes: Annotated[
        int | None,
        Field(
            alias="sizeBytes",
            description="""The size of the image in bytes.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
