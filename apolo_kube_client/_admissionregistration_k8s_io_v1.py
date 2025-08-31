from kubernetes.client.models import (
    V1MutatingWebhookConfiguration,
    V1MutatingWebhookConfigurationList,
    V1Status,
)

from ._base_resource import ClusterScopedResource
from ._core import _KubeCore


class AdmissionRegistrationK8SioV1Api:
    """
    AdmissionRegistrationK8sIo v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "apis/admissionregistration.k8s.io/v1"

    def __init__(self, core: _KubeCore) -> None:
        self._core = core
        self.mutating_webhook_configuration = MutatingWebhookConfiguration(
            core, self.group_api_query_path
        )


class MutatingWebhookConfiguration(
    ClusterScopedResource[
        V1MutatingWebhookConfiguration,
        V1MutatingWebhookConfigurationList,
        V1Status,
    ]
):
    query_path = "mutatingwebhookconfigurations"
