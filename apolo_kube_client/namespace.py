import dataclasses
import re
from hashlib import sha256
from typing import Any, Optional

from apolo_kube_client.client import KubeClient

KUBE_NAME_LENGTH_MAX = 63
DASH = "-"
KUBE_NAMESPACE_SEP = DASH * 2
KUBE_NAMESPACE_PREFIX = "platform"
KUBE_NAMESPACE_HASH_LENGTH = 24
NO_ORG = "NO_ORG"
RE_DASH_REPLACEABLE = re.compile(r"[\s_:]+")


# todo: this doesn't really belongs to a kube client, and should be removed,
#  once we'll have an event-system in place.
#  the reason why it's here, is that we want to avoid a code duplication.
def generate_namespace_name(org_name: str, project_name: str) -> str:
    """
    returns a Kubernetes resource name in the format
    `platform--<org_name>--<project_name>--<hash>`,
    ensuring that the total length does not exceed `KUBE_NAME_LENGTH_MAX` characters.

    - `platform--` prefix is never truncated
    - `<hash>` (a sha256 truncated to 24 chars), is also never truncated
    - if the names are long, we truncate them evenly,
      so at least some parts of both org and proj names will remain
    """

    # normalize names, by replacing illegal characters with dashes, lower-casing, etc.
    org_name = re.sub(RE_DASH_REPLACEABLE, DASH, org_name).lower().strip()
    project_name = re.sub(RE_DASH_REPLACEABLE, DASH, project_name).lower().strip()

    hashable = f"{org_name}{KUBE_NAMESPACE_SEP}{project_name}"
    name_hash = sha256(hashable.encode("utf-8")).hexdigest()[
        :KUBE_NAMESPACE_HASH_LENGTH
    ]

    len_reserved = (
        len(KUBE_NAMESPACE_PREFIX)
        + (len(KUBE_NAMESPACE_SEP) * 2)
        + KUBE_NAMESPACE_HASH_LENGTH
    )
    len_free = KUBE_NAME_LENGTH_MAX - len_reserved
    if len(hashable) <= len_free:
        return (
            f"{KUBE_NAMESPACE_PREFIX}"
            f"{KUBE_NAMESPACE_SEP}"
            f"{hashable}"
            f"{KUBE_NAMESPACE_SEP}"
            f"{name_hash}"
        )

    # org and project names do not fit into a full length.
    # let's figure out the full length of org and proj, and calculate a ratio
    # between org and project, so that we'll truncate more chars from the
    # string which actually has more chars
    len_org, len_proj = len(org_name), len(project_name)
    len_org_proj = len_org + len_proj + len(KUBE_NAMESPACE_SEP)
    exceeds = len_org_proj - len_free

    # ratio calculation. for proj can be derived via an org ratio
    remove_from_org = round((len_org / len_org_proj) * exceeds)
    remove_from_proj = exceeds - remove_from_org

    new_org_name = org_name[: max(1, len_org - remove_from_org)]
    new_project_name = project_name[: max(1, len_proj - remove_from_proj)]

    return (
        f"{KUBE_NAMESPACE_PREFIX}"
        f"{KUBE_NAMESPACE_SEP}"
        f"{new_org_name}"
        f"{KUBE_NAMESPACE_SEP}"
        f"{new_project_name}"
        f"{KUBE_NAMESPACE_SEP}"
        f"{name_hash}"
    )


@dataclasses.dataclass
class Label:
    name: str
    value: str


@dataclasses.dataclass
class Namespace:
    uid: str
    name: str
    labels: list[Label]

    @property
    def labels_as_dict(self) -> dict[str, str]:
        return {label.name: label.value for label in self.labels}

    @classmethod
    def from_kube(cls, kube_response: dict[str, Any]) -> "Namespace":
        return cls(
            uid=kube_response["metadata"]["uid"],
            name=kube_response["metadata"]["name"],
            labels=[
                Label(name=name, value=value)
                for name, value in kube_response["metadata"]["labels"].items()
            ],
        )


class NamespaceApi:
    """
    Namespace APIs wrapper
    """

    def __init__(self, kube_client: KubeClient):
        self._kube = kube_client

    async def get_namespaces(self) -> list[Namespace]:
        namespaces = await self._kube.get(self._kube.namespaces_url)
        return [Namespace.from_kube(spec) for spec in namespaces["items"]]

    async def get_namespace(self, name: str) -> Namespace:
        url = self._kube.generate_namespace_url(name)
        response = await self._kube.get(url=url)
        return Namespace.from_kube(response)

    async def create_namespace(
        self, name: str, *, labels: Optional[dict[str, str]] = None
    ) -> Namespace:
        payload: dict[str, Any] = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {"name": name},
        }
        if labels:
            payload["metadata"]["labels"] = labels
        response = await self._kube.post(url=self._kube.namespaces_url, json=payload)
        return Namespace.from_kube(response)

    async def delete_namespace(self, name: str) -> dict[str, Any]:
        url = self._kube.generate_namespace_url(name)
        return await self._kube.delete(url)
