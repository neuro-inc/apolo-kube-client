from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1SecretReference",)


class V1SecretReference(BaseModel):
    """SecretReference represents a Secret Reference. It has enough information to retrieve secret in any namespace"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.SecretReference"

    name: Annotated[
        str | None,
        Field(
            description="""name is unique within a namespace to reference a secret resource.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    namespace: Annotated[
        str | None,
        Field(
            description="""namespace defines the space within which the secret name must be unique.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
