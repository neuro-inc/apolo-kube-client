from pydantic import AliasChoices, BaseModel, Field
from .admissionregistration_v1_webhook_client_config import (
    AdmissionregistrationV1WebhookClientConfig,
)
from .base import _default_if_none
from .v1_label_selector import V1LabelSelector
from .v1_match_condition import V1MatchCondition
from .v1_rule_with_operations import V1RuleWithOperations
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ValidatingWebhook",)


class V1ValidatingWebhook(BaseModel):
    admission_review_versions: list[str] = Field(
        default=[],
        serialization_alias="admissionReviewVersions",
        validation_alias=AliasChoices(
            "admission_review_versions", "admissionReviewVersions"
        ),
    )

    client_config: Annotated[
        AdmissionregistrationV1WebhookClientConfig,
        BeforeValidator(_default_if_none(AdmissionregistrationV1WebhookClientConfig)),
    ] = Field(
        default_factory=lambda: AdmissionregistrationV1WebhookClientConfig(),
        serialization_alias="clientConfig",
        validation_alias=AliasChoices("client_config", "clientConfig"),
    )

    failure_policy: str | None = Field(
        default=None,
        serialization_alias="failurePolicy",
        validation_alias=AliasChoices("failure_policy", "failurePolicy"),
    )

    match_conditions: list[V1MatchCondition] = Field(
        default=[],
        serialization_alias="matchConditions",
        validation_alias=AliasChoices("match_conditions", "matchConditions"),
    )

    match_policy: str | None = Field(
        default=None,
        serialization_alias="matchPolicy",
        validation_alias=AliasChoices("match_policy", "matchPolicy"),
    )

    name: str | None = None

    namespace_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="namespaceSelector",
        validation_alias=AliasChoices("namespace_selector", "namespaceSelector"),
    )

    object_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="objectSelector",
        validation_alias=AliasChoices("object_selector", "objectSelector"),
    )

    rules: list[V1RuleWithOperations] = []

    side_effects: str | None = Field(
        default=None,
        serialization_alias="sideEffects",
        validation_alias=AliasChoices("side_effects", "sideEffects"),
    )

    timeout_seconds: int | None = Field(
        default=None,
        serialization_alias="timeoutSeconds",
        validation_alias=AliasChoices("timeout_seconds", "timeoutSeconds"),
    )
