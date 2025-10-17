from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector import V1LabelSelector

__all__ = ("V1AggregationRule",)


class V1AggregationRule(BaseModel):
    cluster_role_selectors: list[V1LabelSelector] = Field(
        default=[],
        serialization_alias="clusterRoleSelectors",
        validation_alias=AliasChoices("cluster_role_selectors", "clusterRoleSelectors"),
    )
