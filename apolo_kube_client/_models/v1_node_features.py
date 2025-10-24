from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1NodeFeatures",)


class V1NodeFeatures(BaseModel):
    """NodeFeatures describes the set of features implemented by the CRI implementation. The features contained in the NodeFeatures should depend only on the cri implementation independent of runtime handlers."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.NodeFeatures"

    supplemental_groups_policy: Annotated[
        bool | None,
        Field(
            alias="supplementalGroupsPolicy",
            description="""SupplementalGroupsPolicy is set to true if the runtime supports SupplementalGroupsPolicy and ContainerUser.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
