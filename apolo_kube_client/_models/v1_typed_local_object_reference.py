from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1TypedLocalObjectReference",)


class V1TypedLocalObjectReference(BaseModel):
    """TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.core.v1.TypedLocalObjectReference"
    )

    api_group: Annotated[
        str | None,
        Field(
            alias="apiGroup",
            description="""APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str, Field(description="""Kind is the type of resource being referenced""")
    ]

    name: Annotated[
        str, Field(description="""Name is the name of resource being referenced""")
    ]
