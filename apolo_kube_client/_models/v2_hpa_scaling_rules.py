from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v2_hpa_scaling_policy import V2HPAScalingPolicy
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2HPAScalingRules",)


class V2HPAScalingRules(BaseModel):
    policies: Annotated[
        list[V2HPAScalingPolicy], BeforeValidator(_collection_if_none("[]"))
    ] = []

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
