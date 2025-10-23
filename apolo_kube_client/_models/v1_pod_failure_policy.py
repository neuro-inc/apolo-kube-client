from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_pod_failure_policy_rule import V1PodFailurePolicyRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodFailurePolicy",)


class V1PodFailurePolicy(BaseModel):
    rules: Annotated[
        list[V1PodFailurePolicyRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
