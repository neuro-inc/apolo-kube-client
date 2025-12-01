from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field

from .v1_parent_reference import V1ParentReference


__all__ = ("V1IPAddressSpec",)


class V1IPAddressSpec(BaseModel):
    """IPAddressSpec describe the attributes in an IP Address."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.networking.v1.IPAddressSpec"

    parent_ref: Annotated[
        V1ParentReference,
        Field(
            alias="parentRef",
            description="""ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object.""",
        ),
    ]
