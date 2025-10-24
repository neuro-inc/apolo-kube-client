from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1StatefulSetOrdinals",)


class V1StatefulSetOrdinals(BaseModel):
    """StatefulSetOrdinals describes the policy used for replica ordinal assignment in this StatefulSet."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.apps.v1.StatefulSetOrdinals"

    start: Annotated[
        int | None,
        Field(
            description="""start is the number representing the first replica's index. It may be used to number replicas from an alternate index (eg: 1-indexed) over the default 0-indexed names, or to orchestrate progressive movement of replicas from one StatefulSet to another. If set, replica indices will be in the range:
  [.spec.ordinals.start, .spec.ordinals.start + .spec.replicas).
If unset, defaults to 0. Replica indices will be in the range:
  [0, .spec.replicas).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
