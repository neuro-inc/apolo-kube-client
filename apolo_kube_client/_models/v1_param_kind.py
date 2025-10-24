from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1ParamKind",)


class V1ParamKind(BaseModel):
    """ParamKind is a tuple of Group Kind and Version."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1.ParamKind"
    )

    api_version: Annotated[
        str | None,
        Field(
            alias="apiVersion",
            description="""APIVersion is the API group version the resources belong to. In format of "group/version". Required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    kind: Annotated[
        str | None,
        Field(
            description="""Kind is the API kind the resources belong to. Required.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
