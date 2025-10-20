from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1alpha3_device_taint_rule import V1alpha3DeviceTaintRule

__all__ = ("V1alpha3DeviceTaintRuleList",)


class V1alpha3DeviceTaintRuleList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1alpha3DeviceTaintRule] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
