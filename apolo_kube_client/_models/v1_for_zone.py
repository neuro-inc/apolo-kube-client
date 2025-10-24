from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ForZone",)


class V1ForZone(BaseModel):
    """ForZone provides information about which zones should consume this endpoint."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.discovery.v1.ForZone"

    name: Annotated[str, Field(description="""name represents the name of the zone.""")]
