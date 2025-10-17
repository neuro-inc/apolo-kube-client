from pydantic import BaseModel, Field
from .v1_http_ingress_rule_value import V1HTTPIngressRuleValue

__all__ = ("V1IngressRule",)


class V1IngressRule(BaseModel):
    host: str | None = None

    http: V1HTTPIngressRuleValue = Field(
        default_factory=lambda: V1HTTPIngressRuleValue()
    )
