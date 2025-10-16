from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_http_ingress_rule_value import V1HTTPIngressRuleValue

__all__ = ("V1IngressRule",)


class V1IngressRule(BaseModel):
    host: str | None = Field(None, alias="host")

    http: V1HTTPIngressRuleValue | None = Field(None, alias="http")
