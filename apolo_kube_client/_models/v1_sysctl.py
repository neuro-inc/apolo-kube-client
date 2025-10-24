from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1Sysctl",)


class V1Sysctl(BaseModel):
    """Sysctl defines a kernel parameter to be set"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Sysctl"

    name: Annotated[str, Field(description="""Name of a property to set""")]

    value: Annotated[str, Field(description="""Value of a property to set""")]
