from pydantic import BaseModel, Field

from .v1_h_t_t_p_ingress_path import V1HTTPIngressPath


class V1HTTPIngressRuleValue(BaseModel):
    paths: list[V1HTTPIngressPath] | None = Field(None, alias="paths")
