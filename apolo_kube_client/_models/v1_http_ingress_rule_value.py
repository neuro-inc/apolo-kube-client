from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_http_ingress_path import V1HTTPIngressPath
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1HTTPIngressRuleValue",)


class V1HTTPIngressRuleValue(BaseModel):
    paths: Annotated[
        list[V1HTTPIngressPath], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
