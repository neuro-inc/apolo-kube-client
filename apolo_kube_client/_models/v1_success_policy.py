from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_success_policy_rule import V1SuccessPolicyRule
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SuccessPolicy",)


class V1SuccessPolicy(BaseModel):
    rules: Annotated[
        list[V1SuccessPolicyRule], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
