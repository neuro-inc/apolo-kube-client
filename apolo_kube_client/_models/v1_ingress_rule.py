from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1_http_ingress_rule_value import V1HTTPIngressRuleValue
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1IngressRule",)


class V1IngressRule(BaseModel):
    host: str | None = None

    http: Annotated[
        V1HTTPIngressRuleValue,
        BeforeValidator(_default_if_none(V1HTTPIngressRuleValue)),
    ] = Field(default_factory=lambda: V1HTTPIngressRuleValue())
