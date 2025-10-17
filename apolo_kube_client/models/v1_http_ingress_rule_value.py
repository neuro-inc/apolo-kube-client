from pydantic import BaseModel
from .v1_http_ingress_path import V1HTTPIngressPath

__all__ = ("V1HTTPIngressRuleValue",)


class V1HTTPIngressRuleValue(BaseModel):
    paths: list[V1HTTPIngressPath] = []
