from pydantic import AliasChoices, BaseModel, Field
from .v2_hpa_scaling_policy import V2HPAScalingPolicy

__all__ = ("V2HPAScalingRules",)


class V2HPAScalingRules(BaseModel):
    policies: list[V2HPAScalingPolicy] = []

    select_policy: str | None = Field(
        default=None,
        serialization_alias="selectPolicy",
        validation_alias=AliasChoices("select_policy", "selectPolicy"),
    )

    stabilization_window_seconds: int | None = Field(
        default=None,
        serialization_alias="stabilizationWindowSeconds",
        validation_alias=AliasChoices(
            "stabilization_window_seconds", "stabilizationWindowSeconds"
        ),
    )

    tolerance: str | None = None
