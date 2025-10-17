from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1alpha3_device_taint_rule_spec import V1alpha3DeviceTaintRuleSpec

__all__ = ("V1alpha3DeviceTaintRule",)


class V1alpha3DeviceTaintRule(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1alpha3DeviceTaintRuleSpec = Field(
        default_factory=lambda: V1alpha3DeviceTaintRuleSpec()
    )
