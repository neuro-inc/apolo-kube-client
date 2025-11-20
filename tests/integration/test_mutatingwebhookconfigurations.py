from typing import Callable

from apolo_kube_client import KubeClient
from apolo_kube_client._utils import base64_encode
from apolo_kube_client import (
    AdmissionregistrationV1ServiceReference,
    AdmissionregistrationV1WebhookClientConfig,
    V1LabelSelector,
    V1LabelSelectorRequirement,
    V1MutatingWebhook,
    V1MutatingWebhookConfiguration,
    V1ObjectMeta,
    V1RuleWithOperations,
)


class TestMutatingWebhookConfigurations:
    async def test_crud(
        self, kube_client: KubeClient, generate_certs: Callable[[str], tuple[str, str]]
    ) -> None:
        service_name = "test-service"
        _, ca_cert = generate_certs("k8s-test-ca")
        client_config = AdmissionregistrationV1WebhookClientConfig(
            service=AdmissionregistrationV1ServiceReference(
                namespace=kube_client.namespace,
                name=service_name,
                path="/mutate",
            ),
            ca_bundle=base64_encode(ca_cert),
        )
        mvc = V1MutatingWebhookConfiguration(
            metadata=V1ObjectMeta(name="test-mvc"),
            webhooks=[
                V1MutatingWebhook(
                    name=f"{service_name}.apolo.us",
                    admission_review_versions=["v1", "v1beta1"],
                    side_effects="None",
                    client_config=client_config,
                    object_selector=V1LabelSelector(),
                    namespace_selector=V1LabelSelector(
                        match_labels={},
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="platform.apolo.us/org",
                                operator="Exists",
                                values=[],
                            )
                        ],
                    ),
                    rules=[
                        V1RuleWithOperations(
                            operations=["CREATE"],
                            api_groups=[""],
                            api_versions=["v1"],
                            resources=["pods"],
                        )
                    ],
                    failure_policy="Ignore",
                    reinvocation_policy="Never",
                    timeout_seconds=30,
                )
            ],
        )

        # test creating a
        mvc_create = await kube_client.admission_registration_k8s_io_v1.mutating_webhook_configuration.create(
            model=mvc
        )
        assert mvc_create.metadata.name == mvc_create.metadata.name

        assert mvc.metadata.name is not None
        # test getting the mutating_webhook_configuration
        mvc_get = await kube_client.admission_registration_k8s_io_v1.mutating_webhook_configuration.get(
            name=mvc.metadata.name
        )
        assert mvc_get.metadata.name == mvc.metadata.name

        # test listing mutating_webhook_configuration
        mvc_list = await kube_client.admission_registration_k8s_io_v1.mutating_webhook_configuration.get_list()  # fmt: skip
        mvc_names = {m.metadata.name for m in mvc_list.items}
        assert len(mvc_list.items) > 0
        assert mvc.metadata.name in mvc_names

        # test deleting the mutating_webhook_configuration
        mvc_status = await kube_client.admission_registration_k8s_io_v1.mutating_webhook_configuration.delete(
            name=mvc.metadata.name
        )
        assert mvc_status.status == "Success"
