from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1beta1_parent_reference import V1beta1ParentReference

__all__ = ("V1beta1IPAddressSpec",)


class V1beta1IPAddressSpec(BaseModel):
    """IPAddressSpec describe the attributes in an IP Address."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1beta1.IPAddressSpec"

    parent_ref: Annotated[
        V1beta1ParentReference,
        Field(
            alias="parentRef",
            description="""ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object.""",
        ),
    ]
