from pydantic import BaseModel, Field

from .v1_h_t_t_p_ingress_rule_value import V1HTTPIngressRuleValue


class V1IngressRule(BaseModel):
    host: str | None = Field(None, alias="host")

    http: V1HTTPIngressRuleValue | None = Field(None, alias="http")
