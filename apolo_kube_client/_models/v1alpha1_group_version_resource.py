from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1alpha1GroupVersionResource",)


class V1alpha1GroupVersionResource(BaseModel):
    """The names of the group, the version, and the resource."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.storagemigration.v1alpha1.GroupVersionResource"
    )

    group: Annotated[
        str | None,
        Field(description="""The name of the group.""", exclude_if=lambda v: v is None),
    ] = None

    resource: Annotated[
        str | None,
        Field(
            description="""The name of the resource.""", exclude_if=lambda v: v is None
        ),
    ] = None

    version: Annotated[
        str | None,
        Field(
            description="""The name of the version.""", exclude_if=lambda v: v is None
        ),
    ] = None
