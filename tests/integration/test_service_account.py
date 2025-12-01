from uuid import uuid4

from apolo_kube_client import (
    AuthenticationV1TokenRequest,
    KubeClient,
    V1ObjectMeta,
    V1ServiceAccount,
    V1TokenRequestSpec,
)


async def test_service_account(kube_client: KubeClient) -> None:
    name = f"test-sa-{uuid4().hex[:8]}"

    sa = V1ServiceAccount(metadata=V1ObjectMeta(name=name))
    created = await kube_client.core_v1.serviceaccounts.create(sa, namespace="default")
    assert created.metadata.name == name

    fetched = await kube_client.core_v1.serviceaccounts.get(
        name=name, namespace="default"
    )
    assert fetched.metadata.name == name

    sa_list = await kube_client.core_v1.serviceaccounts.get_list()
    names = {s.metadata.name for s in sa_list.items}
    assert name in names

    token_request = AuthenticationV1TokenRequest(
        spec=V1TokenRequestSpec(audiences=["api"])
    )
    token_response = await kube_client.core_v1.serviceaccounts[name].token.create(
        token_request,
        namespace="default",
    )

    assert token_response.status is not None
    assert token_response.status.token
    assert token_response.status.expiration_timestamp is not None

    await kube_client.core_v1.serviceaccounts.delete(name=name, namespace="default")
