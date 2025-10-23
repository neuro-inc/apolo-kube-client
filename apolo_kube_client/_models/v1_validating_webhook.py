from pydantic import AliasChoices, BaseModel, Field
from .admissionregistration_v1_webhook_client_config import (
    AdmissionregistrationV1WebhookClientConfig,
)
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_label_selector import V1LabelSelector
from .v1_match_condition import V1MatchCondition
from .v1_rule_with_operations import V1RuleWithOperations
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ValidatingWebhook",)


class V1ValidatingWebhook(BaseModel):
    admission_review_versions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="admissionReviewVersions",
        validation_alias=AliasChoices(
            "admission_review_versions", "admissionReviewVersions"
        ),
        exclude_if=_exclude_if,
    )

    client_config: Annotated[
        AdmissionregistrationV1WebhookClientConfig,
        BeforeValidator(_default_if_none(AdmissionregistrationV1WebhookClientConfig)),
    ] = Field(
        default_factory=lambda: AdmissionregistrationV1WebhookClientConfig(),
        serialization_alias="clientConfig",
        validation_alias=AliasChoices("client_config", "clientConfig"),
        exclude_if=_exclude_if,
    )

    failure_policy: str | None = Field(
        default=None,
        serialization_alias="failurePolicy",
        validation_alias=AliasChoices("failure_policy", "failurePolicy"),
        exclude_if=_exclude_if,
    )

    match_conditions: Annotated[
        list[V1MatchCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="matchConditions",
        validation_alias=AliasChoices("match_conditions", "matchConditions"),
        exclude_if=_exclude_if,
    )

    match_policy: str | None = Field(
        default=None,
        serialization_alias="matchPolicy",
        validation_alias=AliasChoices("match_policy", "matchPolicy"),
        exclude_if=_exclude_if,
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespace_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="namespaceSelector",
        validation_alias=AliasChoices("namespace_selector", "namespaceSelector"),
        exclude_if=_exclude_if,
    )

    object_selector: Annotated[
        V1LabelSelector, BeforeValidator(_default_if_none(V1LabelSelector))
    ] = Field(
        default_factory=lambda: V1LabelSelector(),
        serialization_alias="objectSelector",
        validation_alias=AliasChoices("object_selector", "objectSelector"),
        exclude_if=_exclude_if,
    )

    rules: Annotated[
        list[V1RuleWithOperations], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    side_effects: str | None = Field(
        default=None,
        serialization_alias="sideEffects",
        validation_alias=AliasChoices("side_effects", "sideEffects"),
        exclude_if=_exclude_if,
    )

    timeout_seconds: int | None = Field(
        default=None,
        serialization_alias="timeoutSeconds",
        validation_alias=AliasChoices("timeout_seconds", "timeoutSeconds"),
        exclude_if=_exclude_if,
    )
