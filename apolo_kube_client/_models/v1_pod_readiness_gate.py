from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1PodReadinessGate",)


class V1PodReadinessGate(BaseModel):
    condition_type: str | None = Field(
        default=None,
        serialization_alias="conditionType",
        validation_alias=AliasChoices("condition_type", "conditionType"),
        exclude_if=_exclude_if,
    )
