from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field


__all__ = ("V1beta1ParamKind",)


class V1beta1ParamKind(BaseModel):
    """ParamKind is a tuple of Group Kind and Version."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1beta1.ParamKind"
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
