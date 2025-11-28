from uuid import uuid4

from apolo_kube_client import (
    KubeClient,
    RbacV1Subject,
    V1ClusterRole,
    V1ClusterRoleBinding,
    V1ClusterRoleBindingList,
    V1ClusterRoleList,
    V1ObjectMeta,
    V1PolicyRule,
    V1RoleRef,
)


async def test_cluster_role_crud(kube_client: KubeClient) -> None:
    name = f"test-cr-{uuid4().hex[:8]}"

    role = V1ClusterRole(
        metadata=V1ObjectMeta(name=name),
        rules=[
            V1PolicyRule(
                api_groups=[""],
                resources=["pods"],
                verbs=["get"],
            )
        ],
    )

    created = await kube_client.rbac_authorization_k8s_io_v1.cluster_role.create(role)
    assert created.metadata.name == name

    fetched = await kube_client.rbac_authorization_k8s_io_v1.cluster_role.get(name=name)
    assert fetched.metadata.name == name

    roles = await kube_client.rbac_authorization_k8s_io_v1.cluster_role.get_list()
    assert isinstance(roles, V1ClusterRoleList)
    names = {r.metadata.name for r in roles.items}
    assert name in names

    status = await kube_client.rbac_authorization_k8s_io_v1.cluster_role.delete(
        name=name
    )
    assert status.status == "Success"


async def test_cluster_role_binding_crud(kube_client: KubeClient) -> None:
    role_name = f"test-cr-{uuid4().hex[:8]}"
    binding_name = f"test-crb-{uuid4().hex[:8]}"

    role = V1ClusterRole(
        metadata=V1ObjectMeta(name=role_name),
        rules=[
            V1PolicyRule(
                api_groups=[""],
                resources=["pods"],
                verbs=["get"],
            )
        ],
    )
    await kube_client.rbac_authorization_k8s_io_v1.cluster_role.create(role)

    binding = V1ClusterRoleBinding(
        metadata=V1ObjectMeta(name=binding_name),
        role_ref=V1RoleRef(
            api_group="rbac.authorization.k8s.io",
            kind="ClusterRole",
            name=role_name,
        ),
        subjects=[
            RbacV1Subject(
                kind="ServiceAccount",
                name="default",
                namespace="default",
            )
        ],
    )

    created = (
        await kube_client.rbac_authorization_k8s_io_v1.cluster_role_binding.create(
            binding
        )
    )
    assert created.metadata.name == binding_name

    fetched = await kube_client.rbac_authorization_k8s_io_v1.cluster_role_binding.get(
        name=binding_name
    )
    assert fetched.metadata.name == binding_name

    bindings = (
        await kube_client.rbac_authorization_k8s_io_v1.cluster_role_binding.get_list()
    )
    assert isinstance(bindings, V1ClusterRoleBindingList)
    names = {b.metadata.name for b in bindings.items}
    assert binding_name in names

    status = await kube_client.rbac_authorization_k8s_io_v1.cluster_role_binding.delete(
        name=binding_name
    )
    assert status.status == "Success"

    await kube_client.rbac_authorization_k8s_io_v1.cluster_role.delete(name=role_name)
