from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector


class V1AggregationRule(BaseModel):
    cluster_role_selectors: list[V1LabelSelector] | None = Field(
        None, alias="clusterRoleSelectors"
    )
