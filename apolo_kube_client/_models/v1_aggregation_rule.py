from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_label_selector import V1LabelSelector
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1AggregationRule",)


class V1AggregationRule(BaseModel):
    cluster_role_selectors: Annotated[
        list[V1LabelSelector], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="clusterRoleSelectors",
        validation_alias=AliasChoices("cluster_role_selectors", "clusterRoleSelectors"),
        exclude_if=_exclude_if,
    )
