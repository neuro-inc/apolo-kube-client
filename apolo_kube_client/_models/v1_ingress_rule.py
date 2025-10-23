from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_http_ingress_rule_value import V1HTTPIngressRuleValue
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressRule",)


class V1IngressRule(BaseModel):
    host: str | None = Field(default=None, exclude_if=_exclude_if)

    http: Annotated[
        V1HTTPIngressRuleValue,
        BeforeValidator(_default_if_none(V1HTTPIngressRuleValue)),
    ] = Field(default_factory=lambda: V1HTTPIngressRuleValue(), exclude_if=_exclude_if)
