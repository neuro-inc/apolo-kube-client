from pydantic import BaseModel, Field

from .admissionregistration_v1_webhook_client_config import (
    AdmissionregistrationV1WebhookClientConfig,
)
from .v1_label_selector import V1LabelSelector
from .v1_match_condition import V1MatchCondition
from .v1_rule_with_operations import V1RuleWithOperations


class V1ValidatingWebhook(BaseModel):
    admission_review_versions: list[str] | None = Field(
        None, alias="admissionReviewVersions"
    )

    client_config: AdmissionregistrationV1WebhookClientConfig | None = Field(
        None, alias="clientConfig"
    )

    failure_policy: str | None = Field(None, alias="failurePolicy")

    match_conditions: list[V1MatchCondition] | None = Field(
        None, alias="matchConditions"
    )

    match_policy: str | None = Field(None, alias="matchPolicy")

    name: str | None = Field(None, alias="name")

    namespace_selector: V1LabelSelector | None = Field(None, alias="namespaceSelector")

    object_selector: V1LabelSelector | None = Field(None, alias="objectSelector")

    rules: list[V1RuleWithOperations] | None = Field(None, alias="rules")

    side_effects: str | None = Field(None, alias="sideEffects")

    timeout_seconds: int | None = Field(None, alias="timeoutSeconds")
