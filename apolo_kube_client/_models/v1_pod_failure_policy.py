from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_pod_failure_policy_rule import V1PodFailurePolicyRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodFailurePolicy",)


class V1PodFailurePolicy(BaseModel):
    rules: Annotated[
        list[V1PodFailurePolicyRule], BeforeValidator(_collection_if_none("[]"))
    ] = []
