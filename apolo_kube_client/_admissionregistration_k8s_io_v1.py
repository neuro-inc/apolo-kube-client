from ._attr import _Attr
from ._base_resource import ClusterScopedResource
from ._core import KubeCore
from ._models import (
    V1MutatingWebhookConfiguration,
    V1MutatingWebhookConfigurationList,
    V1Status,
)


class MutatingWebhookConfiguration(
    ClusterScopedResource[
        V1MutatingWebhookConfiguration,
        V1MutatingWebhookConfigurationList,
        V1Status,
    ]
):
    query_path = "mutatingwebhookconfigurations"


class AdmissionRegistrationK8SioV1Api:
    """
    AdmissionRegistrationK8sIo v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/admissionregistration.k8s.io/v1"

    mutating_webhook_configuration = _Attr(
        MutatingWebhookConfiguration, group_api_query_path
    )

    def __init__(self, core: KubeCore) -> None:
        self._core = core
