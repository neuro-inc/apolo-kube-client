from pydantic import BaseModel, Field

from .v1_label_selector_requirement import V1LabelSelectorRequirement


class V1LabelSelector(BaseModel):
    match_expressions: list[V1LabelSelectorRequirement] | None = Field(
        None, alias="matchExpressions"
    )

    match_labels: dict(str, str) | None = Field(None, alias="matchLabels")
