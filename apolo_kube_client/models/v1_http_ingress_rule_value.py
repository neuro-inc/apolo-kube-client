from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_http_ingress_path import V1HTTPIngressPath

__all__ = ("V1HTTPIngressRuleValue",)


class V1HTTPIngressRuleValue(BaseModel):
    paths: list[V1HTTPIngressPath] | None = Field(None, alias="paths")
