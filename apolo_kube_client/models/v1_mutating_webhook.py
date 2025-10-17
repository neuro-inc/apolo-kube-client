from __future__ import annotations
from pydantic import BaseModel, Field
from .admissionregistration_v1_webhook_client_config import (
    AdmissionregistrationV1WebhookClientConfig,
)
from .v1_label_selector import V1LabelSelector
from .v1_match_condition import V1MatchCondition
from .v1_rule_with_operations import V1RuleWithOperations

__all__ = ("V1MutatingWebhook",)


class V1MutatingWebhook(BaseModel):
    admission_review_versions: list[str] = Field(
        default_factory=lambda: [], alias="admissionReviewVersions"
    )

    client_config: AdmissionregistrationV1WebhookClientConfig = Field(
        default_factory=lambda: AdmissionregistrationV1WebhookClientConfig(),
        alias="clientConfig",
    )

    failure_policy: str | None = Field(
        default_factory=lambda: None, alias="failurePolicy"
    )

    match_conditions: list[V1MatchCondition] = Field(
        default_factory=lambda: [], alias="matchConditions"
    )

    match_policy: str | None = Field(default_factory=lambda: None, alias="matchPolicy")

    name: str | None = Field(default_factory=lambda: None)

    namespace_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="namespaceSelector"
    )

    object_selector: V1LabelSelector = Field(
        default_factory=lambda: V1LabelSelector(), alias="objectSelector"
    )

    reinvocation_policy: str | None = Field(
        default_factory=lambda: None, alias="reinvocationPolicy"
    )

    rules: list[V1RuleWithOperations] = Field(default_factory=lambda: [])

    side_effects: str | None = Field(default_factory=lambda: None, alias="sideEffects")

    timeout_seconds: int | None = Field(
        default_factory=lambda: None, alias="timeoutSeconds"
    )
