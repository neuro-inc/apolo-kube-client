from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("CoreV1ResourceClaim",)


class CoreV1ResourceClaim(BaseModel):
    """ResourceClaim references one entry in PodSpec.ResourceClaims."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ResourceClaim"

    name: Annotated[
        str,
        Field(
            description="""Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container."""
        ),
    ]

    request: Annotated[
        str | None,
        Field(
            description="""Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
