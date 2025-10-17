from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1alpha3_device_taint_rule import V1alpha3DeviceTaintRule

__all__ = ("V1alpha3DeviceTaintRuleList",)


class V1alpha3DeviceTaintRuleList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1alpha3DeviceTaintRule] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
