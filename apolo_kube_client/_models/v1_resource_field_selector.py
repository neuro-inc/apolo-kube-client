from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ResourceFieldSelector",)


class V1ResourceFieldSelector(BaseModel):
    """ResourceFieldSelector represents container resources (cpu, memory) and their output format"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.ResourceFieldSelector"

    container_name: Annotated[
        str | None,
        Field(
            alias="containerName",
            description="""Container name: required for volumes, optional for env vars""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    divisor: Annotated[
        str | None,
        Field(
            description='''Specifies the output format of the exposed resources, defaults to "1"''',
            exclude_if=lambda v: v is None,
        ),
    ] = None

    resource: Annotated[str, Field(description="""Required: resource to select""")]
