from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .admissionregistration_v1_webhook_client_config import (
    AdmissionregistrationV1WebhookClientConfig,
)
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_label_selector import V1LabelSelector
from .v1_match_condition import V1MatchCondition
from .v1_rule_with_operations import V1RuleWithOperations
from pydantic import BeforeValidator

__all__ = ("V1ValidatingWebhook",)


class V1ValidatingWebhook(BaseModel):
    """ValidatingWebhook describes an admission webhook and the resources and operations it applies to."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.admissionregistration.v1.ValidatingWebhook"
    )

    admission_review_versions: Annotated[
        list[str],
        Field(
            alias="admissionReviewVersions",
            description="""AdmissionReviewVersions is an ordered list of preferred `AdmissionReview` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy.""",
        ),
    ]

    client_config: Annotated[
        AdmissionregistrationV1WebhookClientConfig,
        Field(
            alias="clientConfig",
            description="""ClientConfig defines how to communicate with the hook. Required""",
        ),
    ]

    failure_policy: Annotated[
        str | None,
        Field(
            alias="failurePolicy",
            description="""FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    match_conditions: Annotated[
        list[V1MatchCondition],
        Field(
            alias="matchConditions",
            description="""MatchConditions is a list of conditions that must be met for a request to be sent to this webhook. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.

The exact matching logic is (in order):
  1. If ANY matchCondition evaluates to FALSE, the webhook is skipped.
  2. If ALL matchConditions evaluate to TRUE, the webhook is called.
  3. If any matchCondition evaluates to an error (but none are FALSE):
     - If failurePolicy=Fail, reject the request
     - If failurePolicy=Ignore, the error is ignored and the webhook is skipped""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    match_policy: Annotated[
        str | None,
        Field(
            alias="matchPolicy",
            description='''matchPolicy defines how the "rules" list is used to match incoming requests. Allowed values are "Exact" or "Equivalent".

- Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.

- Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and "rules" only included `apiGroups:["apps"], apiVersions:["v1"], resources: ["deployments"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.

Defaults to "Equivalent"''',
            exclude_if=lambda v: v is None,
        ),
    ] = None

    name: Annotated[
        str,
        Field(
            description="""The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where "imagepolicy" is the name of the webhook, and kubernetes.io is the name of the organization. Required."""
        ),
    ]

    namespace_selector: Annotated[
        V1LabelSelector,
        Field(
            alias="namespaceSelector",
            description="""NamespaceSelector decides whether to run the webhook on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the webhook.

For example, to run the webhook on any objects whose namespace is not associated with "runlevel" of "0" or "1";  you will set the selector as follows: "namespaceSelector": {
  "matchExpressions": [
    {
      "key": "runlevel",
      "operator": "NotIn",
      "values": [
        "0",
        "1"
      ]
    }
  ]
}

If instead you want to only run the webhook on any objects whose namespace is associated with the "environment" of "prod" or "staging"; you will set the selector as follows: "namespaceSelector": {
  "matchExpressions": [
    {
      "key": "environment",
      "operator": "In",
      "values": [
        "prod",
        "staging"
      ]
    }
  ]
}

See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels for more examples of label selectors.

Default to the empty LabelSelector, which matches everything.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LabelSelector)),
    ] = V1LabelSelector()

    object_selector: Annotated[
        V1LabelSelector,
        Field(
            alias="objectSelector",
            description="""ObjectSelector decides whether to run the webhook based on if the object has matching labels. objectSelector is evaluated against both the oldObject and newObject that would be sent to the webhook, and is considered to match if either object matches the selector. A null object (oldObject in the case of create, or newObject in the case of delete) or an object that cannot have labels (like a DeploymentRollback or a PodProxyOptions object) is not considered to match. Use the object selector only if the webhook is opt-in, because end users may skip the admission webhook by setting the labels. Default to the empty LabelSelector, which matches everything.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1LabelSelector)),
    ] = V1LabelSelector()

    rules: Annotated[
        list[V1RuleWithOperations],
        Field(
            description="""Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    side_effects: Annotated[
        str,
        Field(
            alias="sideEffects",
            description="""SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some.""",
        ),
    ]

    timeout_seconds: Annotated[
        int | None,
        Field(
            alias="timeoutSeconds",
            description="""TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
